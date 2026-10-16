import logging
import os
import time
from datetime import datetime
from typing import Optional, List

try:
    from buissnes_agent.metrics import (
        ChunkingRunMetrics,
        CostMetrics,
        FullRAGMetrics,
        GenerationMetrics,
        IMetricsRepository,
        RetrievalMetrics,
        get_repository,
    )
except ImportError:
    from metrics import (  # type: ignore
        ChunkingRunMetrics,
        CostMetrics,
        FullRAGMetrics,
        GenerationMetrics,
        IMetricsRepository,
        RetrievalMetrics,
        get_repository,
    )

logger = logging.getLogger(__name__)


# ==============================================================================
# METRIC CALCULATORS
# ==============================================================================
# Note: metrics are always active (no enabling flag).
# The only guard: as long as the metrics repository is available
# (e.g. Postgres is up) - see MetricsCollector.is_enabled().

class MetricsCalculator:
    """Class with methods that calculate metrics"""

    @staticmethod
    def calculate_avg_score(scores: List[float]) -> float:
        if not scores:
            return 0.0
        return sum(scores) / len(scores)

    @staticmethod
    def calculate_latency_ms(start_time: float) -> int:
        return int((time.time() - start_time) * 1000)

    @staticmethod
    def extract_top_scores(points) -> List[float]:
        return [point.score for point in points]

    @staticmethod
    def create_retrieval_metrics(
            query: str,
            collection_name: str,
            points,
            total_latency_ms: int,
            embedding_latency_ms: Optional[int] = None,
            search_latency_ms: Optional[int] = None
    ) -> RetrievalMetrics:
        """Factory method for RetrievalMetrics"""
        top_scores = MetricsCalculator.extract_top_scores(points) if points else []
        avg_score = MetricsCalculator.calculate_avg_score(top_scores)

        return RetrievalMetrics(
            query=query,
            collection_name=collection_name,
            num_results=len(points) if points else 0,
            top_scores=top_scores,
            avg_score=avg_score,
            latency_ms=total_latency_ms,
            embedding_latency_ms=embedding_latency_ms,
            search_latency_ms=search_latency_ms,
            timestamp=datetime.now().isoformat()
        )

    @staticmethod
    def create_error_metrics(
            query: str,
            collection_name: str,
            latency_ms: int
    ) -> RetrievalMetrics:
        """Factory method for error metrics"""
        return RetrievalMetrics(
            query=query,
            collection_name=collection_name,
            num_results=0,
            top_scores=[],
            avg_score=0.0,
            latency_ms=latency_ms,
            timestamp=datetime.now().isoformat()
        )


# ==============================================================================
# METRICS COLLECTOR (uses the interface)
# ==============================================================================

