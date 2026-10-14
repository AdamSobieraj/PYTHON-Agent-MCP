from .models import (
    RetrievalMetrics,
    GenerationMetrics,
    FullRAGMetrics,
    ChunkingRunMetrics,
    MetricsStats
)

from .repository_interface import IMetricsRepository
from .repository_factory import MetricsRepositoryFactory

# Convenience functions
def get_repository(storage_type: str = None) -> IMetricsRepository:
    """Get the repository (singleton)"""
    return MetricsRepositoryFactory.get_singleton(storage_type)


def create_repository(storage_type: str = None, **kwargs) -> IMetricsRepository:
    """Create a new repository instance"""
    return MetricsRepositoryFactory.create(storage_type, **kwargs)


__all__ = [
    "RetrievalMetrics",
    "GenerationMetrics",
    "FullRAGMetrics",
    "ChunkingRunMetrics",
    "MetricsStats",
    "IMetricsRepository",
    "MetricsRepositoryFactory",
    "get_repository",
    "create_repository",
]