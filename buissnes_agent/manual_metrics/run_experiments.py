"""
Runner for experiments E1-E5 (chapter 4, "Experiment plan").

E1: chunking quality comparison for four strategies,
E2: cost and processing-time comparison,
E3: size x overlap parameter ablation,
E4: system resilience to failures (LLM / embedding endpoint),
E5: retrieval A/B - dense (pure vector) vs hybrid (dense + sparse BM25,
    RRF fusion) on ONE collection; Hit@k / Recall@k / MRR against a
    query set with ground truth (config/e5_queries.json).

Each run goes through the full SearchKnowledgebase pipeline
(load -> chunk -> embed -> store); per-document results
(quality + cost + time) are saved to the metrics database
(ChunkingRunMetrics) via get_repository().insert_chunking_metrics_manual()
(wiersze manualne trafiaja do tabeli rag_chunking_metrics_manual).

Dataset source is selected in .env:
    MANUAL_METRICS_SOURCE=local   (default; dataset_path directory)
    MANUAL_METRICS_SOURCE=s3      (bucket: MANUAL_METRICS_S3_BUCKET,
                                   fallback S3_BUCKET;
                                   optional MANUAL_METRICS_S3_PREFIX)

Usage:
    python -m buissnes_agent.manual_metrics.run_experiments --exp all
    python -m buissnes_agent.manual_metrics.run_experiments --exp E1
    python -m buissnes_agent.manual_metrics.run_experiments --exp E4
"""
import argparse
import json
import os
import platform
import sys
from contextlib import contextmanager, nullcontext
from dataclasses import fields
from datetime import datetime
from types import MethodType
from typing import Any, Dict, List, Optional

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
# Allow both invocation styles: as a module (python -m ...) and
# directly (python buissnes_agent/manual_metrics/run_experiments.py)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import yaml
from dotenv import load_dotenv

from buissnes_agent.EmbeddingClient import LocalEmbeddingClient
from buissnes_agent.KnowledgebasePipeline import SearchKnowledgebase
from buissnes_agent.metrics import ChunkingRunMetrics, get_repository
from buissnes_agent.textchunker.langchain.strategies.new_agentic import (
    NewAgenticStrategy,
)

from buissnes_agent.evaluation.chunk_metrics import compute_chunk_metrics


# ==============================================================================
# COMPONENTS
# ==============================================================================
class InMemoryStore:
    """
    Vector store for measurement runs without a database
    (measures write time without a Qdrant dependency).
    """

    def __init__(self):
        self._count = 0

    def count(self) -> int:
        return self._count

    def insert_batch(self, items: List[Dict[str, Any]]) -> None:
        self._count += len(items)

    def search(self, query_vector: List[float], limit: int = 3) -> List[Dict]:
        return []


def _make_store(experiment_id: str):
    """Qdrant, if configured; otherwise InMemoryStore."""
    qdrant_url = os.getenv("QDRANT_API")
    if not qdrant_url:
        return InMemoryStore()

    from buissnes_agent.QdrantDatabaseStore import QdrantDatabaseStore

    try:
        dim = int(os.getenv("EMBEDDING_DIM"))
    except (TypeError, ValueError):
        dim = 1536

    return QdrantDatabaseStore(
        url=qdrant_url,
        api_key=os.getenv("QDRANT_API_KEY"),
        collection_name=f"exp_{experiment_id}",
        vector_size=dim,
    )


def _load_experiments_config(path: str) -> Dict[str, Any]:
    if not os.path.isabs(path):
        path = os.path.join(PROJECT_ROOT, path)
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def _quality_callback(client, chunk_size: int, min_chunk_len: int):
    """on_document hook: per-document quality metrics (E1)."""

    def callback(object_key, documents_list, processed_chunks) -> Dict[str, Any]:
        source_text = "\n".join(d.page_content for d in documents_list)
        try:
            quality = compute_chunk_metrics(
                processed_chunks,
                source_text,
                chunk_size=chunk_size,
                min_chunk_len=min_chunk_len,
                embeddings=client,
            )
        except Exception as e:
            # Fault-injected run (E4/embedding_failure): coherence needs the
            # embedding endpoint -> recompute without it (coherence = None),
            # all other quality metrics are still produced
            print(f"[warn] quality metrics for {object_key}: "
                  f"embeddings unavailable ({e}); "
                  f"recomputing without coherence")
            quality = compute_chunk_metrics(
                processed_chunks,
                source_text,
                chunk_size=chunk_size,
                min_chunk_len=min_chunk_len,
                embeddings=None,
            )
        return quality.to_dict()

    return callback


