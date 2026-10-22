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
    Embedding client for local servers (LM Studio, LocalAI, Ollama),
    which bypasses the strict validations of the `langchain_openai` library.

    Sends raw HTTP requests, handling specific JSON formatting errors (HTTP 400).
    """

    def __init__(self,
                 base_url: str = None,
                 api_key: str = None,
                 model: str = None,
                 dimensions: int = None,
                 batch_size: int = None):

        # Configuration from arguments or environment variables (.env)
        self.base_url = base_url or os.getenv("EMBEDDING_BASE_URL")
        self.api_key = api_key or os.getenv("EMBEDDING_API_KEY")
        self.model = model or os.getenv("EMBEDDING_MODEL")
        self.dimensions = int(dimensions or os.getenv("EMBEDDING_DIM"))

        # Retry mechanism configuration
        self.max_retries = int(os.getenv("EMBEDDING_MAX_RETRIES", "3"))
        self.base_delay = float(os.getenv("EMBEDDING_DELAY", "1.0"))

        # Read timeout (seconds) for one embedding HTTP request.
        # Local models (e.g. 4B on LM Studio) can need minutes per batch.
        self.timeout = int(os.getenv("EMBEDDING_TIMEOUT", "600"))

        # Limit on the number of texts sent in a single HTTP request
        self.batch_size = batch_size or int(os.getenv("EMBEDDING_BATCH_SIZE", "16"))

        # EOS token workaround. Some local embedding models (e.g. Qwen3-Embedding
        # via llama.cpp) use last-token pooling and were trained with an EOS/SEP at
        # the end of the text. When the GGUF header does not declare
        # add_eos_token=true, llama.cpp computes the vector from the last word
        # instead of the EOS state (lower retrieval quality) and warns about it.
        # Instead of patching the GGUF we can append the model's EOS token to every
        # text on the client side. Toggle with EMBEDDING_APPEND_EOS; the token
        # string itself is read from EMBEDDING_EOS_TOKEN.
        self.append_eos = os.getenv("EMBEDDING_APPEND_EOS", "false").lower() in ('true', '1', 't')
        self.eos_token = os.getenv("EMBEDDING_EOS_TOKEN", "")

        self.endpoint_url = f"{self.base_url}"

        # 2. Initialize a persistent HTTP session (speeds up requests in a loop - Connection Pooling)
        self.session = requests.Session()
        
        # SSL verification disabled by default (bypassing corporate network blocks),
        # unless explicitly enabled in .env
        self.session.verify = os.getenv("SSL_VERIFY", 'False').lower() in ('true', '1', 't')
        
        # Force requests to ignore system and Python CA certificates
        # os.environ['CURL_CA_BUNDLE'] = ''
        # os.environ['REQUESTS_CA_BUNDLE'] = ''
        if(os.getenv("TRUST_ENV_FALSE", 'False').lower() in ('true', '1', 't')):
            self.session.trust_env = False 

        if(os.getenv("TRUST_ENV_TRUE", 'False').lower() in ('true', '1', 't')):
            self.session.trust_env = True 

        if not self.session.verify:
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        })

        # Cost counters (E2 metrics): number of successful HTTP calls
        # and number of texts sent for embedding.
        self.http_requests = 0
        self.texts_embedded = 0

        eos_info = f" | EOS append: ON (token={self.eos_token!r})" if (self.append_eos and self.eos_token) else ""
        logger.info(f"Initialized LocalEmbeddingClient: {self.model} @ {self.endpoint_url}{eos_info}")

    def reset_counters(self) -> None:
        """Reset cost counters (call between documents / experiments)."""
        self.http_requests = 0
        self.texts_embedded = 0

    def _clean_text(self, text: Any) -> str:
        """Private method for cleaning a single text."""
        if hasattr(text, 'page_content'):
            text = text.page_content

        clean = str(text).replace("\n", " ").strip()
        # Guard against an empty string within a batch
        return clean if clean else " "

    def _append_eos(self, text: str) -> str:
        """Append the configured EOS token when EMBEDDING_APPEND_EOS is enabled.

        The token is appended directly (no separator): EOS is a boundary token,
        so it must stand alone at the very end of the text. Empty placeholders
        are left untouched.
        """
        if self.append_eos and self.eos_token and text.strip():
            return f"{text}{self.eos_token}"
        return text

    def _post_with_retry(self, payload: dict) -> List[List[float]]:
        """
        Main engine sending HTTP requests with built-in Retry, Backoff and Jitter.
        Returns a list of embedding vectors.
        """

        for attempt in range(self.max_retries):
            try:
                logger.info(f"Sending POST to {self.endpoint_url} with verify={self.session.verify}")
                response = self.session.post(
                    self.endpoint_url,
                    json=payload,
                    timeout=self.timeout,
                    verify=self.session.verify
                )

                if response.status_code == 200:
                    self.http_requests += 1
                    data = response.json()

                    # Cost usage hook: the OpenAI-compatible embeddings API
                    # reports prompt (input) tokens in "usage"; when the
                    # server reports nothing (e.g. local LM Studio), the
                    # tokens are estimated from the payload texts
                    try:
                        from buissnes_agent.tools.rag_metrics import (
                            estimate_tokens,
                            log_cost_usage,
                        )

                        usage = data.get("usage") or {}
                        reported = int(usage.get("prompt_tokens") or 0)
                        if reported > 0:
                            input_tokens = reported
                            estimated = False
                        else:
                            raw_input = payload.get("input", "")
                            texts = raw_input if isinstance(raw_input, list) else [raw_input]
                            input_tokens = sum(estimate_tokens(t) for t in texts)
                            estimated = True
                        if input_tokens > 0:
                            log_cost_usage(
                                model=self.model,
                                section="embedding",
                                input_tokens=input_tokens,
                                output_tokens=0,
                                provider=os.getenv("EMBEDDING_PROVIDER", "local"),
                                estimated=estimated,
                            )
                    except Exception as cost_err:
                        logger.warning(f"Cost usage (embedding): {cost_err}")

                    if "data" in data and len(data["data"]) > 0:
                        # Return the list of vectors (whether it is a single text or a batch)
                        # The OpenAI API orders results in the 'data' array, we must extract them correctly
                        sorted_data = sorted(data["data"], key=lambda x: x.get("index", 0))
                        return [item["embedding"] for item in sorted_data]
                    else:
                        raise ValueError(f"Nieprawidłowy format odpowiedzi: {data}")

                # HTTP 400 - some servers reject a raw string, requiring a single-element list
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
        Generates embeddings for a list of texts using BATCHING (grouping).
        Significantly reduces the number of HTTP requests and speeds up the process.
        """
        if not texts:
            return []

        all_embeddings = []
        clean_texts = [self._append_eos(self._clean_text(t)) for t in texts]

        # Split the large list of texts into smaller packs (chunks) according to self.batch_size
        for i in range(0, len(clean_texts), self.batch_size):
            batch = clean_texts[i: i + self.batch_size]

            payload = {
                "input": batch,
                "model": self.model
            }

            logger.debug(f"Wysyłam batch {i // self.batch_size + 1} (rozmiar: {len(batch)} tekstów)")
            batch_embeddings = self._post_with_retry(payload)
            self.texts_embedded += len(batch)
            all_embeddings.extend(batch_embeddings)

        return all_embeddings

    def embed_query(self, text: str) -> List[float]:
        """
        Generates an embedding for a single text.
        """
        clean_text = self._clean_text(text)

        # Guard against empty text (returns all zeros for a fast response)
        if clean_text == " ":
            return [0.0] * self.dimensions

        clean_text = self._append_eos(clean_text)

        payload = {
            "input": [clean_text],  # We usually send it as a single-element array
            "model": self.model
        }

        embeddings = self._post_with_retry(payload)
        self.texts_embedded += 1
        return embeddings[0] if embeddings else [0.0] * self.dimensions