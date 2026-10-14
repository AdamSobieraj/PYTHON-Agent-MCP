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


def _measure_search_time(client, collection_name: str, query_vector: list, top_k: int):
    """
    Perform search with time measurement

    Returns:
        tuple: (search_response, search_latency_ms)
    """
    start_time = time.time()
    search_response = client.query_points(
        collection_name=collection_name,
        query=query_vector,
        limit=top_k,
        with_payload=True
    )
    latency_ms = MetricsCalculator.calculate_latency_ms(start_time)
    return search_response, latency_ms


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
) -> Tuple[str, Optional[RetrievalMetrics]]:
    """
    RAG with full retrieval metrics (if enabled in ENV)

    Args:
        query: User question
        collection_name: Collection name in Qdrant

    Returns:
        tuple: (formatted_output, retrieval_metrics)
               If the metrics repository is unavailable, metrics will be None
    """
    # Start timer for the whole process
    total_start = time.time()

    top_k = resolve_top_k(top_k)

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
                latency_ms=total_latency
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
                latency_ms=total_latency
            )
            metrics_collector.log_retrieval(error_metrics)

        return error_msg, error_metrics

    print(f"[RAG] Szukam: '{query}' w kolekcji '{collection_name}'", file=sys.stderr)

    # ===== MAIN RETRIEVAL LOGIC =====
    try:
        # STEP 1: Generate the query vector (with time measurement)
        query_vector, embedding_latency = _measure_embedding_time(embedder, query)

        # STEP 2: Search in Qdrant (with time measurement)
        search_response, search_latency = _measure_search_time(
            client, collection_name, query_vector, top_k
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
                    search_latency_ms=search_latency
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
                search_latency_ms=search_latency
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
                latency_ms=total_latency
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
    )
    return result
