from .models import (
    RetrievalMetrics,
    GenerationMetrics,
    FullRAGMetrics,
    MetricsStats
)

from .repository_interface import IMetricsRepository
from .repository_factory import MetricsRepositoryFactory

# Convenience functions
def get_repository(storage_type: str = None) -> IMetricsRepository:
    """Pobierz repository (singleton)"""
    return MetricsRepositoryFactory.get_singleton(storage_type)


def create_repository(storage_type: str = None, **kwargs) -> IMetricsRepository:
    """Utwórz nową instancję repository"""
    return MetricsRepositoryFactory.create(storage_type, **kwargs)


__all__ = [
    "RetrievalMetrics",
    "GenerationMetrics",
    "FullRAGMetrics",
    "MetricsStats",
    "IMetricsRepository",
    "MetricsRepositoryFactory",
    "get_repository",
    "create_repository",
]