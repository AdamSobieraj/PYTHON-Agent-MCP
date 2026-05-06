import logging
import os
import sys
from typing import Dict, Any, Generator, Tuple, Protocol, List

from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings

from buissnes_agent.config_loader import get_settings
# Chunkings
from buissnes_agent.textchunker.langchain.LangChainChunker import LangChainChunker
from buissnes_agent.textchunker.noLibChunker.NoLibChunker import NoLibChunker as LegacyChunker

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)


# ==============================================================================
# DEFINICJA INTERFEJSU (KONTRAKTU) Wymagania dla Bazy Wektorowej
# ==============================================================================
class VectorStoreInterface(Protocol):

    def count(self) -> int:
        """Zwraca liczbę wektorów w bazie."""
        ...

    def insert_batch(self, items: List[Dict[str, Any]]) -> None:
        """
        Wstawia paczkę dokumentów.
        items: Lista słowników zawierających klucze 'text', 'vector', 'metadata'.
        """
        ...

    def search(self, query_vector: List[float], limit: int = 3) -> List[Dict]:
        """
        Wyszukuje podobne wektory.
        Zwraca listę wyników (słowniki z 'text' i 'score').
        """
        ...


# ==============================================================================
# INTERFEJS 2: ŹRÓDŁO DANYCH (Data Loader)
# ==============================================================================
class DataLoaderInterface(Protocol):
    """
    Abstrakcja źródła danych.
    Ujednolica sposób pobierania plików z S3 (DataLoaderS3FileLoader)
    oraz z dysku lokalnego (DataLoaderLocalFileLoader).
    """

    def list_objects(self) -> Generator[str, None, None]:
        """
        Zwraca generator kluczy/ścieżek do plików.
        """
        ...

    # --- POPRAWKA: Typ zwracany to teraz Tuple[List[Document], Dict[str, Any]] ---
    def load_file_with_metadata(self, key: str) -> Tuple[List[Document], Dict[str, Any]]:
        """
        Pobiera treść pliku i jego metadane na podstawie klucza.
        Returns: (lista_stron_jako_documents, base_metadata_dict)
        """
        ...