# ==============================================================================
# FAILURE SIMULATION (E4)
# ==============================================================================
class _BoomLLM:
    """LLM whose every call ends with an exception (E4: llm_failure)."""

    def invoke(self, *args, **kwargs):
        raise RuntimeError("simulated LLM outage (E4)")


@contextmanager
def _llm_fault():
    """
    E4/llm_failure: every new NewAgenticStrategy gets an LLM that
    always fails -> the real fallback path (llm_calls, fallbacks).
    """
    os.environ.setdefault("CHAT_BASE_URL", "http://fault.local/v1")
    os.environ.setdefault("CHAT_MODEL", "fault-model")

    original_init = NewAgenticStrategy.__init__

    def patched_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)
        self.llm = _BoomLLM()

    NewAgenticStrategy.__init__ = patched_init
    try:
        yield
    finally:
        NewAgenticStrategy.__init__ = original_init


@contextmanager
def _embedding_fault(client):
    """
    E4/embedding_failure: the embedding endpoint always rejects requests.
    """

    def boom(self, *args):
        # bound via MethodType: self is injected, *args swallows the payload
        raise RuntimeError("simulated embedding outage (E4)")

    original = client._post_with_retry
    client._post_with_retry = MethodType(boom, client)
    try:
        yield
    finally:
        client._post_with_retry = original


# ==============================================================================
# SINGLE RUN EXECUTION
# ==============================================================================
_VALID_RUN_FIELDS = {f.name for f in fields(ChunkingRunMetrics)}


def _to_run_metrics(record: Dict[str, Any], cfg: Dict[str, Any],
                    experiment_id: str, strategy: str) -> ChunkingRunMetrics:
    """Per-document record (with the quality hook) -> ChunkingRunMetrics."""
    data = {k: v for k, v in record.items() if k in _VALID_RUN_FIELDS}
    data["experiment_id"] = experiment_id
    data["strategy"] = strategy
    data.setdefault("num_chunks", 0)
    data.setdefault("timestamp", datetime.now().isoformat())
    data["batch_size"] = int(cfg.get("batch_size", 50))
    data["force_refresh"] = bool(cfg.get("force_refresh", True))
    data["embedding_model"] = os.getenv("EMBEDDING_MODEL")
    data["llm_model"] = os.getenv("CHAT_MODEL")
    data["python_version"] = platform.python_version()
    return ChunkingRunMetrics(**data)


def data_source() -> str:
    """Dataset source for experiments: 'local' or 's3' (MANUAL_METRICS_SOURCE)."""
    source = os.getenv("MANUAL_METRICS_SOURCE", "local").strip().lower()
    return source if source in ("local", "s3") else "local"


def _make_loader(source: str, dataset_path: str):
    """Build the data loader according to the configured source.

    local: DataLoaderLocalFileLoader over dataset_path (default),
    s3:    DataLoaderS3FileLoader over MANUAL_METRICS_S3_BUCKET
           (fallback: S3_BUCKET) with an optional MANUAL_METRICS_S3_PREFIX.
    """
    if source == "s3":
        from buissnes_agent.DataLoaderS3FileLoader import DataLoaderS3FileLoader

        bucket = os.getenv("MANUAL_METRICS_S3_BUCKET") or os.getenv(
            "S3_BUCKET", ""
        )
        if not bucket:
            raise ValueError(
                "MANUAL_METRICS_SOURCE=s3 requires a bucket: set "
                "MANUAL_METRICS_S3_BUCKET (or S3_BUCKET) in .env"
            )
        prefix = os.getenv("MANUAL_METRICS_S3_PREFIX", "")
        return DataLoaderS3FileLoader(bucket_name=bucket, prefix=prefix)

    from buissnes_agent.DataLoaderLocalFileLoader import (
        DataLoaderLocalFileLoader,
    )

    if not os.path.isabs(dataset_path):
        dataset_path = os.path.join(PROJECT_ROOT, dataset_path)
    return DataLoaderLocalFileLoader(directory=dataset_path)


