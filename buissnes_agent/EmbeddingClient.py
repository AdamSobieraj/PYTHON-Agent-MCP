import logging
import os
import random
import time
from typing import List, Any

import requests
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
                 dimensions: int = None,
                 batch_size: int = None):

        # Pobieranie konfiguracji z argumentów lub zmiennych środowiskowych (.env)
        self.base_url = base_url or os.getenv("EMBEDDING_BASE_URL")
        self.api_key = api_key or os.getenv("EMBEDDING_API_KEY")
        self.model = model or os.getenv("EMBEDDING_MODEL")
        self.dimensions = int(dimensions or os.getenv("EMBEDDING_DIM"))

        # Konfiguracja mechanizmu Retry
        self.max_retries = int(os.getenv("EMBEDDING_MAX_RETRIES"))
        self.base_delay = float(os.getenv("EMBEDDING_DELAY"))

        # Ograniczenie ilości tekstów wysyłanych w jednym żądaniu HTTP
        self.batch_size = batch_size or int(os.getenv("EMBEDDING_BATCH_SIZE"))

        self.endpoint_url = f"{self.base_url}"

        # 2. Inicjalizacja stałej sesji HTTP (przyspiesza zapytania w pętli - Connection Pooling)
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        })

        logger.info(f"Initialized LocalEmbeddingClient: {self.model} @ {self.endpoint_url}")

    def _clean_text(self, text: Any) -> str:
        """Prywatna metoda do czyszczenia pojedynczego tekstu."""
        if hasattr(text, 'page_content'):
            text = text.page_content

        clean = str(text).replace("\n", " ").strip()
        # Zabezpieczenie przed pustym stringiem wewnątrz batcha
        return clean if clean else " "

    def _post_with_retry(self, payload: dict) -> List[List[float]]:
        """
        Główny silnik wysyłający zapytania HTTP z wbudowanym Retry, Backoff i Jitter.
        Zwraca listę wektorów embeddingów.
        """

        for attempt in range(self.max_retries):
            try:
                response = self.session.post(self.endpoint_url, json=payload, timeout=120)

                if response.status_code == 200:
                    data = response.json()
                    if "data" in data and len(data["data"]) > 0:
                        # Zwracamy listę wektorów (niezależnie czy to jeden tekst czy batch)
                        # API OpenAI sortuje wyniki w tablicy 'data', musimy je poprawnie wyciągnąć
                        sorted_data = sorted(data["data"], key=lambda x: x.get("index", 0))
                        return [item["embedding"] for item in sorted_data]
                    else:
                        raise ValueError(f"Nieprawidłowy format odpowiedzi: {data}")

                # Błąd 400 - niektóre serwery odrzucają stringa, wymagając jednoelementowej listy
                if response.status_code == 400 and isinstance(payload["input"], str):
                    logger.warning("Błąd 400. Zmieniam payload na listę (['tekst']) dla kolejnych prób.")
                    payload["input"] = [payload["input"]]

                if attempt == self.max_retries - 1:
                    raise RuntimeError(
                        f"Błąd serwera po {self.max_retries} próbach: HTTP {response.status_code} - {response.text}")

                sleep_time = (self.base_delay * (2 ** attempt)) + random.uniform(0.1, 1.5)
                logger.warning(
                    f"Odmowa serwera (HTTP {response.status_code}). Ponawiam próbę {attempt + 1}/{self.max_retries - 1} za {sleep_time:.2f}s...")
                time.sleep(sleep_time)

            except requests.exceptions.RequestException as e:
                if attempt == self.max_retries - 1:
                    logger.error(f"KRYTYCZNY BŁĄD SIECI po {self.max_retries} próbach: {e}")
                    raise e

                sleep_time = (self.base_delay * (2 ** attempt)) + random.uniform(0.1, 1.5)
                logger.warning(
                    f"Problem z siecią: {e}. Ponawiam próbę {attempt + 1}/{self.max_retries - 1} za {sleep_time:.2f}s...")
                time.sleep(sleep_time)

        return []

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Generuje embeddingi dla listy tekstów używając BATCHINGU (Grupowania).
        Znacznie redukuje ilość zapytań HTTP i przyspiesza proces.
        """
        if not texts:
            return []

        all_embeddings = []
        clean_texts = [self._clean_text(t) for t in texts]

        # Podział dużej listy tekstów na mniejsze paczki (chunks) wg self.batch_size
        for i in range(0, len(clean_texts), self.batch_size):
            batch = clean_texts[i: i + self.batch_size]

            payload = {
                "input": batch,
                "model": self.model
            }

            logger.debug(f"Wysyłam batch {i // self.batch_size + 1} (rozmiar: {len(batch)} tekstów)")
            batch_embeddings = self._post_with_retry(payload)
            all_embeddings.extend(batch_embeddings)

        return all_embeddings

    def embed_query(self, text: str) -> List[float]:
        """
        Generuje embedding dla pojedynczego tekstu.
        """
        clean_text = self._clean_text(text)

        # Zabezpieczenie przed pustym tekstem (zwraca same zera dla szybkiej reakcji)
        if clean_text == " ":
            return [0.0] * self.dimensions

        payload = {
            "input": [clean_text],  # Standardowo wysyłamy jako jednoelementowa tablica
            "model": self.model
        }

        embeddings = self._post_with_retry(payload)
        return embeddings[0] if embeddings else [0.0] * self.dimensions