class MetricsCollector:
    """
    Singleton for collecting metrics.

    Uses IMetricsRepository - it doesn't know which concrete database it is!
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MetricsCollector, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Collector initialization (metrics are always active)"""
        self.repository: Optional[IMetricsRepository] = None

        try:
            # We use a factory - we don't know whether it's Postgres or File!
            self.repository = get_repository()
            logger.info("Metrics collector zainicjalizowany")
        except Exception as e:
            logger.error(f"Nie można zainicjalizować repository: {e}")

    def is_enabled(self) -> bool:
        """Metrics are always active - enabled as long as the repository is available"""
        return self.repository is not None

    def log_retrieval(self, metrics: RetrievalMetrics) -> None:
        """Save retrieval metrics (via the interface!)"""
        if not self.is_enabled():
            return

        try:
            record_id = self.repository.insert_retrieval_metrics(metrics)

            if record_id:
                logger.info(
                    f"[Retrieval Metrics] "
                    f"Query: '{metrics.query[:50]}...', "
                    f"Results: {metrics.num_results}, "
                    f"Avg Score: {metrics.avg_score:.3f}, "
                    f"Latency: {metrics.latency_ms}ms"
                )
            else:
                logger.warning("Nie udało się zapisać metryk retrieval")

        except Exception as e:
            logger.error(f"Błąd zapisu metryk: {e}")

    def log_generation(self, metrics: GenerationMetrics,
                       retrieval_id: Optional[int] = None) -> Optional[int]:
        """
        Save generation metrics (via the interface!).
        retrieval_id: optional link to the retrieval row (Stack B).
        Returns the id of the saved row (None on failure).
        """
        if not self.is_enabled():
            return None

        try:
            record_id = self.repository.insert_generation_metrics(metrics, retrieval_id)

            if record_id:
                logger.info(
                    f"[Generation Metrics] "
                    f"Query: '{metrics.query[:50]}...', "
                    f"Latency: {metrics.latency_ms}ms"
                )
            else:
                logger.warning("Nie udało się zapisać metryk generation")

            return record_id

        except Exception as e:
            logger.error(f"Błąd zapisu metryk generation: {e}")
            return None

    def log_full_rag(self, metrics: FullRAGMetrics) -> None:
        """Save full RAG metrics (via the interface!)"""
        if not self.is_enabled():
            return

        try:
            record_id = self.repository.insert_full_metrics(metrics)

            if record_id:
                logger.info(
                    f"[Full RAG Metrics] "
                    f"Total Latency: {metrics.total_latency_ms}ms"
                )
            else:
                logger.warning("Nie udało się zapisać full metrics")

        except Exception as e:
            logger.error(f"Błąd zapisu full metrics: {e}")

    def log_chunking(self, metrics: ChunkingRunMetrics) -> None:
        """Save chunking metrics (via the interface!)"""
        if not self.is_enabled():
            return

        try:
            record_id = self.repository.insert_chunking_metrics(metrics)

            if record_id:
                logger.info(
                    f"[Chunking Metrics] "
                    f"Exp: {metrics.experiment_id}, "
                    f"Strategy: {metrics.strategy}, "
                    f"Source: {metrics.source}, "
                    f"Chunks: {metrics.num_chunks}, "
                    f"Total: {metrics.total_ms}ms"
                )
            else:
                logger.warning("Nie udało się zapisać metryk chunkingu")

        except Exception as e:
            logger.error(f"Błąd zapisu metryk chunkingu: {e}")

    def close(self):
        """Close connections"""
        if self.repository:
            self.repository.close()


# Singleton instance
metrics_collector = MetricsCollector()


# ==============================================================================
# FULL METRICS FOR A RAG TURN (shared helper for Stacks A and B)
# ==============================================================================
def log_full_rag_for_turn(query: str,
                          answer: str,
                          context_chars: Optional[int],
                          total_latency_ms: Optional[int]) -> None:
    """
    Complete saving of the RAG turn's metrics (shared by Stacks A and B):
    1. finds the freshest retrieval row for the same query
       (saved by the MCP server in tool_iso_rag),
    2. saves generation - with a retrieval_id link if the row exists,
    3. if a retrieval row exists: inserts rag_full_metrics with links to both.

    No retrieval row (question without the DB) => generation only, no full.
    Best-effort: silently skipped if the repository is missing, never breaks the app.
    """
    if not metrics_collector.is_enabled():
        return

    try:
        row = None
        try:
            # NOTE: the query in the retrieval row is the AGENT's query (the LLM
            # rewrites it for the tool), not the user's literal question -
            # so matching by text rarely hit. Instead:
            # the freshest retrieval row from a 5-minute window (the turn ended
            # just now) + a fallback to exact matching.
            rows = metrics_collector.repository.get_retrieval_metrics(limit=20)
            now = datetime.now()
            row = next(
                (r for r in rows
                 if r.get("query") == query
                 or (isinstance(r.get("timestamp"), datetime)
                     and (now - r["timestamp"]).total_seconds() < 300)),
                None
            )
        except Exception as e:
            logger.debug("Odczyt retrieval metrics nieudany: %s", e)

        retrieval_id = row.get("id") if row else None

        # 2) generation (with a retrieval link, if one exists)
        generation = GenerationMetrics(
            query=query,
            answer=answer,
            context_length=context_chars,
            latency_ms=total_latency_ms,
            timestamp=datetime.now().isoformat(),
        )
        generation_id = metrics_collector.log_generation(generation, retrieval_id)

        # 3) full metrics - only if the turn queried the database
        if row is None:
            logger.debug(
                "Brak wiersza retrieval dla zapytania '%s' - pomijam full metrics",
                query
            )
            return

        from dataclasses import fields

        valid = {f.name for f in fields(RetrievalMetrics)}
        retrieval = RetrievalMetrics(
            **{k: v for k, v in row.items() if k in valid}
        )

        full = FullRAGMetrics(
            retrieval=retrieval,
            retrieval_id=retrieval_id,
            generation=generation,
            generation_id=generation_id,
            total_latency_ms=total_latency_ms,
        )
        metrics_collector.log_full_rag(full)

    except Exception as e:
        logger.error(f"Błąd zapisu metryk tury RAG: {e}")