def _run_one(
        cfg: Dict[str, Any],
        dataset_path: str,
        experiment_id: str,
        strategy: str,
        size: int,
        overlap: int,
        fault: Optional[str] = None
) -> Dict[str, Any]:
    """
    One experiment run: full pipeline + saving records
    to the metrics database + summary.
    """
    source = data_source()
    loader = _make_loader(source, dataset_path)
    total_docs = sum(1 for _ in loader.list_objects())

    client = LocalEmbeddingClient()
    store = _make_store(experiment_id)
    min_chunk_len = int(cfg.get("min_chunk_len", 50))

    fault_ctx = (
        _llm_fault() if fault == "llm_failure"
        else _embedding_fault(client) if fault == "embedding_failure"
        else nullcontext()
    )

    with fault_ctx:
        kb = SearchKnowledgebase(
            client=client,
            database_store=store,
            data_loader=loader,
            embedding_model=os.getenv("EMBEDDING_MODEL"),
            batch_size=int(cfg.get("batch_size", 50)),
            force_refresh=bool(cfg.get("force_refresh", True)),
            strategy_name=strategy,
            chunk_size=size,
            chunk_overlap=overlap,
            on_document=_quality_callback(client, size, min_chunk_len),
            # The runner saves the records itself (its own experiment_id) -
            # disables double saving in the pipeline
            persist_metrics=False,
        )

    # Save per-document results to the metrics database
    repository = get_repository()
    saved = 0
    for record in kb.document_results:
        run_metrics = _to_run_metrics(
            record, cfg, experiment_id, strategy
        )
        # Manual metrics go to the dedicated rag_chunking_metrics_manual
        # table (production ingestion keeps rag_chunking_metrics)
        if repository.insert_chunking_metrics_manual(run_metrics):
            saved += 1

    processed = len(kb.document_results)
    summary = {
        "experiment_id": experiment_id,
        "strategy": strategy,
        "size": size,
        "overlap": overlap,
        "fault": fault,
        "documents_total": total_docs,
        "documents_processed": processed,
        "documents_failed": total_docs - processed,
        "fallbacks": sum(r.get("fallbacks", 0) for r in kb.document_results),
        "llm_calls": sum(r.get("llm_calls", 0) for r in kb.document_results),
        "empty_chunks": sum(
            r.get("empty_chunks", 0) for r in kb.document_results
        ),
        "records_saved": saved,
    }
    print(f"[RUN] {json.dumps(summary, ensure_ascii=False)}")
    return summary


# ==============================================================================
# EXPERIMENTS
# ==============================================================================
def _stamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def _base_params(cfg: Dict[str, Any]) -> tuple:
    params = cfg.get("parameters", {})
    return int(params.get("size", 600)), int(params.get("overlap", 100))


def run_e1(cfg: Dict[str, Any], dataset_path: str) -> List[Dict[str, Any]]:
    """E1: chunking quality for four strategies."""
    size, overlap = _base_params(cfg)
    results = []
    for strategy in cfg.get("strategies", []):
        exp_id = f"E1_{strategy}_{size}_{overlap}_{_stamp()}"
        results.append(_run_one(cfg, dataset_path, exp_id, strategy, size, overlap))
    return results


def run_e2(cfg: Dict[str, Any], dataset_path: str) -> List[Dict[str, Any]]:
    """E2: cost and time (same runs, records contain the counters)."""
    size, overlap = _base_params(cfg)
    results = []
    for strategy in cfg.get("strategies", []):
        exp_id = f"E2_{strategy}_{size}_{overlap}_{_stamp()}"
        results.append(_run_one(cfg, dataset_path, exp_id, strategy, size, overlap))
    return results


def run_e3(cfg: Dict[str, Any], dataset_path: str) -> List[Dict[str, Any]]:
    """E3: size x overlap parameter ablation."""
    e3 = cfg.get("e3", {})
    strategies = e3.get("strategies", ["fixedSize", "sentenceBased"])
    sizes = e3.get("size", [300, 600, 1000])
    overlaps = e3.get("overlap", [0, 50, 100])
    min_chunk_len = int(cfg.get("min_chunk_len", 50))

    results = []
    for strategy in strategies:
        for size in sizes:
            for overlap in overlaps:
                if overlap >= size:
                    continue  # invalid configuration
                exp_id = f"E3_{strategy}_{size}_{overlap}_{_stamp()}"
                # For E3, quality metrics are computed with the current size limit
                cfg_local = dict(cfg)
                cfg_local["min_chunk_len"] = min(
                    min_chunk_len, max(1, int(size * 0.1))
                )
                results.append(
                    _run_one(cfg_local, dataset_path, exp_id, strategy,
                             int(size), int(overlap))
                )
    return results