# ==============================================================================
# KLASA ORKIESTRATORA
# ==============================================================================
class SearchKnowledgebase:
    """
    ### Klasa Orkiestrator (Coordinator Class)

    Realizuje proces w 3 krokach:
    1. **Setup Danych:** Wybór odpowiedniego Loadera (S3 lub Local).
    2. **Setup Logiki:** Wybór odpowiedniego Chunkera (LangChain lub Legacy).
    3. **Execution (Pipeline):** Jednolita pętla przetwarzania (Load -> Chunk -> Embed -> Store).
    """

    def __init__(
            self,
            client: Embeddings,
            database_store: VectorStoreInterface,
            data_loader: DataLoaderInterface,
            embedding_model: str,
            batch_size: int = 50,
            force_refresh: bool = False
    ):
        self.client = client
        self.store = database_store
        self.model = embedding_model
        self.batch_size = batch_size
        self.data_loader = data_loader

        # ======================================================================
        # ETAP Weryfikacja i Uruchomienie
        # ======================================================================
        count = self.store.count()
        logger.info(f"Stan bazy wektorowej: {count} dokumentów.")

        if count > 0 and not force_refresh:
            logger.info("SKIP: Baza niepusta. Ingestia pominięta.")
        else:
            logger.info("START: Uruchamianie jednolitego procesu ETL...")
            self.perform_ingestion()

    def perform_ingestion(self):
        batch_items = []
        files_processed = 0

        object_generator = self.data_loader.list_objects()

        for object_key in object_generator:
            logger.info(f"Processing: {object_key}")

            try:
                # Loader zwraca teraz listę stron (List[Document])
                documents_list, file_metadata = self.data_loader.load_file_with_metadata(object_key)

                if not documents_list:
                    continue

                # Dodaj numerację linii przed chunkowaniem
                self._add_line_numbers_to_documents(documents_list)

                # Wzbogacamy każdą stronę o ogólne metadane pliku (jeśli loader tego nie zrobił)
                # Choć zaktualizowane loadery już to robią, ten krok jest świetnym zabezpieczeniem.
                for doc in documents_list:
                    for key, value in file_metadata.items():
                        # Jeśli klucza nie ma na stronie, ALBO jeśli strona ma pod tym kluczem None
                        if key not in doc.metadata or doc.metadata.get(key) is None:
                            doc.metadata[key] = value

                # 3. CHUNKING (Transform) - Przekazujemy LISTĘ DOKUMENTÓW i metadane pliku
                processed_chunks = self._transform_to_chunks(object_key, documents_list, file_metadata)

                # 4. EMBEDDING & BATCHING
                self._embed_and_queue_batch(processed_chunks, batch_items)

                files_processed += 1

            except Exception as e:
                logger.error(f"Błąd przetwarzania pliku {object_key}: {e}")
                continue

        if batch_items:
            self.store.insert_batch(batch_items)

        logger.info(f"PROCES ZAKOŃCZONY. Przetworzono plików: {files_processed}")

    # --- Zabezpieczenie dla starego Legacy Chunker ---
    def _transform_to_chunks(self, object_key: str, documents_list: List[Document], base_metadata: dict) -> list[dict]:
        """
        Transformuje strony na listę chunków ze zunifikowanymi metadanymi.
        """
        settings = get_settings()
        chunk_module = settings.get("chunking.module")
        ext = os.path.splitext(object_key)[1].lower()

        chunk_size, chunk_overlap, strategy = self._get_chunk_config(chunk_module, ext)

        if chunk_module in ["langchain"]:
            logger.info(f"LOGIC LAYER: Wybrano LangChainChunker. Strategia: {strategy}")
            chunker_engine = LangChainChunker(strategy, chunk_size, chunk_overlap)
            processed_chunks = chunker_engine.process_content(documents_list)

            # Dodaj numery linii do chunków
            self._add_line_numbers_to_chunks(processed_chunks, documents_list)

            return processed_chunks

        else:
            logger.info("LOGIC LAYER: Wybrano Legacy Chunker.")
            chunker_engine = LegacyChunker(strategy, chunk_size, chunk_overlap)

            # --- SUPER POPRAWKA: Przetwarzamy starym systemem strona po stronie! ---
            all_legacy_chunks = []

            for doc in documents_list:
                # doc.metadata zawiera już poprawny page_number (1, 2, 3...)
                # doc.page_content to tekst tylko z tej konkretnej strony
                page_chunks = chunker_engine.process_content(doc.page_content, doc.metadata)

                # Dodaj numery linii dla legacy chunków
                self._add_line_numbers_to_legacy_chunks(page_chunks, doc)

                all_legacy_chunks.extend(page_chunks)

            return all_legacy_chunks

    def _embed_and_queue_batch(self, processed_chunks: list[dict], batch_items: list[dict]) -> None:
        """
        Generuje embeddingi dla chunków i dodaje je do kolejki (batch).
        """
        for item in processed_chunks:
            text_content = item["text"]
            metadata = item["metadata"]

            # Generowanie wektora
            vec = self.client.embed_query(text_content)

            batch_items.append({
                "text": text_content,
                "vector": vec,
                "metadata": metadata
            })

            # Sprawdzenie wielkości paczki i wysyłka
            if len(batch_items) >= self.batch_size:
                self.store.insert_batch(batch_items)
                batch_items.clear()

    def _get_chunk_config(self, module_name: str, ext: str) -> tuple[int, int, str]:
        """
        Uniwersalna metoda pobierająca konfigurację chunkowania z obiektu settings.
        Zastępuje hardkodowane match/case.

        Logika:
        1. Szuka konfiguracji w: chunking.strategies.{module_name}.{ext_bez_kropki}
        2. Jeśli brak, szuka w: chunking.strategies.{module_name}.def (fallback modułu)
        3. Pobiera parametry, uzupełniając braki globalnymi wartościami domyślnymi.
        """
        settings = get_settings()

        clean_ext = ext.lstrip(".").lower()
        if not clean_ext:
            clean_ext = "def"

        base_path = f"chunking.strategies.{module_name}"
        ext_config = settings.get(f"{base_path}.{clean_ext}")

        if not ext_config:
            logger.debug(f"Brak strategii dla {clean_ext} w module {module_name}. Używam fallbacku 'def'.")
            ext_config = settings.get(f"{base_path}.def")

        if not ext_config:
            logger.warning(f"CRITICAL: Brak konfiguracji fallback 'def' dla modułu {module_name}!")
            ext_config = {}

        global_default_size = settings.get("chunking.default_size")
        global_default_overlap = settings.get("chunking.default_overlap")

        chunk_size = ext_config.get("size", global_default_size)
        chunk_overlap = ext_config.get("overlap", global_default_overlap)

        strategy = ext_config.get("strategy", "recursive" if module_name == "langchain" else "auto")

        return int(chunk_size), int(chunk_overlap), str(strategy)

    def _add_line_numbers_to_documents(self, documents_list: List[Document]) -> None:
        """
        Dodaje do metadanych każdej strony zakres linii w oryginalnym pliku Markdown.
        document_line_start/end = zakres całej strony
        """
        current_line = 1

        for doc in documents_list:
            line_count = doc.page_content.count('\n') + 1

            doc.metadata['document_line_start'] = current_line
            doc.metadata['document_line_end'] = current_line + line_count - 1

            current_line += line_count

        logger.info(f"Numeracja stron: {len(documents_list)} stron, łącznie {current_line - 1} linii")


    def _calculate_chunk_line_numbers(self, chunk_text: str, original_text: str, page_line_start: int,
                                      last_position: int = 0) -> Tuple[int, int, int]:
        """
        Oblicza numer linii początkowej i końcowej dla danego chunka.

        Args:
            chunk_text: Tekst chunka
            original_text: Oryginalny tekst strony
            page_line_start: Numer linii, od której zaczyna się cała strona
            last_position: Ostatnia pozycja w tekście (dla śledzenia kolejnych chunków)

        Returns:
            Tuple[chunk_line_start, chunk_line_end, new_position]
        """
        # Znajdź pozycję chunka w oryginalnym tekście (od ostatniej pozycji)
        chunk_position = original_text.find(chunk_text, last_position)

        if chunk_position == -1:
            # Jeśli nie znaleziono (może być zmodyfikowany przez chunker), użyj last_position
            chunk_position = last_position

        # Policz linie przed chunkiem (od początku strony)
        text_before_chunk = original_text[:chunk_position]
        lines_before = text_before_chunk.count('\n')

        # Policz linie w samym chunku
        lines_in_chunk = chunk_text.count('\n')

        # Oblicz zakres linii
        chunk_line_start = page_line_start + lines_before
        chunk_line_end = chunk_line_start + lines_in_chunk

        # Jeśli chunk nie kończy się znakiem nowej linii, ale ma jakąś treść, to zajmuje tę linię
        if chunk_text and not chunk_text.endswith('\n'):
            chunk_line_end += 1

        # Nowa pozycja do śledzenia następnego chunka
        new_position = chunk_position + len(chunk_text)

        return chunk_line_start, chunk_line_end, new_position

    def _add_line_numbers_to_chunks(self, chunks: List[Dict[str, Any]], documents_list: List[Document]) -> None:
        """
        Dodaje do każdego chunka:
        1. document_line_start/end - zakres STRONY źródłowej (kopiowane)
        2. embedding_line_start/end - zakres CHUNKA w oryginalnym pliku (obliczane)
        """
        for chunk in chunks:
            chunk_text = chunk["text"]
            chunk_metadata = chunk["metadata"]

            chunk_page_number = chunk_metadata.get("page_number")

            if chunk_page_number is None:
                logger.warning(" Chunk bez page_number - pomijam numerację linii")
                continue

            # Znajdź stronę źródłową
            original_doc = None
            for doc in documents_list:
                if doc.metadata.get("page_number") == chunk_page_number:
                    original_doc = doc
                    break

            if original_doc is None:
                logger.warning(f"Nie znaleziono strony {chunk_page_number}")
                continue

            # 1. KOPIUJ zakres STRONY do chunka (document_line_*)
            page_line_start = original_doc.metadata.get("document_line_start", 1)
            page_line_end = original_doc.metadata.get("document_line_end", 1)

            chunk_metadata["document_line_start"] = page_line_start  # ✅ Zakres całej strony
            chunk_metadata["document_line_end"] = page_line_end  # ✅ Zakres całej strony

            # 2. OBLICZ zakres CHUNKA (embedding_line_*)
            page_text = original_doc.page_content
            chunk_position = page_text.find(chunk_text)

            if chunk_position == -1:
                # Fallback - jeśli nie znaleziono chunka, użyj zakresu całej strony
                logger.debug(f"Chunk nie znaleziony w tekście strony {chunk_page_number}")
                chunk_metadata["embedding_line_start"] = page_line_start
                chunk_metadata["embedding_line_end"] = page_line_end
                continue

            # Policz linie przed chunkiem (w obrębie strony)
            text_before_chunk = page_text[:chunk_position]
            lines_before = text_before_chunk.count('\n')

            # Policz linie w samym chunku
            lines_in_chunk = chunk_text.count('\n')

            # Oblicz GLOBALNY zakres chunka w pliku
            chunk_line_start = page_line_start + lines_before
            chunk_line_end = chunk_line_start + lines_in_chunk

            # Jeśli chunk ma treść i nie kończy się \n, zajmuje jeszcze jedną linię
            if chunk_text and not chunk_text.endswith('\n'):
                chunk_line_end += 1

            chunk_metadata["embedding_line_start"] = chunk_line_start  # Zakres chunka
            chunk_metadata["embedding_line_end"] = chunk_line_end  # akres chunka

        logger.info(f"Numeracja chunków: {len(chunks)} chunków przetworzonych")

    def _add_line_numbers_to_legacy_chunks(self, chunks: List[Dict[str, Any]], original_doc: Document) -> None:
        """
        Dodaje do każdego legacy chunka:
        1. document_line_start/end - zakres STRONY źródłowej
        2. embedding_line_start/end - zakres CHUNKA w oryginalnym pliku
        """
        page_line_start = original_doc.metadata.get("document_line_start", 1)
        page_line_end = original_doc.metadata.get("document_line_end", 1)
        page_text = original_doc.page_content

        current_position = 0

        for chunk in chunks:
            chunk_text = chunk["text"]
            chunk_metadata = chunk["metadata"]

            # 1. KOPIUJ zakres STRONY
            chunk_metadata["document_line_start"] = page_line_start
            chunk_metadata["document_line_end"] = page_line_end

            # 2. OBLICZ zakres CHUNKA
            chunk_position = page_text.find(chunk_text, current_position)

            if chunk_position == -1:
                chunk_position = current_position

            text_before_chunk = page_text[:chunk_position]
            lines_before = text_before_chunk.count('\n')

            lines_in_chunk = chunk_text.count('\n')

            chunk_line_start = page_line_start + lines_before
            chunk_line_end = chunk_line_start + lines_in_chunk

            if chunk_text and not chunk_text.endswith('\n'):
                chunk_line_end += 1

            chunk_metadata["embedding_line_start"] = chunk_line_start
            chunk_metadata["embedding_line_end"] = chunk_line_end

            current_position = chunk_position + len(chunk_text)

        logger.info(f"Legacy chunków: {len(chunks)} chunków przetworzonych")