import json
import logging
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
from pathlib import Path

from .repository_interface import IMetricsRepository
from .models import RetrievalMetrics, GenerationMetrics, FullRAGMetrics, MetricsStats

logger = logging.getLogger(__name__)


class FileMetricsRepository(IMetricsRepository):
    """Implementacja repository dla pliku JSONL"""

    def __init__(self, file_path: str = "rag_metrics.jsonl"):
        self.file_path = Path(file_path)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Upewnij się, że plik istnieje"""
        if not self.file_path.exists():
            self.file_path.touch()
            logger.info(f"Utworzono plik metryk: {self.file_path}")

    def initialize_schema(self) -> bool:
        """Implementacja: dla pliku nie ma schematu"""
        self._ensure_file_exists()
        return True

    def test_connection(self) -> bool:
        """Implementacja: sprawdź czy możemy pisać do pliku"""
        try:
            self._ensure_file_exists()
            return self.file_path.exists() and self.file_path.is_file()
        except Exception as e:
            logger.error(f"Test file connection failed: {e}")
            return False

    def insert_retrieval_metrics(self, metrics: RetrievalMetrics) -> Optional[int]:
        """Implementacja: dopisz do pliku JSONL"""
        try:
            with open(self.file_path, "a", encoding="utf-8") as f:
                f.write(metrics.to_json() + "\n")
            # Dla pliku zwracamy timestamp jako "ID"
            return int(datetime.now().timestamp() * 1000)
        except Exception as e:
            logger.error(f"Błąd zapisu do pliku: {e}")
            return None

    def insert_generation_metrics(
            self,
            metrics: GenerationMetrics,
            retrieval_id: Optional[int] = None
    ) -> Optional[int]:
        """Implementacja: dopisz generation metrics"""
        try:
            data = {
                **metrics.to_dict(),
                "retrieval_id": retrieval_id
            }
            with open(self.file_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(data) + "\n")
            return int(datetime.now().timestamp() * 1000)
        except Exception as e:
            logger.error(f"Błąd zapisu generation metrics: {e}")
            return None

    def insert_full_metrics(self, metrics: FullRAGMetrics) -> Optional[int]:
        """Implementacja: dopisz pełne metryki"""
        try:
            with open(self.file_path, "a", encoding="utf-8") as f:
                f.write(metrics.to_json() + "\n")
            return int(datetime.now().timestamp() * 1000)
        except Exception as e:
            logger.error(f"Błąd zapisu full metrics: {e}")
            return None

    def get_retrieval_metrics(
            self,
            limit: int = 100,
            collection_name: Optional[str] = None,
            hours: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """Implementacja: odczyt z pliku z filtrowaniem"""
        metrics = []

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        data = json.loads(line)

                        # Filtruj po collection_name
                        if collection_name and data.get("collection_name") != collection_name:
                            continue

                        # Filtruj po czasie
                        if hours:
                            timestamp = datetime.fromisoformat(data.get("timestamp", ""))
                            cutoff = datetime.now() - timedelta(hours=hours)
                            if timestamp < cutoff:
                                continue

                        metrics.append(data)

            # Sortuj po timestamp (DESC) i ogranicz
            metrics.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
            return metrics[:limit]

        except FileNotFoundError:
            logger.warning(f"Plik metryk nie istnieje: {self.file_path}")
            return []
        except Exception as e:
            logger.error(f"Błąd odczytu metryk: {e}")
            return []

    def get_aggregated_stats(
            self,
            hours: Optional[int] = 24,
            collection_name: Optional[str] = None
    ) -> MetricsStats:
        """Implementacja: oblicz statystyki z pliku"""
        metrics = self.get_retrieval_metrics(
            limit=10000,  # Pobierz wszystkie
            collection_name=collection_name,
            hours=hours
        )

        if not metrics:
            return MetricsStats(
                total_queries=0,
                avg_latency_ms=0,
                p50_latency_ms=0,
                p95_latency_ms=0,
                p99_latency_ms=0,
                avg_score=0,
                avg_results=0,
                queries_no_results=0
            )

        # Oblicz statystyki
        latencies = sorted([m['latency_ms'] for m in metrics])
        scores = [m['avg_score'] for m in metrics]
        results = [m['num_results'] for m in metrics]

        def percentile(data, p):
            k = (len(data) - 1) * p
            f = int(k)
            c = int(k) + 1
            if f == c:
                return data[f]
            return data[f] * (c - k) + data[c] * (k - f)

        return MetricsStats(
            total_queries=len(metrics),
            avg_latency_ms=sum(latencies) / len(latencies),
            p50_latency_ms=percentile(latencies, 0.5),
            p95_latency_ms=percentile(latencies, 0.95),
            p99_latency_ms=percentile(latencies, 0.99),
            avg_score=sum(scores) / len(scores),
            avg_results=sum(results) / len(results),
            queries_no_results=sum(1 for r in results if r == 0)
        )

    def close(self) -> None:
        """Implementacja: dla pliku nie ma co zamykać"""
        pass