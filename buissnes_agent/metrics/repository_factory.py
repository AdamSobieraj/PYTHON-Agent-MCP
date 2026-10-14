import os
import logging
from importlib import import_module
from typing import Optional

from .repository_interface import IMetricsRepository
from .repository_file import FileMetricsRepository

logger = logging.getLogger(__name__)


class MetricsRepositoryFactory:
    """
    Factory for creating the appropriate repository based on ENV.

    Supported types:
    - postgres: PostgreSQL
    - file: JSONL file storage
    - (extensible: mysql, mongodb, redis, etc.)
    """

    _instance: Optional[IMetricsRepository] = None

    @staticmethod
    def _load_postgres_repository_class():
        try:
            module = import_module("buissnes_agent.metrics.repository_postgres")
        except ImportError:
            module = import_module(".repository_postgres", package=__package__)
        return module.PostgresMetricsRepository

    @classmethod
    def create(
            cls,
            storage_type: Optional[str] = None,
            **kwargs
    ) -> IMetricsRepository:
        """
        Create a repository based on the storage type

        Args:
            storage_type: Storage type ("postgres", "file") or None (from ENV)
            **kwargs: Additional parameters (e.g. file_path for file storage)

        Returns:
            IMetricsRepository: Instance of the appropriate repository

        Raises:
            ValueError: If the storage type is unknown
        """
        if storage_type is None:
            storage_type = os.getenv("METRICS_STORAGE_TYPE", "file").lower()

        logger.info(f"Tworzenie metrics repository: type={storage_type}")

        if storage_type == "postgres":
            postgres_repository_class = cls._load_postgres_repository_class()
            return postgres_repository_class()

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
        Get the singleton repository instance

        On the first call it creates the instance, later calls return the same one.
        """
        if cls._instance is None:
            cls._instance = cls.create(storage_type)
        return cls._instance

    @classmethod
    def reset_singleton(cls):
        """Force a singleton reset (useful in tests)"""
        if cls._instance:
            cls._instance.close()
        cls._instance = None
