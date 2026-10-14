import json
import logging
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
from pathlib import Path

from .repository_interface import IMetricsRepository
from .models import (
    RetrievalMetrics,
    GenerationMetrics,
    FullRAGMetrics,
    ChunkingRunMetrics,
    MetricsStats
)

logger = logging.getLogger(__name__)


class FileMetricsRepository(IMetricsRepository):
    """Repository implementation for a JSONL file"""

    def __init__(self, file_path: str = "rag_metrics.jsonl"):
        self.file_path = Path(file_path)
        self._ensure_file_exists()

    def _ensure_file_exists(self):
        """Ensure the file exists"""
        if not self.file_path.exists():
            self.file_path.touch()
            logger.info(f"Utworzono plik metryk: {self.file_path}")

    def initialize_schema(self) -> bool:
        """Implementation: a file has no schema"""
        self._ensure_file_exists()
        return True

    def test_connection(self) -> bool:
        """Implementation: check whether we can write to the file"""
        try:
            self._ensure_file_exists()
            return self.file_path.exists() and self.file_path.is_file()
        except Exception as e:
            logger.error(f"Test file connection failed: {e}")
            return False

    def insert_retrieval_metrics(self, metrics: RetrievalMetrics) -> Optional[int]:
        """Implementation: append to the JSONL file"""
        try:
            with open(self.file_path, "a", encoding="utf-8") as f:
                f.write(metrics.to_json() + "\n")
            # For a file, we return the timestamp as the "ID"
            return int(datetime.now().timestamp() * 1000)
        except Exception as e:
            logger.error(f"Błąd zapisu do pliku: {e}")
            return None

    def insert_generation_metrics(
            self,
            metrics: GenerationMetrics,
            retrieval_id: Optional[int] = None
    ) -> Optional[int]:
        """Implementation: append generation metrics"""
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
        """Implementation: append full metrics"""
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
        """Implementation: read from the file with filtering"""
        metrics = []

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        data = json.loads(line)

                        # Filter by collection_name
                        if collection_name and data.get("collection_name") != collection_name:
                            continue

                        # Filter by time
                        if hours:
                            timestamp = datetime.fromisoformat(data.get("timestamp", ""))
                            cutoff = datetime.now() - timedelta(hours=hours)
                            if timestamp < cutoff:
                                continue

                        metrics.append(data)

            # Sort by timestamp (DESC) and limit
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
        """Implementation: compute statistics from the file"""
        metrics = self.get_retrieval_metrics(
            limit=10000,  # Get all
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

        # Compute statistics
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

    def insert_chunking_metrics(self, metrics: ChunkingRunMetrics) -> Optional[int]:
        """Implementation: append chunking metrics to the JSONL file"""
        try:
            with open(self.file_path, "a", encoding="utf-8") as f:
                f.write(metrics.to_json() + "\n")
            return int(datetime.now().timestamp() * 1000)
        except Exception as e:
            logger.error(f"Błąd zapisu metryk chunking: {e}")
            return None

    def get_chunking_metrics(
            self,
            limit: int = 100,
            experiment_id: Optional[str] = None,
            strategy: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Implementation: read chunking metrics with filtering"""
        records: List[Dict[str, Any]] = []
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    data = json.loads(line)
                    # File shared with other metric types -
                    # fetch only chunking records
                    if "experiment_id" not in data:
                        continue
                    if experiment_id and data.get("experiment_id") != experiment_id:
                        continue
                    if strategy and data.get("strategy") != strategy:
                        continue
                    records.append(data)
        except FileNotFoundError:
            logger.warning(f"Plik metryk nie istnieje: {self.file_path}")
            return []
        except Exception as e:
            logger.error(f"Błąd odczytu metryk chunking: {e}")
            return []

        records.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
        return records[:limit]

    def close(self) -> None:
        """Implementation: nothing to close for a file"""
        pass