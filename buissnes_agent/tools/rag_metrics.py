import logging
import os
import time
from datetime import datetime
from typing import Optional, List

try:
    from buissnes_agent.metrics import (
        FullRAGMetrics,
        IMetricsRepository,
        RetrievalMetrics,
        get_repository,
    )
except ImportError:
    from metrics import (  # type: ignore
        FullRAGMetrics,
        IMetricsRepository,
        RetrievalMetrics,
        get_repository,
    )

logger = logging.getLogger(__name__)


# ==============================================================================
# KONFIGURACJA
# ==============================================================================

def _get_metrics_enabled() -> bool:
    """Sprawdź czy metryki są włączone"""
    enabled = os.getenv("ENABLE_RAG_METRICS", "false").lower()
    return enabled in ("true", "1", "yes", "on")


METRICS_ENABLED = _get_metrics_enabled()


# ==============================================================================
# KALKULATORY METRYK
# ==============================================================================

class MetricsCalculator:
    """Klasa z metodami obliczającymi metryki"""

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
        """Factory method dla RetrievalMetrics"""
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
        """Factory method dla metryk błędu"""
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
# METRICS COLLECTOR (używa interfejsu)
# ==============================================================================

class MetricsCollector:
    """
    Singleton do zbierania metryk.

    Używa IMetricsRepository - nie wie jaka to konkretna baza!
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MetricsCollector, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Inicjalizacja collectora"""
        self.enabled = METRICS_ENABLED
        self.repository: Optional[IMetricsRepository] = None

        if self.enabled:
            try:
                # Używamy factory - nie wiemy czy to Postgres czy File!
                self.repository = get_repository()
                logger.info("Metrics collector zainicjalizowany")
            except Exception as e:
                logger.error(f"Nie można zainicjalizować repository: {e}")
                self.enabled = False

    def is_enabled(self) -> bool:
        """Sprawdź czy zbieranie metryk jest włączone"""
        return self.enabled and self.repository is not None

    def log_retrieval(self, metrics: RetrievalMetrics) -> None:
        """Zapisz metryki retrieval (przez interfejs!)"""
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

    def log_full_rag(self, metrics: FullRAGMetrics) -> None:
        """Zapisz pełne metryki RAG (przez interfejs!)"""
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

    def close(self):
        """Zamknij połączenia"""
        if self.repository:
            self.repository.close()


# Singleton instance
metrics_collector = MetricsCollector()