def run_e4(cfg: Dict[str, Any], dataset_path: str,
           faults: Optional[List[str]] = None) -> List[Dict[str, Any]]:
    """E4: resilience to failures (agentic fallback / no embeddings).

    `faults` optionally filters the configured fault list (CLI: --fault).
    """
    e4 = cfg.get("e4", {})
    faults = faults or e4.get("faults", ["llm_failure", "embedding_failure"])
    fault_strategy = e4.get("fault_strategy_map", {
        "llm_failure": "agentic",
        "embedding_failure": "semanticChunker",
    })
    size, overlap = _base_params(cfg)

    results = []
    for fault in faults:
        strategy = fault_strategy.get(fault, "agentic")
        exp_id = f"E4_{fault}_{strategy}_{_stamp()}"
        results.append(
            _run_one(cfg, dataset_path, exp_id, strategy, size, overlap,
                     fault=fault)
        )
    return results


# ==============================================================================
# E5: RETRIEVAL A/B (dense vs hybrid BM25+RRF)
# ==============================================================================
# Both arms query the SAME collection (ingested once): the metric rows are
# distinguished by the "strategy" column (dense/hybrid) in the metrics DB,
# and the per-query results (retrieved IDs + ground truth match) are saved
# to results/e5_results.json for the thesis analysis (thesis_pipeline).
E5_STRATEGIES = ("dense", "hybrid")

# Payload fields used to match a chunk against the expected sources
# (ground truth = case-insensitive substring, any field).
E5_SOURCE_FIELDS = ("source", "title", "markdown_path", "url", "markdown_url")


