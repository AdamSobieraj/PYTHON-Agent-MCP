import logging
import os
import sys
import time
from typing import Optional, Tuple

import qdrant_client
from dotenv import load_dotenv
from buissnes_agent.EmbeddingClient import LocalEmbeddingClient

# ===== METRICS: IMPORT =====
try:
    from buissnes_agent.tools.rag_metrics import (
        MetricsCalculator,
        RetrievalMetrics,
        metrics_collector,
    )
except ImportError:
    from tools.rag_metrics import (  # type: ignore
        MetricsCalculator,
        RetrievalMetrics,
        metrics_collector,
    )
# ===========================

logger = logging.getLogger(__name__)
DEFAULT_VECTOR_AMOUNT_RAG = 10

# ==============================================================================
# GLOBAL RESOURCES (SINGLETONS)
# ==============================================================================
# We keep the Qdrant client and embedding model instances globally,
# so we don't create a new connection on every query (optimization).
_qdrant_client: Optional[qdrant_client.QdrantClient] = None
_embeddings: Optional[LocalEmbeddingClient] = None

load_dotenv()

def _init_resources():
    """
    ### LAZY RESOURCE INITIALIZATION (Lazy Loading)

    This function is called only on the first use of the tool.

    Why:
    1. Faster server startup (we don't wait for the DB connection at boot).
    2. Fault tolerance (if Qdrant is down, the server still starts, and the error only appears on the query).
    """
    global _qdrant_client, _embeddings

    # If the resources already exist, do nothing.
    if _qdrant_client and _embeddings:
        return

    try:
        # Fetch Qdrant configuration from .env
        qdrant_url = os.getenv('QDRANT_API')
        qdrant_key = os.getenv('QDRANT_API_KEY')

        # Verification only for Qdrant, since LocalEmbeddingClient checks its own variables itself
        if not qdrant_url:
            raise ValueError("Brak zmiennej QDRANT_API w pliku .env")

        # 1. Initialize the Qdrant vector database client
        logger.info(f"Łączenie z Qdrant: {qdrant_url}")
        _qdrant_client = qdrant_client.QdrantClient(
            url=qdrant_url,
            api_key=qdrant_key,
            # timeout=60 # Optionally increase the timeout
        )

        # 2. Initialize the embedding model (Local Embedding Client)
        # The class itself pulls: EMBEDDING_BASE_URL, EMBEDDING_API_KEY, EMBEDDING_MODEL from .env
        # and automatically fixes 400 Bad Request errors.
        logger.info("Inicjalizacja LocalEmbeddingClient...")
        _embeddings = LocalEmbeddingClient()

        print(f"[ISO Tool] Połączono z Qdrant i skonfigurowano Embeddingi ({_embeddings.model}).", file=sys.stderr)

    except Exception as e:
        err_msg = f"[ISO Tool] Błąd krytyczny inicjalizacji zasobów: {e}"
        print(err_msg, file=sys.stderr)
        logger.error(err_msg)
        raise e

# ==============================================================================
# METRIC HELPER METHODS (separated)
# ==============================================================================

def _measure_embedding_time(embedder, query: str) -> Tuple[list, int]:
    """
    Generate embedding with time measurement

    Returns:
        tuple: (query_vector, embedding_latency_ms)
    """
    start_time = time.time()
    query_vector = embedder.embed_query(query)
    latency_ms = MetricsCalculator.calculate_latency_ms(start_time)
    return query_vector, latency_ms


# ==============================================================================
# RETRIEVAL STRATEGY: dense (pure vector) vs hybrid (dense + sparse BM25, RRF)
# ==============================================================================

DEFAULT_RETRIEVAL_STRATEGY = "dense"
DEFAULT_HYBRID_PREFETCH_LIMIT = 50

# Collection -> dense vector name (None = old schema, single unnamed vector).
# Resolved once per collection per process (schema does not change at runtime).
_DENSE_VECTOR_NAMES: dict = {}
_SPARSE_VECTOR_NAMES: dict = {}


def resolve_strategy(strategy: str | None = None) -> str:
    """
    Resolve the retrieval strategy: explicit argument takes precedence,
    then RETRIEVAL_STRATEGY from .env, then the "dense" default
    (so behaviour is unchanged until the flag is set).
    """
    if strategy:
        resolved = strategy.strip().lower()
        if resolved:
            return resolved
    env_value = (os.getenv("RETRIEVAL_STRATEGY") or "").strip().lower()
    return env_value or DEFAULT_RETRIEVAL_STRATEGY


