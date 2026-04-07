from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from .models import RetrievalMetrics, GenerationMetrics, FullRAGMetrics, MetricsStats


class IMetricsRepository(ABC):
    """
    Interfejs dla wszystkich implementacji storage metryk.

    Każda baza danych (PostgreSQL, MySQL, MongoDB, File, etc.)
    musi implementować wszystkie te metody.
    """

    @abstractmethod
    def initialize_schema(self) -> bool:
        """
        Inicjalizacja schematu bazy (tworzenie tabel/kolekcji)

        Returns:
            bool: True jeśli sukces, False w przypadku błędu
        """
        pass

    @abstractmethod
    def test_connection(self) -> bool:
        """
        Test połączenia z bazą

        Returns:
            bool: True jeśli połączenie działa
        """
        pass

    @abstractmethod
    def insert_retrieval_metrics(self, metrics: RetrievalMetrics) -> Optional[int]:
        """
        Wstaw metryki retrieval

        Args:
            metrics: Obiekt RetrievalMetrics

        Returns:
            Optional[int]: ID wstawionego rekordu lub None
        """
        pass

    @abstractmethod
    def insert_generation_metrics(
            self,
            metrics: GenerationMetrics,
            retrieval_id: Optional[int] = None
    ) -> Optional[int]:
        """
        Wstaw metryki generation

        Args:
            metrics: Obiekt GenerationMetrics
            retrieval_id: ID powiązanego retrieval (opcjonalne)

        Returns:
            Optional[int]: ID wstawionego rekordu lub None
        """
        pass

    @abstractmethod
    def insert_full_metrics(
            self,
            metrics: FullRAGMetrics
    ) -> Optional[int]:
        """
        Wstaw pełne metryki RAG pipeline

        Args:
            metrics: Obiekt FullRAGMetrics

        Returns:
            Optional[int]: ID wstawionego rekordu lub None
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
        Pobierz metryki retrieval

        Args:
            limit: Maksymalna liczba rekordów
            collection_name: Filtruj po kolekcji (opcjonalnie)
            hours: Pobierz tylko z ostatnich N godzin (opcjonalnie)

        Returns:
            List[Dict]: Lista metryk jako słowniki
        """
        pass

    @abstractmethod
    def get_aggregated_stats(
            self,
            hours: Optional[int] = 24,
            collection_name: Optional[str] = None
    ) -> MetricsStats:
        """
        Pobierz zagregowane statystyki

        Args:
            hours: Zakres czasowy w godzinach
            collection_name: Filtruj po kolekcji (opcjonalnie)

        Returns:
            MetricsStats: Obiekt ze statystykami
        """
        pass

    @abstractmethod
    def close(self) -> None:
        """Zamknij połączenia z bazą"""
        pass