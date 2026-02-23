import logging
import os
import sys

import qdrant_client
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
import json
from buissnes_agent.config_loader import settings
import httpx
logger = logging.getLogger(__name__)

# ==============================================================================
# ZASOBY GLOBALNE (SINGLETONY)
# ==============================================================================
# Przechowujemy instancje klienta Qdrant i modelu Embeddingów globalnie,
# aby nie tworzyć nowego połączenia przy każdym zapytaniu (optymalizacja).
_qdrant_client = None
_embeddings = None

SSL_VERIFY = os.getenv("SSL_VERIFY", 'False').lower() in ('true', '1', 't')

load_dotenv()

def _init_resources():
    """
    ### LENIWA INICJALIZACJA ZASOBÓW (Lazy Loading)

    Ta funkcja jest wywoływana dopiero przy pierwszym użyciu narzędzia.

    Dlaczego:
    1. Szybszy start serwera (nie czekamy na połączenie z bazą przy bootowaniu).
    2. Odporność na błędy (jeśli Qdrant leży, serwer wstanie, a błąd pojawi się dopiero przy pytaniu).
    """
    global _qdrant_client, _embeddings

    # Jeśli zasoby już istnieją, nie rób nic.
    if _qdrant_client and _embeddings:
        return

    try:
        # Pobranie konfiguracji z .env
        emb_model = os.getenv('EMBEDDING_MODEL')
        emb_url = os.getenv('EMBEDDING_BASE_URL')
        emb_key = os.getenv('EMBEDDING_API_KEY')
        qdrant_url = os.getenv('QDRANT_API')
        qdrant_key = os.getenv('QDRANT_API_KEY')

        if not emb_model:
            raise ValueError("Brak zmiennej EMBEDDING_MODEL w pliku .env")

        # 1. Inicjalizacja klienta bazy wektorowej Qdrant
        _qdrant_client = qdrant_client.QdrantClient(
            url=qdrant_url,
            api_key=qdrant_key,
        )

        # 2. Inicjalizacja modelu Embeddingów (OpenAI lub Local/Nomic)
        # check_embedding_ctx_length=False pozwala na dłuższe teksty (ważne przy RAG)
        sync_client = httpx.Client(
            verify=SSL_VERIFY,
        )
        async_client = httpx.AsyncClient(
            verify=SSL_VERIFY,
        )
        _embeddings = OpenAIEmbeddings(
            model=emb_model,
            base_url=emb_url,
            api_key=emb_key,
            check_embedding_ctx_length=False,
            http_client=sync_client,
            http_async_client=async_client,
            default_headers=json.loads(os.getenv('DEFAULT_HEADERS')),
        )
        print(f"[ISO Tool] Połączono z Qdrant i skonfigurowano Embeddingi ({emb_model}).", file=sys.stderr)

    except Exception as e:
        print(f"[ISO Tool] Błąd krytyczny inicjalizacji: {e}", file=sys.stderr)
        raise e


def run_generic_rag(query: str, collection_name: str) -> str:
    """
    ### GŁÓWNA LOGIKA NARZĘDZIA RAG

    1. Zamienia pytanie tekstowe na wektor (Embedding).
    2. Szuka w bazie Qdrant wektorów najbardziej podobnych (Search).
    3. Zwraca surowy tekst dokumentacji wraz z metadanymi.
    """
    top_k = 5  # Ilość zwracanych fragmentów

    # Upewnij się, że mamy połączenie z bazą
    try:
        _init_resources()
    except Exception as e:
        return f"Błąd techniczny: Nie udało się połączyć z bazą wiedzy ({str(e)})."

    if not _qdrant_client or not _embeddings:
        return "Błąd techniczny: Narzędzie RAG nie jest poprawnie skonfigurowane."

    print(f"[RAG] Szukam: '{query}' w kolekcji '{collection_name}'", file=sys.stderr)

    try:
        # KROK 1: Generowanie wektora zapytania
        query_vector = _embeddings.embed_query(query)

        # KROK 2: Wyszukiwanie w Qdrant (Metoda query_points)
        # ZMIANA: Używamy query_points zamiast search
        search_response = _qdrant_client.query_points(
            collection_name=collection_name,
            query=query_vector,  # ZMIANA: parametr nazywa się 'query', a nie 'query_vector'
            limit=top_k,
            with_payload=True
        )

        # ZMIANA: query_points zwraca obiekt QueryResponse, a punkty są w atrybucie .points
        points = search_response.points

        if not points:
            return "Nie znaleziono relewantnych dokumentów w bazie wiedzy ISO 20022."

        # KROK 3: Formatowanie wyniku dla LLM
        formatted_output = []
        for i, point in enumerate(points, 1):
            payload = point.payload or {}

            # --- EKSTRAKCJA PÓL Z PAYLOADU ---
            # Treść główna
            content = payload.get("phrase") or payload.get("text") or "[BRAK TREŚCI]"

            # Podstawowe informacje
            title = payload.get("title", "Bez tytułu")
            source_path = payload.get("source", "Nieznane źródło")

            # Dodatkowe metadane (zgodnie z Twoim JSON-em)
            url = payload.get("url", "-")
            domain = payload.get("domain", "ogólna")
            extension = payload.get("extension", "")
            meta_id = payload.get("phrase_metadata_id", "brak-id")

            # Obsługa tagów (lista -> string)
            tags_list = payload.get("tags", [])
            tags_str = ", ".join(tags_list) if isinstance(tags_list, list) else str(tags_list)

            # Opcjonalne (jeśli wystąpią w innych plikach)
            page = payload.get("page_number")
            page_info = f", Strona: {page}" if page else ""

            # --- BUDOWANIE WPISU ---
            entry = (
                f"--- DOKUMENT {i} (Relewancja: {point.score:.4f}) ---\n"
                f"Tytuł: {title}\n"
                f"Źródło (plik): {source_path}{page_info}\n"
                f"URL: {url}\n"
                f"Domena: {domain}\n"
                f"Typ: {extension}\n"
                f"Tagi: {tags_str}\n"
                f"ID Fragmentu: {meta_id}\n"
                f"Treść:\n{content.strip()}"
            )
            formatted_output.append(entry)

        return "\n\n".join(formatted_output)

    except Exception as e:
        err_msg = f"Błąd podczas przeszukiwania bazy wiedzy: {str(e)}"
        print(f"[RAG Error] {err_msg}", file=sys.stderr)
        return err_msg