def _resolve_prefetch_limit() -> int:
    """HYBRID_PREFETCH_LIMIT from .env (how deep each leg fetches before RRF)."""
    env_value = (os.getenv("HYBRID_PREFETCH_LIMIT") or "").strip()
    if not env_value:
        return DEFAULT_HYBRID_PREFETCH_LIMIT
    try:
        resolved = int(env_value)
    except ValueError:
        logger.warning(
            "Invalid HYBRID_PREFETCH_LIMIT=%r. Falling back to %s.",
            env_value,
            DEFAULT_HYBRID_PREFETCH_LIMIT,
        )
        return DEFAULT_HYBRID_PREFETCH_LIMIT
    return resolved if resolved > 0 else DEFAULT_HYBRID_PREFETCH_LIMIT


def _collection_vector_names(client, collection_name: str) -> Tuple[Optional[str], bool]:
    """
    Returns (dense_vector_name, has_sparse) for the collection schema.

    dense_vector_name: "dense" for the new schema (named vectors),
    None for the old schema (a single unnamed vector).
    has_sparse: whether the collection has the named "sparse" vector.
    """
    if collection_name not in _DENSE_VECTOR_NAMES:
        try:
            info = client.get_collection(collection_name)
            vectors = info.config.params.vectors
            dense_name = "dense" if isinstance(vectors, dict) and "dense" in vectors else None
            sparse_config = info.config.params.sparse_vectors
            has_sparse = bool(sparse_config) and "sparse" in sparse_config
        except Exception as e:
            logger.warning(
                "Nie udało się odczytać schematu kolekcji %s: %s", collection_name, e
            )
            dense_name, has_sparse = None, False
        _DENSE_VECTOR_NAMES[collection_name] = dense_name
        _SPARSE_VECTOR_NAMES[collection_name] = has_sparse
    return _DENSE_VECTOR_NAMES[collection_name], _SPARSE_VECTOR_NAMES[collection_name]


def _measure_search_time(client, collection_name: str, query: str,
                         query_vector: list, top_k: int,
                         strategy: str = "dense"):
    """
    Perform search with time measurement.

    strategy:
        "dense"  -- pure vector search (query_points on the dense vector)
        "hybrid" -- Qdrant native hybrid: two prefetches (dense + sparse
                    BM25 from the app-side index) fused with RRF on the server.

    Falls back to dense (and reports the strategy actually used) when the
    BM25 index is missing, the collection has no sparse vector, or the
    query contains no tokens from the index vocabulary.

    Returns:
        tuple: (search_response, search_latency_ms, strategy_used)
    """
    start_time = time.time()
    dense_name, has_sparse = _collection_vector_names(client, collection_name)

    # ---- hybrid leg (only when requested AND everything is in place) ----
    if strategy == "hybrid" and has_sparse:
        try:
            from buissnes_agent.Bm25Index import load_index
        except ImportError:
            from Bm25Index import load_index  # type: ignore

        index = load_index(collection_name)
        if index is None:
            logger.warning(
                "Hybryda: brak indeksu BM25 dla kolekcji '%s' -- "
                "używam czystego wyszukiwania wektorowego.", collection_name
            )
        else:
            sparse_indices, sparse_values = index.encode_query(query)
            if not sparse_indices:
                logger.warning(
                    "Hybryda: zapytanie nie zawiera tokenów ze słownika BM25 -- "
                    "używam czystego wyszukiwania wektorowego."
                )
            else:
                from qdrant_client.models import Fusion, FusionQuery, Prefetch, SparseVector

                prefetch_k = _resolve_prefetch_limit()
                dense_prefetch = {"query": query_vector, "limit": prefetch_k}
                if dense_name is not None:
                    dense_prefetch["using"] = dense_name
                search_response = client.query_points(
                    collection_name=collection_name,
                    prefetch=[
                        Prefetch(**dense_prefetch),
                        Prefetch(
                            query=SparseVector(indices=sparse_indices, values=sparse_values),
                            using="sparse",
                            limit=prefetch_k,
                        ),
                    ],
                    query=FusionQuery(fusion=Fusion.RRF),
                    limit=top_k,
                    with_payload=True,
                )
                latency_ms = MetricsCalculator.calculate_latency_ms(start_time)
                return search_response, latency_ms, "hybrid"

    # ---- dense (default + fallback) ----
    query_kwargs = {}
    if dense_name is not None:
        query_kwargs["using"] = dense_name
    search_response = client.query_points(
        collection_name=collection_name,
        query=query_vector,
        limit=top_k,
        with_payload=True,
        **query_kwargs
    )
    latency_ms = MetricsCalculator.calculate_latency_ms(start_time)
    return search_response, latency_ms, "dense"


