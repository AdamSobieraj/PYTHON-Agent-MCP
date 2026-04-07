# tools/rag_metrics.py

import time
import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime
from typing import List, Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)


# ==============================================================================
# KONFIGURACJA Z ENV
# ==============================================================================

def _get_metrics_enabled() -> bool:
    """Sprawdź czy metryki są włączone w .env"""
    enabled = os.getenv("ENABLE_RAG_METRICS", "false").lower()
    return enabled in ("true", "1", "yes", "on")


def _get_storage_type() -> str:
    """Pobierz typ storage: postgres lub file"""
    return os.getenv("METRICS_STORAGE_TYPE", "file").lower()


def _get_metrics_file() -> str:
    """Pobierz ścieżkę do pliku metryk (fallback)"""
    return os.getenv("RAG_METRICS_FILE", "rag_metrics.jsonl")


def _get_fallback_enabled() -> bool:
    """Czy włączony fallback do pliku gdy PostgreSQL niedostępny"""
    enabled = os.getenv("METRICS_FALLBACK_TO_FILE", "true").lower()
    return enabled in ("true", "1", "yes", "on")


METRICS_ENABLED = _get_metrics_enabled()
STORAGE_TYPE = _get_storage_type()
METRICS_FILE = _get_metrics_file()
FALLBACK_ENABLED = _get_fallback_enabled()


# ==============================================================================
# DATACLASSES DLA METRYK
# ==============================================================================

@dataclass
class RetrievalMetrics:
    """Metryki dla fazy retrieval"""
    query: str
    collection_name: str
    num_results: int
    top_scores: List[float]
    avg_score: float
    latency_ms: int
    timestamp: str
    embedding_latency_ms: Optional[int] = None
    search_latency_ms: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class GenerationMetrics:
    """Metryki dla fazy generation (gdy używasz LLM)"""
    query: str
    answer: str
    context_length: int
    tokens_used: Optional[int] = None
    latency_ms: Optional[int] = None
    cost: Optional[float] = None
    timestamp: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


@dataclass
class FullRAGMetrics:
    """Metryki dla całego pipeline RAG"""
    retrieval: RetrievalMetrics
    generation: Optional[GenerationMetrics] = None
    total_latency_ms: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "retrieval": self.retrieval.to_dict(),
            "generation": self.generation.to_dict() if self.generation else None,
            "total_latency_ms": self.total_latency_ms
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())


# ==============================================================================
# KALKULATORY METRYK (wydzielone metody)
# ==============================================================================

class MetricsCalculator:
    """Klasa z metodami obliczającymi metryki"""

    @staticmethod
    def calculate_avg_score(scores: List[float]) -> float:
        """Oblicz średni score z listy"""
        if not scores:
            return 0.0
        return sum(scores) / len(scores)

    @staticmethod
    def calculate_latency_ms(start_time: float) -> int:
        """Oblicz latency w ms od start_time"""
        return int((time.time() - start_time) * 1000)

    @staticmethod
    def extract_top_scores(points) -> List[float]:
        """Ekstraktuj score z Qdrant points"""
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
# METRICS STORAGE BACKENDS
# ==============================================================================

class MetricsStorageBackend:
    """Interfejs dla różnych backendów storage"""

    def save_retrieval(self, metrics: RetrievalMetrics) -> bool:
        """Zapisz metryki retrieval"""
        raise NotImplementedError

    def save_full_rag(self, metrics: FullRAGMetrics) -> bool:
        """Zapisz pełne metryki RAG"""
        raise NotImplementedError


class FileStorageBackend(MetricsStorageBackend):
    """Backend zapisujący do pliku JSONL"""

    def __init__(self, file_path: str):
        self.file_path = file_path

    def save_retrieval(self, metrics: RetrievalMetrics) -> bool:
        """Zapisz do pliku JSONL"""
        try:
            with open(self.file_path, "a", encoding="utf-8") as f:
                f.write(metrics.to_json() + "\n")
            return True
        except Exception as e:
            logger.error(f"Błąd zapisu do pliku {self.file_path}: {e}")
            return False

    def save_full_rag(self, metrics: FullRAGMetrics) -> bool:
        """Zapisz pełne metryki do pliku"""
        try:
            with open(self.file_path, "a", encoding="utf-8") as f:
                f.write(metrics.to_json() + "\n")
            return True
        except Exception as e:
            logger.error(f"Błąd zapisu do pliku {self.file_path}: {e}")
            return False


