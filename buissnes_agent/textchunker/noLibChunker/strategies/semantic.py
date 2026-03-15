import logging
from typing import List

from ..base import BaseNoLibStrategy

# Logger lokalny dla strategii
logger = logging.getLogger(__name__)


class SemanticStrategy(BaseNoLibStrategy):
    """
    ### Strategia 4: Semantic Chunker (LangChain Wrapper)

    To jedyna strategia w pakiecie NoLib, która faktycznie używa biblioteki (LangChain).
    Została tu umieszczona, aby zachować kompatybilność z oryginalnym kodem `NoLibChunker`.

    **Obsługa błędów:**
    Jeśli biblioteka `langchain_experimental` nie jest zainstalowana lub wystąpi błąd
    konfiguracji embeddingów, klasa zaloguje błąd i zwróci tekst jako jeden kawałek.
    """

    def __init__(self, chunk_size: int, chunk_overlap: int):
        super().__init__(chunk_size, chunk_overlap)
        self.splitter = None

        try:
            # Import warunkowy - tylko jeśli strategia jest używana
            from langchain_experimental.text_splitter import SemanticChunker

            # Musi on być dostępny w ścieżce projektu
            from buissnes_agent.embeddings.local_client import LocalEmbeddingClient

            # Inicjalizacja klienta (zaciąga URL i Key z .env automatycznie)
            embeddings = LocalEmbeddingClient()

            logger.info("SemanticStrategy: Używam EmbeddingClient (Bypass OpenAI API).")

            # Inicjalizacja splittera
            self.splitter = SemanticChunker(
                embeddings,
                breakpoint_threshold_type="percentile",
                # Opcjonalnie można dodać min_chunk_size, jeśli chunks są za małe
                # min_chunk_size=chunk_size // 4
            )

        except ImportError as e:
            logger.error(f"Brak wymaganych bibliotek dla SemanticStrategy: {e}")
            logger.warning("Zainstaluj: langchain_experimental oraz requests")
        except Exception as e:
            logger.error(f"Błąd inicjalizacji SemanticStrategy: {e}")

    def split_text(self, text: str) -> List[str]:
        if not self.splitter:
            logger.warning("Semantic splitter nie został zainicjowany (błąd w __init__). Zwracam tekst bez zmian.")
            return [text]

        try:
            # SemanticChunker zwraca obiekty Document
            docs = self.splitter.create_documents([text])

            # NoLibChunker oczekuje prostej listy stringów, więc mapujemy wynik
            return [doc.page_content for doc in docs]

        except Exception as e:
            logger.error(f"Błąd podczas dzielenia tekstu (Semantic): {e}")
            # Fallback w razie awarii API embeddingów
            return [text]