def resolve_top_k(top_k: int | None = None) -> int:
    """
    Resolve the effective retrieval limit.

    Explicit top_k takes precedence. When it is not provided, the function
    falls back to VECTOR_AMOUNT_RAG from the environment and then to the code
    default.
    """
    if top_k is not None:
        if top_k <= 0:
            raise ValueError("top_k must be a positive integer when provided.")
        return top_k

    env_value = (os.getenv("VECTOR_AMOUNT_RAG") or "").strip()
    if not env_value:
        return DEFAULT_VECTOR_AMOUNT_RAG

    try:
        resolved_top_k = int(env_value)
    except ValueError:
        logger.warning(
            "Invalid VECTOR_AMOUNT_RAG=%r. Falling back to %s.",
            env_value,
            DEFAULT_VECTOR_AMOUNT_RAG,
        )
        return DEFAULT_VECTOR_AMOUNT_RAG

    if resolved_top_k <= 0:
        logger.warning(
            "Non-positive VECTOR_AMOUNT_RAG=%r. Falling back to %s.",
            env_value,
            DEFAULT_VECTOR_AMOUNT_RAG,
        )
        return DEFAULT_VECTOR_AMOUNT_RAG

    return resolved_top_k


def _format_search_results(points) -> str:
    """
    Format search results into readable text

    Args:
        points: List of points from Qdrant

    Returns:
        str: Formatted output
    """
    formatted_output = []

    for i, point in enumerate(points, 1):
        payload = point.payload or {}

        # Extract fields from the payload
        content = payload.get("phrase") or payload.get("text") or "[BRAK TREŚCI]"
        title = payload.get("title", "Bez tytułu")
        source_path = payload.get("source", "Nieznane źródło")
        url = payload.get("url", "-")
        domain = payload.get("domain", "ogólna")
        extension = payload.get("extension", "")
        meta_id = payload.get("phrase_metadata_id", "brak-id")

        tags_list = payload.get("tags", [])
        tags_str = ", ".join(tags_list) if isinstance(tags_list, list) else str(tags_list)

        page = payload.get("page_number")
        page_info = f", Strona: {page}" if page else ""

        entry = (
            f"--- DOKUMENT {i} (Relewancja: {point.score:.4f}) ---\n"
            f"Tytuł: {title}\n"
            f"Źródło (plik): {source_path}{page_info}\n"
            f"URL: {url}\n"
            f"Domena: {domain}\n"
            f"Typ: {extension}\n"
            f"Tagi: {tags_str}\n"
            f"ID Fragmentu: {meta_id}\n"
            f"Treść:\n{content.strip()}"
        )
        formatted_output.append(entry)

    return "\n\n".join(formatted_output)


# ==============================================================================
# MAIN RAG FUNCTION WITH METRICS
# ==============================================================================

