"""
Runner for experiments E1-E4 (chapter 4, "Experiment plan").

E1: chunking quality comparison for four strategies,
E2: cost and processing-time comparison,
E3: size x overlap parameter ablation,
E4: system resilience to failures (LLM / embedding endpoint).

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
        quality = compute_chunk_metrics(
            processed_chunks,
            source_text,
            chunk_size=chunk_size,
            min_chunk_len=min_chunk_len,
            embeddings=client,
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

    def boom(payload):
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


def run_e4(cfg: Dict[str, Any], dataset_path: str) -> List[Dict[str, Any]]:
    """E4: resilience to failures (agentic fallback / no embeddings)."""
    e4 = cfg.get("e4", {})
    faults = e4.get("faults", ["llm_failure", "embedding_failure"])
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


RUNNERS = {
    "E1": run_e1,
    "E2": run_e2,
    "E3": run_e3,
    "E4": run_e4,
}


# ==============================================================================
# CLI
# ==============================================================================
def main(argv: Optional[List[str]] = None) -> int:
    load_dotenv()

    parser = argparse.ArgumentParser(
        description="Runner for experiments E1-E4 (chapter 4)"
    )
    parser.add_argument(
        "--exp", default="all",
        choices=["E1", "E2", "E3", "E4", "all"],
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

    for name in names:
        print(f"\n=== {name} ===")
        RUNNERS[name](cfg, dataset_path)

    print("\n= KONIEC. Wyniki zapisane w bazie metryk "
          f"({os.getenv('METRICS_STORAGE_TYPE', 'file')}) =")
    return 0


if __name__ == "__main__":
    sys.exit(main())
