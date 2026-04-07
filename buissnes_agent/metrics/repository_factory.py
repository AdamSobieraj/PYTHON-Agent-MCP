import os
import logging
from typing import Optional

from .repository_interface import IMetricsRepository
from .repository_postgres import PostgresMetricsRepository
from .repository_file import FileMetricsRepository

logger = logging.getLogger(__name__)


class MetricsRepositoryFactory:
    """
    Factory do tworzenia odpowiedniego repository na podstawie ENV.

    Wspierane typy:
    - postgres: PostgreSQL
    - file: JSONL file storage
    - (możliwość rozszerzenia: mysql, mongodb, redis, etc.)
    """

    _instance: Optional[IMetricsRepository] = None

    @classmethod
    def create(
            cls,
            storage_type: Optional[str] = None,
            **kwargs
    ) -> IMetricsRepository:
        """
        Utwórz repository na podstawie typu storage

        Args:
            storage_type: Typ storage ("postgres", "file") lub None (z ENV)
            **kwargs: Dodatkowe parametry (np. file_path dla file storage)

        Returns:
            IMetricsRepository: Instancja odpowiedniego repository

        Raises:
            ValueError: Gdy typ storage jest nieznany
        """
        if storage_type is None:
            storage_type = os.getenv("METRICS_STORAGE_TYPE", "file").lower()

        logger.info(f"Tworzenie metrics repository: type={storage_type}")

        if storage_type == "postgres":
            return PostgresMetricsRepository()

        elif storage_type == "file":
            file_path = kwargs.get("file_path") or os.getenv(
                "RAG_METRICS_FILE",
                "rag_metrics.jsonl"
            )
            return FileMetricsRepository(file_path)

        else:
            raise ValueError(
                f"Nieznany typ storage: {storage_type}. "
                f"Wspierane: postgres, file"
            )

    @classmethod
    def get_singleton(cls, storage_type: Optional[str] = None) -> IMetricsRepository:
        """
        Pobierz singleton instance repository

        Przy pierwszym wywołaniu tworzy instancję, później zwraca tę samą.
        """
        if cls._instance is None:
            cls._instance = cls.create(storage_type)
        return cls._instance

    @classmethod
    def reset_singleton(cls):
        """Wymuś reset singletona (przydatne w testach)"""
        if cls._instance:
            cls._instance.close()
        cls._instance = None