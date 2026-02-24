import os
import logging
import requests
import numpy as np
from typing import List, Any
from langchain_core.embeddings import Embeddings

logger = logging.getLogger(__name__)

class LocalEmbeddingClient(Embeddings):
    """
    Klient Embeddingów dla serwerów (LM Studio, LocalAI, Ollama),
    który omija restrykcyjne walidacje biblioteki `langchain_openai`.

    Wysyła surowe zapytania HTTP, obsługując specyficzne błędy formatowania JSON (błąd 400).
    """

    def __init__(self,
                 base_url: str = None,
                 api_key: str = None,
                 model: str = None,
                 dimensions: int = None):

        # Pobieranie konfiguracji z argumentów lub zmiennych środowiskowych (.env)
        self.base_url = base_url or os.getenv("EMBEDDING_BASE_URL")
        self.api_key = api_key or os.getenv("EMBEDDING_API_KEY")
        self.model = model or os.getenv("EMBEDDING_MODEL")
        self.dimensions = int(dimensions or os.getenv("EMBEDDING_DIM"))

        # Normalizacja URL - upewniamy się, że kończy się na /embeddings
        if self.base_url.endswith("/"):
            self.endpoint_url = f"{self.base_url}embeddings"
        elif self.base_url.endswith("embeddings"):
            self.endpoint_url = self.base_url
        else:
            self.endpoint_url = f"{self.base_url}/embeddings"

        logger.info(f"Initialized LocalEmbeddingClient: {self.model} @ {self.endpoint_url}")

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Generuje embeddingi dla listy tekstów.
        Wymagana przez interfejs LangChain.
        """
        # Możemy wysłać batchowo lub w pętli.
        # Dla bezpieczeństwa przy lokalnych serwerach, zrobimy prostą pętlę wrapper,
        # lub wyślemy batch jeśli serwer to obsługuje.
        # Tu implementacja bezpieczna (batch request):

        return [self.embed_query(text) for text in texts]

    def embed_query(self, text: str) -> List[float]:
        """
        Generuje embedding dla pojedynczego tekstu.
        Wymagana przez interfejs LangChain.
        """
        # 1. Czyszczenie danych
        if hasattr(text, 'page_content'):  # Obsługa obiektów Document
            text = text.page_content

        # Wymuszenie stringa i usunięcie nowych linii
        clean_text = str(text).replace("\n", " ").strip()

        # Obsługa pustego tekstu (zwracamy wektor zerowy)
        if not clean_text:
            logger.warning("Pominięto pusty tekst (zwracam wektor zerowy).")
            return np.zeros(self.dimensions, dtype=np.float32).tolist()

        # 2. Przygotowanie żądania HTTP
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        # Domyślny payload (pojedynczy string)
        payload = {
            "input": clean_text,
            "model": self.model
        }

        try:
            # 3. Wysłanie żądania
            response = requests.post(self.endpoint_url, json=payload, headers=headers, timeout=60)

            # 4. Obsługa błędów (Retry logic)
            if response.status_code != 200:
                logger.warning(
                    f"Embedding Server Error {response.status_code}: {response.text}. Retrying with list format...")

                # Fallback: Niektóre serwery wymagają listy ["tekst"]
                payload["input"] = [clean_text]
                response = requests.post(self.endpoint_url, json=payload, headers=headers, timeout=60)

                if response.status_code != 200:
                    raise Exception(f"Server rejected input: {response.text}")

            # 5. Parsowanie wyniku
            data = response.json()

            if "data" in data and len(data["data"]) > 0:
                embedding = data["data"][0]["embedding"]
                # Zwracamy listę floatów (nie numpy array), bo tego oczekuje LangChain w interfejsie
                return embedding
            else:
                raise Exception(f"Invalid response format: {data}")

        except Exception as e:
            logger.error(f"CRITICAL ERROR in LocalEmbeddingClient: {e}")
            raise e