class PostgresStorageBackend(MetricsStorageBackend):
    """Backend zapisujący do PostgreSQL"""

    def __init__(self):
        self._repository = None
        self._init_repository()

    def _init_repository(self):
        """Lazy initialization repository"""
        if self._repository is None:
            try:
                from ..metrics_db import MetricsRepository
                self._repository = MetricsRepository()
                logger.info("PostgreSQL metrics backend zainicjalizowany")
            except Exception as e:
                logger.error(f"Błąd inicjalizacji PostgreSQL backend: {e}")
                raise

    def save_retrieval(self, metrics: RetrievalMetrics) -> bool:
        """Zapisz do PostgreSQL"""
        try:
            record_id = self._repository.insert_retrieval_metrics(metrics.to_dict())
            return record_id is not None
        except Exception as e:
            logger.error(f"Błąd zapisu do PostgreSQL: {e}")
            return False

    def save_full_rag(self, metrics: FullRAGMetrics) -> bool:
        """Zapisz pełne metryki"""
        try:
            # Najpierw retrieval
            retrieval_id = self._repository.insert_retrieval_metrics(
                metrics.retrieval.to_dict()
            )

            if not retrieval_id:
                return False

            # Potem generation (jeśli istnieje)
            generation_id = None
            if metrics.generation:
                generation_id = self._repository.insert_generation_metrics(
                    metrics.generation.to_dict(),
                    retrieval_id
                )

            # Na koniec full metrics
            full_id = self._repository.insert_full_metrics(
                retrieval_id,
                generation_id,
                metrics.total_latency_ms
            )

            return full_id is not None

        except Exception as e:
            logger.error(f"Błąd zapisu full metrics do PostgreSQL: {e}")
            return False


# ==============================================================================
# METRICS COLLECTOR
# ==============================================================================

class MetricsCollector:
    """Singleton do zbierania i zapisywania metryk"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MetricsCollector, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        """Inicjalizacja collectora"""
        self.enabled = METRICS_ENABLED
        self.storage_type = STORAGE_TYPE
        self.fallback_enabled = FALLBACK_ENABLED

        # Wybór głównego backend
        self.primary_backend = self._create_backend(self.storage_type)

        # Fallback backend (zawsze file)
        self.fallback_backend = None
        if self.fallback_enabled and self.storage_type != "file":
            self.fallback_backend = FileStorageBackend(METRICS_FILE)
            logger.info(f"Fallback backend (file) skonfigurowany: {METRICS_FILE}")

    def _create_backend(self, storage_type: str) -> Optional[MetricsStorageBackend]:
        """Factory method dla storage backend"""
        if storage_type == "postgres":
            try:
                backend = PostgresStorageBackend()
                logger.info("Primary backend: PostgreSQL")
                return backend
            except Exception as e:
                logger.error(f"Nie można utworzyć PostgreSQL backend: {e}")
                if self.fallback_enabled:
                    logger.warning("Fallback do file storage")
                    return FileStorageBackend(METRICS_FILE)
                return None

        elif storage_type == "file":
            logger.info(f"Primary backend: File ({METRICS_FILE})")
            return FileStorageBackend(METRICS_FILE)

        else:
            logger.error(f"Nieznany typ storage: {storage_type}")
            return None

    def is_enabled(self) -> bool:
        """Sprawdź czy zbieranie metryk jest włączone"""
        return self.enabled

    def log_retrieval(self, metrics: RetrievalMetrics) -> None:
        """Zapisz metryki retrieval"""
        if not self.enabled:
            return

        # Próba zapisu do primary backend
        success = False
        if self.primary_backend:
            success = self.primary_backend.save_retrieval(metrics)

        # Fallback jeśli primary zawiódł
        if not success and self.fallback_backend:
            logger.warning("Primary backend failed, using fallback")
            self.fallback_backend.save_retrieval(metrics)

        # Log do konsoli
        logger.info(
            f"[Retrieval Metrics] "
            f"Query: '{metrics.query[:50]}...', "
            f"Results: {metrics.num_results}, "
            f"Avg Score: {metrics.avg_score:.3f}, "
            f"Latency: {metrics.latency_ms}ms"
        )

    def log_full_rag(self, metrics: FullRAGMetrics) -> None:
        """Zapisz pełne metryki RAG"""
        if not self.enabled:
            return

        # Próba zapisu do primary backend
        success = False
        if self.primary_backend:
            success = self.primary_backend.save_full_rag(metrics)

        # Fallback jeśli primary zawiódł
        if not success and self.fallback_backend:
            logger.warning("Primary backend failed, using fallback")
            self.fallback_backend.save_full_rag(metrics)

        # Log do konsoli
        logger.info(
            f"[Full RAG Metrics] "
            f"Total Latency: {metrics.total_latency_ms}ms"
        )


# Singleton instance
metrics_collector = MetricsCollector()