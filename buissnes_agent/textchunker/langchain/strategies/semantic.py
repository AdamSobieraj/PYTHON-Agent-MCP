import logging
from typing import List
from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker

from buissnes_agent.EmbeddingClient import LocalEmbeddingClient
from buissnes_agent.textchunker.langchain.base import ChunkingStrategy

logger = logging.getLogger(__name__)

class SemanticStrategy(ChunkingStrategy):
    """
    ### Strategia 4: Semantic Chunking (Znaczeniowa / AI)

    Najbardziej zaawansowana metoda. Nie patrzy na znaki nowej linii czy nagłówki.
    Analizuje wektory (embeddingi) zdań.

    **Jak działa:**
    1. Zamienia zdania na liczby (wektory).
    2. Oblicza podobieństwo między sąsiednimi zdaniami.
    3. Jeśli podobieństwo spada poniżej progu (breakpoint threshold), uznaje to za zmianę tematu i robi cięcie.

    """

    def __init__(self):
        # Inicjalizacja klienta embeddingów.
        try:
            self.embeddings = LocalEmbeddingClient()
            logger.info("SemanticStrategy: Initialized EmbeddingClient successfully.")
        except Exception as e:
            logger.error(f"SemanticStrategy: Failed to initialize embeddings. Error: {e}")
            raise e

    def split_text(self, text: str) -> List[Document]:
        """
        Dzieli tekst na semantyczne fragmenty.
        """
        if not self.embeddings:
            raise ValueError("Embeddings not initialized. Check env vars.")

        text_splitter = SemanticChunker(
            self.embeddings,
            breakpoint_threshold_type="percentile",
            breakpoint_threshold_amount=95.0,  # Wysoki próg - tnie tylko przy wyraźnej zmianie tematu
            min_chunk_size=200  # Minimalna wielkość chunka (żeby nie tworzył "ogryzków")
        )

        try:
            # create_documents oczekuje listy tekstów, my mamy jeden duży tekst
            return text_splitter.create_documents([text])
        except Exception as e:
            logger.error(f"SemanticStrategy: Error during semantic split: {e}")
            # Fallback: W razie błędu semantycznego (np. serwer embeddingów padł),
            # można by tu rzucić wyjątek lub zwrócić tekst jako jeden chunk.
            raise e