def _load_e5_queries(cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Load the E5 query set (config/e5_queries.json)."""
    e5 = cfg.get("e5", {})
    queries_path = e5.get("queries_file", "config/e5_queries.json")
    if not os.path.isabs(queries_path):
        queries_path = os.path.join(PROJECT_ROOT, queries_path)
    with open(queries_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    queries = data.get("queries", [])
    for i, q in enumerate(queries, 1):
        q.setdefault("id", f"q{i:02d}")
        q["expected_sources"] = [
            s.lower() for s in q.get("expected_sources", [])
        ]
    return queries


def _e5_source_matches(payload: Dict[str, Any],
                       expected: List[str]) -> bool:
    """
    Ground truth: does any expected substring occur (case-insensitive)
    in any of the chunk's source payload fields?
    """
    if not expected:
        return False
    haystack = " ".join(
        str(payload.get(field) or "") for field in E5_SOURCE_FIELDS
    ).lower()
    return any(needle in haystack for needle in expected)


def run_e5(cfg: Dict[str, Any], dataset_path: str) -> Dict[str, Any]:
    """
    E5: dense vs hybrid retrieval on one corpus.

    1. (re)build the collection through SearchKnowledgebase (new schema:
       named "dense" vector + "sparse" BM25 placeholder),
    2. build the BM25 sparse index (post-ingestion pass),
    3. run the query set for BOTH arms via run_generic_rag_with_metrics,
    4. score each arm against the ground truth (Hit@k / Recall@k / MRR)
       from the retrieved point IDs,
    5. save results/e5_results.json (thesis_pipeline._analyze_e5 reads it).

    Requires Qdrant (QDRANT_API) and the metrics repository
    (METRICS_STORAGE_TYPE) - the retrieved IDs are carried by the
    retrieval metrics row.
    """
    e5 = cfg.get("e5", {})
    collection = e5.get("collection", "e5_retrieval")
    strategy_name = e5.get("strategy", "fixedSize")
    top_k = int(e5.get("top_k", 10))
    prefetch_limit = int(e5.get("prefetch_limit", 50))
    rebuild = bool(e5.get("rebuild", True))

    # E5 requires Qdrant - hybrid search (prefetch + RRF) runs in the DB
    qdrant_url = os.getenv("QDRANT_API")
    if not qdrant_url:
        raise RuntimeError(
            "E5 wymaga Qdrant (QDRANT_API w .env) - "
            "hybrydowe wyszukiwanie działa w bazie"
        )

    # Depth of each hybrid leg before the RRF fusion (.env may override)
    os.environ.setdefault("HYBRID_PREFETCH_LIMIT", str(prefetch_limit))

    from buissnes_agent.QdrantDatabaseStore import QdrantDatabaseStore

    try:
        dim = int(os.getenv("EMBEDDING_DIM"))
    except (TypeError, ValueError):
        dim = 1536
    store = QdrantDatabaseStore(
        url=qdrant_url,
        api_key=os.getenv("QDRANT_API_KEY"),
        collection_name=collection,
        vector_size=dim,
    )
    client = store.client

    size, overlap = _base_params(cfg)

    # 1) corpus - ingested ONCE; both arms query the same chunks
    source = data_source()
    loader = _make_loader(source, dataset_path)
    total_docs = sum(1 for _ in loader.list_objects())

    embedding_client = LocalEmbeddingClient()
    if rebuild or store.count() == 0:
        kb = SearchKnowledgebase(
            client=embedding_client,
            database_store=store,
            data_loader=loader,
            embedding_model=os.getenv("EMBEDDING_MODEL"),
            batch_size=int(cfg.get("batch_size", 50)),
            force_refresh=True,
            strategy_name=strategy_name,
            chunk_size=size,
            chunk_overlap=overlap,
            # E5 scores retrieval, not chunking quality - no doc hook
            on_document=None,
            persist_metrics=False,
        )
        print(f"[E5] Kolekcja '{collection}' zbudowana: "
              f"{store.count()} chunków z {total_docs} dokumentów")
    else:
        print(f"[E5] Kolekcja '{collection}' istnieje "
              f"({store.count()} chunków) - pomijam ingest")

    # 2) BM25 sparse index (the keyword leg of the hybrid)
    from buissnes_agent.Bm25Index import build_sparse_vectors, load_index

    if rebuild or load_index(collection) is None:
        build_sparse_vectors(client, collection)
    else:
        print(f"[E5] Indeks BM25 dla '{collection}' istnieje - pomijam")

    # 3) queries + ground truth
    queries = _load_e5_queries(cfg)

    # The retrieved IDs live in the retrieval metrics row -
    # the repository must be up (Postgres per .env)
    from buissnes_agent.tools.rag_metrics import metrics_collector
    if not metrics_collector.is_enabled():
        raise RuntimeError(
            "E5 wymaga repository metryk (METRICS_STORAGE_TYPE w .env) - "
            "identyfikatory pobranych chunków są zapisywane tam"
        )

    # Chunk payloads by ID (ground-truth matching)
    id_to_payload: Dict[str, Dict[str, Any]] = {}
    offset = None
    while True:
        points, offset = client.scroll(
            collection_name=collection,
            limit=512,
            offset=offset,
            with_payload=True,
            with_vectors=False,
        )
        for point in points:
            id_to_payload[str(point.id)] = point.payload or {}
        if offset is None:
            break
    if not id_to_payload:
        raise RuntimeError(
            f"E5: kolekcja '{collection}' nie ma żadnego punktu po ingest"
        )

    # 4) both arms on the same corpus
    from buissnes_agent.tools.tool_iso_rag import run_generic_rag_with_metrics

    per_query: List[Dict[str, Any]] = []
    for q in queries:
        expected = q.get("expected_sources", [])
        relevant_ids = {
            pid for pid, payload in id_to_payload.items()
            if _e5_source_matches(payload, expected)
        }
        entry: Dict[str, Any] = {
            "id": q["id"],
            "query": q["query"],
            "expected_sources": expected,
            "n_relevant": len(relevant_ids),
            "arms": {},
        }
        for arm in E5_STRATEGIES:
            output, metrics = run_generic_rag_with_metrics(
                query=q["query"],
                collection_name=collection,
                top_k=top_k,
                strategy=arm,
            )
            if metrics is None:
                raise RuntimeError(
                    f"E5: brak metryk dla '{q['id']}' ({arm}) - "
                    f"odpowiedź: {output}"
                )
            retrieved_ids = list(metrics.retrieved_ids or [])
            hit_ranks = [
                rank for rank, pid in enumerate(retrieved_ids, 1)
                if pid in relevant_ids
            ]
            entry["arms"][arm] = {
                "requested": arm,
                # the strategy ACTUALLY used (hybrid can fall back to dense
                # when the BM25 index is missing or the query has no
                # tokens from the index vocabulary)
                "strategy_used": metrics.strategy,
                "n_retrieved": len(retrieved_ids),
                "hit": bool(hit_ranks),
                "recall": (
                    len(set(retrieved_ids) & relevant_ids) / len(relevant_ids)
                    if relevant_ids else None
                ),
                "mrr": (1.0 / hit_ranks[0]) if hit_ranks else 0.0,
                "latency_ms": metrics.latency_ms,
                "search_latency_ms": metrics.search_latency_ms,
                "retrieved_ids": retrieved_ids,
            }
        per_query.append(entry)

    # 5) per-arm summary (only the queries the arm ACTUALLY ran -
    #    fallbacks are counted separately and excluded from the pairing)
    per_arm: Dict[str, Any] = {}
    for arm in E5_STRATEGIES:
        rows = [
            qe["arms"][arm] for qe in per_query
            if qe["arms"][arm]["strategy_used"] == arm
        ]
        recalls = [r["recall"] for r in rows if r["recall"] is not None]
        per_arm[arm] = {
            "n_queries": len(per_query),
            "n_ran": len(rows),
            "n_fallback": len(per_query) - len(rows),
            "hit_rate": (
                sum(1 for r in rows if r["hit"]) / len(rows)
            ) if rows else None,
            "recall_mean": (sum(recalls) / len(recalls)) if recalls else None,
            "mrr_mean": (
                sum(r["mrr"] for r in rows) / len(rows)
            ) if rows else None,
            "search_latency_mean_ms": (
                sum(r["search_latency_ms"] for r in rows) / len(rows)
            ) if rows else None,
        }

    result = {
        "experiment_id": f"E5_{collection}_{_stamp()}",
        "collection": collection,
        "chunking_strategy": strategy_name,
        "chunk_size": size,
        "chunk_overlap": overlap,
        "top_k": top_k,
        "prefetch_limit": prefetch_limit,
        "embedding_model": os.getenv("EMBEDDING_MODEL"),
        "documents_total": total_docs,
        "chunks": len(id_to_payload),
        "n_queries": len(per_query),
        "timestamp": datetime.now().isoformat(),
        "per_arm": per_arm,
        "queries": per_query,
    }

    out_path = os.path.join(PROJECT_ROOT, "results", "e5_results.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"[E5] Wyniki: {out_path}")
    return result


RUNNERS = {
    "E1": run_e1,
    "E2": run_e2,
    "E3": run_e3,
    "E4": run_e4,
    "E5": run_e5,
}


# ==============================================================================
# CLI
# ==============================================================================
def main(argv: Optional[List[str]] = None) -> int:
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Runner for experiments E1-E5 (chapter 4)"
    )
    parser.add_argument(
        "--exp", default="all",
        choices=["E1", "E2", "E3", "E4", "E5", "all"],
        help="which experiment to run (default: all)"
    )
    parser.add_argument(
        "--config", default="config/experiments.yaml",
        help="path to config/experiments.yaml"
    )
    parser.add_argument(
        "--dataset", default=None,
        help="override dataset_path from the configuration"
    )
    parser.add_argument(
        "--fault", default=None,
        help="E4 only: comma-separated fault filter "
             "(llm_failure,embedding_failure)"
    )
    args = parser.parse_args(argv)

    cfg = _load_experiments_config(args.config)
    dataset_path = args.dataset or cfg.get(
        "dataset_path", "buissnes_agent/inputs"
    )

    names = list(RUNNERS) if args.exp == "all" else [args.exp]
    print(
        f"= EKSPERYMENTY: {', '.join(names)} | "
        f"source: {data_source()} | dataset: {dataset_path} ="
    )

    fault_filter = (
        [f.strip() for f in args.fault.split(",") if f.strip()]
        if args.fault else None
    )

    for name in names:
        print(f"\n=== {name} ===")
        if name == "E4":
            run_e4(cfg, dataset_path, faults=fault_filter)
        else:
            RUNNERS[name](cfg, dataset_path)

    print("\n= KONIEC. Wyniki zapisane w bazie metryk "
          f"({os.getenv('METRICS_STORAGE_TYPE', 'file')}) =")
    return 0


if __name__ == "__main__":
    sys.exit(main())