def run_generic_rag_with_metrics(
        query: str,
        collection_name: str,
        top_k: int | None = None,
        strategy: str | None = None,
) -> Tuple[str, Optional[RetrievalMetrics]]:
    """
    RAG with full retrieval metrics (if enabled in ENV)

    Args:
        query: User question
        collection_name: Collection name in Qdrant
        top_k: optional retrieval limit (see resolve_top_k)
        strategy: "dense" or "hybrid"; when omitted, RETRIEVAL_STRATEGY
                  from .env is used (default "dense")

    Returns:
        tuple: (formatted_output, retrieval_metrics)
               If the metrics repository is unavailable, metrics will be None
    """
    # Start timer for the whole process
    total_start = time.time()

    top_k = resolve_top_k(top_k)
    strategy = resolve_strategy(strategy)

    # ===== INITIALIZATION ERROR HANDLING =====
    try:
        _init_resources()
    except Exception as e:
        error_msg = f"Błąd techniczny: Nie udało się połączyć z bazą wiedzy ({str(e)})."
        total_latency = MetricsCalculator.calculate_latency_ms(total_start)

        # Create metrics only if enabled
        error_metrics = None
        if metrics_collector.is_enabled():
            error_metrics = MetricsCalculator.create_error_metrics(
                query=query,
                collection_name=collection_name,
                latency_ms=total_latency,
                strategy=strategy
            )
            metrics_collector.log_retrieval(error_metrics)

        return error_msg, error_metrics

    client = _qdrant_client
    embedder = _embeddings

    if not client or not embedder:
        error_msg = "Błąd techniczny: Narzędzie RAG nie jest poprawnie skonfigurowane."
        total_latency = MetricsCalculator.calculate_latency_ms(total_start)

        error_metrics = None
        if metrics_collector.is_enabled():
            error_metrics = MetricsCalculator.create_error_metrics(
                query=query,
                collection_name=collection_name,
                latency_ms=total_latency,
                strategy=strategy
            )
            metrics_collector.log_retrieval(error_metrics)

        return error_msg, error_metrics

    print(f"[RAG] Szukam: '{query}' w kolekcji '{collection_name}' "
          f"(strategia: {strategy})", file=sys.stderr)

    # ===== MAIN RETRIEVAL LOGIC =====
    try:
        # STEP 1: Generate the query vector (with time measurement)
        query_vector, embedding_latency = _measure_embedding_time(embedder, query)

        # STEP 2: Search in Qdrant (with time measurement)
        # The strategy actually used may differ from the requested one
        # (hybrid falls back to dense when the BM25 index is missing) --
        # the metrics must record the strategy that ran, not the request.
        search_response, search_latency, strategy_used = _measure_search_time(
            client, collection_name, query, query_vector, top_k, strategy
        )

        points = search_response.points

        # STEP 3: Handle empty results
        if not points:
            no_results_msg = "Nie znaleziono relewantnych dokumentów w bazie"
            total_latency = MetricsCalculator.calculate_latency_ms(total_start)

            empty_metrics = None
            if metrics_collector.is_enabled():
                empty_metrics = MetricsCalculator.create_retrieval_metrics(
                    query=query,
                    collection_name=collection_name,
                    points=None,
                    total_latency_ms=total_latency,
                    embedding_latency_ms=embedding_latency,
                    search_latency_ms=search_latency,
                    strategy=strategy_used
                )
                metrics_collector.log_retrieval(empty_metrics)

            return no_results_msg, empty_metrics

        # STEP 4: Format the results
        formatted_output = _format_search_results(points)

        # STEP 5: Create metrics (only if enabled)
        total_latency = MetricsCalculator.calculate_latency_ms(total_start)

        metrics = None
        if metrics_collector.is_enabled():
            metrics = MetricsCalculator.create_retrieval_metrics(
                query=query,
                collection_name=collection_name,
                points=points,
                total_latency_ms=total_latency,
                embedding_latency_ms=embedding_latency,
                search_latency_ms=search_latency,
                strategy=strategy_used
            )
            metrics_collector.log_retrieval(metrics)

        return formatted_output, metrics

    except Exception as e:
        err_msg = f"Błąd podczas przeszukiwania bazy wiedzy: {str(e)}"
        print(f"[RAG Error] {err_msg}", file=sys.stderr)

        total_latency = MetricsCalculator.calculate_latency_ms(total_start)

        error_metrics = None
        if metrics_collector.is_enabled():
            error_metrics = MetricsCalculator.create_error_metrics(
                query=query,
                collection_name=collection_name,
                latency_ms=total_latency,
                strategy=strategy
            )
            metrics_collector.log_retrieval(error_metrics)

        return err_msg, error_metrics


# ==============================================================================
# BACKWARD COMPATIBILITY: Old function without metrics
# ==============================================================================

def run_generic_rag(
    query: str,
    collection_name: str,
    top_k: int | None = None,
    strategy: str | None = None,
) -> str:
    """
    Original function without metrics (for backward compatibility)

    Internally uses run_generic_rag_with_metrics but returns only the result.
    Metrics are still collected in the background (if the metrics repository is available).
    """
    result, _ = run_generic_rag_with_metrics(
        query,
        collection_name,
        top_k=top_k,
        strategy=strategy,
    )
    return result