# ==============================================================================
# COST USAGE (token usage + cost per model/section -> rag_cost_metrics)
# ==============================================================================
#
# Prices are read from the COST section in .env (USD per 1M tokens):
#     COST_INPUT_PER_MTOKEN / COST_OUTPUT_PER_MTOKEN
#
# Sections:
#     embedding          - LocalEmbeddingClient (input tokens only)
#     chunking_agentic   - LLM calls in NewAgenticStrategy
#     agent_generation   - final answer generation (AnalysisAgent)


def _price_from_env(name: str) -> float:
    """Read a price (USD per 1M tokens) from the COST section in .env."""
    try:
        return float(os.getenv(name, "0.0"))
    except (TypeError, ValueError):
        return 0.0


def estimate_tokens(text: str) -> int:
    """
    Rough token estimate (chars/4) for use when the provider does not
    report usage. Industry-standard heuristic - good enough for costing.
    """
    if not text:
        return 0
    return max(1, len(text) // 4)


def log_cost_usage(
    model: str,
    section: str,
    input_tokens: int = 0,
    output_tokens: int = 0,
    provider: Optional[str] = None,
    metadata: Optional[dict] = None,
    estimated: bool = False,
) -> None:
    """
    Log token usage + cost for one model usage in one system section.

    Costs (USD) are ALWAYS computed from the COST section in .env
    (COST_INPUT_PER_MTOKEN / COST_OUTPUT_PER_MTOKEN) - also when the
    token counts are estimated (estimated=True, stored in metadata).
    Never raises - metrics must not break the pipeline.
    Rows land in the rag_cost_metrics table.
    """
    try:
        input_tokens = int(input_tokens or 0)
        output_tokens = int(output_tokens or 0)
        if input_tokens <= 0 and output_tokens <= 0:
            return  # nothing to measure and nothing to estimate

        if estimated:
            metadata = dict(metadata or {})
            metadata["estimated"] = True

        cost_in = round(input_tokens / 1_000_000.0 * _price_from_env("COST_INPUT_PER_MTOKEN"), 8)
        cost_out = round(output_tokens / 1_000_000.0 * _price_from_env("COST_OUTPUT_PER_MTOKEN"), 8)

        metrics = CostMetrics(
            model=model or "unknown",
            section=section,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            total_tokens=input_tokens + output_tokens,
            cost_input=cost_in,
            cost_output=cost_out,
            cost_total=round(cost_in + cost_out, 8),
            provider=provider,
            metadata=metadata,
        )
        repo = get_repository()
        repo.insert_cost_metrics(metrics)
        logger.debug(
            "Cost usage zapisane: section=%s model=%s tokens=%d/%d estimated=%s",
            section, model, input_tokens, output_tokens, estimated,
        )
    except Exception as e:
        logger.warning(f"Zapis cost usage nie powiodl sie (non-fatal): {e}")
