from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from .models import (
    RetrievalMetrics,
    GenerationMetrics,
    FullRAGMetrics,
    ChunkingRunMetrics,
    MetricsStats
)


class IMetricsRepository(ABC):
    """
    Interface for all metrics storage implementations.

    Every database (PostgreSQL, MySQL, MongoDB, File, etc.)
    must implement all of these methods.
    """

    @abstractmethod
    def initialize_schema(self) -> bool:
        """
        Initialize the database schema (create tables/collections)

        Returns:
            bool: True on success, False on error
        """
        pass

    @abstractmethod
    def test_connection(self) -> bool:
        """
        Test the database connection

        Returns:
            bool: True if the connection works
        """
        pass

    @abstractmethod
    def insert_retrieval_metrics(self, metrics: RetrievalMetrics) -> Optional[int]:
        """
        Insert retrieval metrics

        Args:
            metrics: RetrievalMetrics object

        Returns:
            Optional[int]: ID of the inserted record or None
        """
        pass

    @abstractmethod
    def insert_generation_metrics(
            self,
            metrics: GenerationMetrics,
            retrieval_id: Optional[int] = None
    ) -> Optional[int]:
        """
        Insert generation metrics

        Args:
            metrics: GenerationMetrics object
            retrieval_id: ID of the related retrieval (optional)

        Returns:
            Optional[int]: ID of the inserted record or None
        """
        pass

    @abstractmethod
    def insert_full_metrics(
            self,
            metrics: FullRAGMetrics
    ) -> Optional[int]:
        """
        Insert full RAG pipeline metrics

        Args:
            metrics: FullRAGMetrics object

        Returns:
            Optional[int]: ID of the inserted record or None
        """
        pass

    @abstractmethod
    def get_retrieval_metrics(
            self,
            limit: int = 100,
            collection_name: Optional[str] = None,
            hours: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Get retrieval metrics

        Args:
            limit: Maximum number of records
            collection_name: Filter by collection (optional)
            hours: Get only the last N hours (optional)

        Returns:
            List[Dict]: List of metrics as dictionaries
        """
        pass

    @abstractmethod
    def get_aggregated_stats(
            self,
            hours: Optional[int] = 24,
            collection_name: Optional[str] = None
    ) -> MetricsStats:
        """
        Get aggregated statistics

        Args:
            hours: Time range in hours
            collection_name: Filter by collection (optional)

        Returns:
            MetricsStats: Object with the statistics
        """
        pass

    @abstractmethod
    def insert_chunking_metrics(self, metrics: ChunkingRunMetrics) -> Optional[int]:
        """
        Insert chunking metrics (experiments E1-E4)

        Args:
            metrics: ChunkingRunMetrics object

        Returns:
            Optional[int]: ID of the inserted record or None
        """
        pass

    @abstractmethod
    def get_chunking_metrics(
            self,
            limit: int = 100,
            experiment_id: Optional[str] = None,
            strategy: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        Get chunking metrics

        Args:
            limit: Maximum number of records
            experiment_id: Filter by experiment (optional)
            strategy: Filter by strategy (optional)

        Returns:
            List[Dict]: List of metrics as dictionaries
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """Close database connections"""
        pass