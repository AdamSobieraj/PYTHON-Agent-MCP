import logging
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
# INTERFACE DEFINITION (CONTRACT) - Requirements for Vector Database
# ==============================================================================
class VectorStoreInterface(Protocol):

    def count(self) -> int:
        """Returns the number of vectors in the database."""
        ...

    def insert_batch(self, items: List[Dict[str, Any]]) -> None:
        """
        Inserts a batch of documents.
        items: List of dictionaries containing keys 'text', 'vector', 'metadata'.
        """
        ...

    def search(self, query_vector: List[float], limit: int = 3) -> List[Dict]:
        """
        Searches for similar vectors.
        Returns a list of results (dictionaries with 'text' and 'score').
        """
        ...


# ==============================================================================
# INTERFACE 2: DATA SOURCE (Data Loader)
# ==============================================================================
class DataLoaderInterface(Protocol):
    """
    Data source abstraction.
    Unifies the way files are fetched from S3 (DataLoaderS3FileLoader)
    and from local disk (DataLoaderLocalFileLoader).
    """

    def list_objects(self) -> Generator[str, None, None]:
        """
        Returns a generator of file keys/paths.
        """
        ...

    def load_file_with_metadata(self, key: str) -> Tuple[List[Document], Dict[str, Any]]:
        """
        Fetches file content and its metadata based on the key.
        Returns: (list_of_pages_as_documents, base_metadata_dict)
        """
        ...


# ==============================================================================
# ORCHESTRATOR CLASS
# ==============================================================================
class SearchKnowledgebase:
    """
    ### Orchestrator Class (Coordinator Class)

    Executes the process in 3 steps:
    1. **Data Setup:** Selecting the appropriate Loader (S3 or Local).
    2. **Logic Setup:** Selecting the appropriate Chunker (LangChain or Legacy).
    3. **Execution (Pipeline):** Unified processing loop (Load -> Chunk -> Embed -> Store).
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
        # PHASE: Verification and Startup
        # ======================================================================
        count = self.store.count()
        logger.info("Vector database state: %d documents.", count)

        if count > 0 and not force_refresh:
            logger.info("SKIP: Database not empty. Ingestion skipped.")
        else:
            logger.info("START: Launching unified ETL process...")
            self.perform_ingestion()

    def perform_ingestion(self):
        batch_items = []
        files_processed = 0

        object_generator = self.data_loader.list_objects()

        for object_key in object_generator:
            logger.info("Processing: %s", object_key)

            try:
                # Loader now returns a list of pages (List[Document])
                documents_list, file_metadata = self.data_loader.load_file_with_metadata(object_key)

                if not documents_list:
                    continue

                # Add line numbering before chunking
                self._add_line_numbers_to_documents(documents_list)

                # Enrich each page with general file metadata (if loader hasn't done so).
                # Although updated loaders already do this, this step is a great safeguard.
                for doc in documents_list:
                    for key, value in file_metadata.items():
                        # If key is missing from the page, OR if the page has None under this key
                        if key not in doc.metadata or doc.metadata.get(key) is None:
                            doc.metadata[key] = value

                # 3. CHUNKING (Transform) - Pass LIST OF DOCUMENTS and file metadata
                processed_chunks = self._transform_to_chunks(object_key, documents_list, file_metadata)

                # 4. EMBEDDING & BATCHING
                self._embed_and_queue_batch(processed_chunks, batch_items)

                files_processed += 1

            except Exception as e:
                logger.error("Error processing file %s: %s", object_key, e)
                continue

        if batch_items:
            self.store.insert_batch(batch_items)

        logger.info("PROCESS COMPLETE. Files processed: %d", files_processed)

    def _transform_to_chunks(
            self,
            object_key: str,
            documents_list: List[Document],
            base_metadata: dict
    ) -> list[dict]:
        """
        Transforms pages into a list of chunks with unified metadata.

        Note: All incoming files are pre-converted .md files from Project 1.
        The original file extension is read from metadata (field 'extension')
        so that the correct chunking strategy can be selected.
        Falls back to 'def' if the original extension is unknown.
        """
        settings = get_settings()
        chunk_module = settings.get("chunking.module")

        # All files arriving here are .md (pre-converted by Project 1).
        # We read the ORIGINAL extension from metadata to select the correct
        # chunking strategy (e.g., pdf -> recursive, xlsx -> def).
        # Falls back to 'def' if original extension is not stored in metadata.
        original_ext = base_metadata.get("extension", "")
        ext = original_ext if original_ext and original_ext != ".md" else ".md"

        chunk_size, chunk_overlap, strategy = self._get_chunk_config(chunk_module, ext)

        if chunk_module in ["langchain"]:
            logger.info(
                "LOGIC LAYER: LangChainChunker selected. Strategy: %s",
                strategy
            )
            chunker_engine = LangChainChunker(strategy, chunk_size, chunk_overlap)
            processed_chunks = chunker_engine.process_content(documents_list)

            # Add line numbers to chunks
            self._add_line_numbers_to_chunks(processed_chunks, documents_list)

            return processed_chunks

        else:
            logger.info("LOGIC LAYER: Legacy Chunker selected.")
            chunker_engine = LegacyChunker(strategy, chunk_size, chunk_overlap)

            # Process with legacy system page by page
            all_legacy_chunks = []

            for doc in documents_list:
                # doc.metadata already contains correct page_number (1, 2, 3...)
                # doc.page_content is text only from this specific page
                page_chunks = chunker_engine.process_content(doc.page_content, doc.metadata)

                # Add line numbers for legacy chunks
                self._add_line_numbers_to_legacy_chunks(page_chunks, doc)

                all_legacy_chunks.extend(page_chunks)

            return all_legacy_chunks

    def _embed_and_queue_batch(
            self,
            processed_chunks: list[dict],
            batch_items: list[dict]
    ) -> None:
        """
        Generates embeddings for chunks and adds them to the queue (batch).
        """
        for item in processed_chunks:
            text_content = item["text"]
            metadata = item["metadata"]

            # Generate vector
            vec = self.client.embed_query(text_content)

            batch_items.append({
                "text": text_content,
                "vector": vec,
                "metadata": metadata
            })

            # Check batch size and send
            if len(batch_items) >= self.batch_size:
                self.store.insert_batch(batch_items)
                batch_items.clear()

    def _get_chunk_config(self, module_name: str, ext: str) -> tuple[int, int, str]:
        """
        Universal method for fetching chunking configuration from the settings object.
        Replaces hardcoded match/case.

        Logic:
        1. Looks for config at: chunking.strategies.{module_name}.{ext_without_dot}
        2. If not found, looks at: chunking.strategies.{module_name}.def (module fallback)
        3. Fetches parameters, filling gaps with global default values.
        """
        settings = get_settings()

        clean_ext = ext.lstrip(".").lower()
        if not clean_ext:
            clean_ext = "def"

        base_path = f"chunking.strategies.{module_name}"
        ext_config = settings.get(f"{base_path}.{clean_ext}")

        if not ext_config:
            logger.debug(
                "No strategy for '%s' in module '%s'. Using 'def' fallback.",
                clean_ext, module_name
            )
            ext_config = settings.get(f"{base_path}.def")

        if not ext_config:
            logger.warning(
                "CRITICAL: No 'def' fallback config for module '%s'!",
                module_name
            )
            ext_config = {}

        global_default_size = settings.get("chunking.default_size")
        global_default_overlap = settings.get("chunking.default_overlap")

        chunk_size = ext_config.get("size", global_default_size)
        chunk_overlap = ext_config.get("overlap", global_default_overlap)

        strategy = ext_config.get(
            "strategy",
            "recursive" if module_name == "langchain" else "auto"
        )

        return int(chunk_size), int(chunk_overlap), str(strategy)

    def _add_line_numbers_to_documents(self, documents_list: List[Document]) -> None:
        """
        Adds to each page's metadata the line range in the original Markdown file.
        document_line_start/end = range of the entire page
        """
        current_line = 1

        for doc in documents_list:
            line_count = doc.page_content.count('\n') + 1

            doc.metadata['document_line_start'] = current_line
            doc.metadata['document_line_end'] = current_line + line_count - 1

            current_line += line_count

        logger.info(
            "Page numbering: %d pages, %d lines total",
            len(documents_list),
            current_line - 1
        )

    def _calculate_chunk_line_numbers(
            self,
            chunk_text: str,
            original_text: str,
            page_line_start: int,
            last_position: int = 0
    ) -> Tuple[int, int, int]:
        """
        Calculates the start and end line number for a given chunk.

        Args:
            chunk_text: Chunk text
            original_text: Original page text
            page_line_start: Line number where the entire page starts
            last_position: Last position in the text (for tracking subsequent chunks)

        Returns:
            Tuple[chunk_line_start, chunk_line_end, new_position]
        """
        # Find chunk position in the original text (from last position)
        chunk_position = original_text.find(chunk_text, last_position)

        if chunk_position == -1:
            # If not found (may have been modified by chunker), use last_position
            chunk_position = last_position

        # Count lines before the chunk (from the beginning of the page)
        text_before_chunk = original_text[:chunk_position]
        lines_before = text_before_chunk.count('\n')

        # Count lines in the chunk itself
        lines_in_chunk = chunk_text.count('\n')

        # Calculate line range
        chunk_line_start = page_line_start + lines_before
        chunk_line_end = chunk_line_start + lines_in_chunk

        # If chunk does not end with newline but has content, it occupies that line
        if chunk_text and not chunk_text.endswith('\n'):
            chunk_line_end += 1

        # New position for tracking the next chunk
        new_position = chunk_position + len(chunk_text)

        return chunk_line_start, chunk_line_end, new_position

    def _add_line_numbers_to_chunks(
            self,
            chunks: List[Dict[str, Any]],
            documents_list: List[Document]
    ) -> None:
        """
        Adds to each chunk:
        1. document_line_start/end - range of the SOURCE PAGE (copied)
        2. embedding_line_start/end - range of the CHUNK in the original file (calculated)
        """
        for chunk in chunks:
            chunk_text = chunk["text"]
            chunk_metadata = chunk["metadata"]

            chunk_page_number = chunk_metadata.get("page_number")

            if chunk_page_number is None:
                logger.warning("Chunk without page_number - skipping line numbering")
                continue

            # Find the source page
            original_doc = None
            for doc in documents_list:
                if doc.metadata.get("page_number") == chunk_page_number:
                    original_doc = doc
                    break

            if original_doc is None:
                logger.warning("Page %s not found", chunk_page_number)
                continue

            # 1. COPY page range to chunk (document_line_*)
            page_line_start = original_doc.metadata.get("document_line_start", 1)
            page_line_end = original_doc.metadata.get("document_line_end", 1)

            chunk_metadata["document_line_start"] = page_line_start  # Range of entire page
            chunk_metadata["document_line_end"] = page_line_end      # Range of entire page

            # 2. CALCULATE chunk range (embedding_line_*)
            page_text = original_doc.page_content
            chunk_position = page_text.find(chunk_text)

            if chunk_position == -1:
                # Fallback - if chunk not found, use entire page range
                logger.debug(
                    "Chunk not found in page %s text",
                    chunk_page_number
                )
                chunk_metadata["embedding_line_start"] = page_line_start
                chunk_metadata["embedding_line_end"] = page_line_end
                continue

            # Count lines before the chunk (within the page)
            text_before_chunk = page_text[:chunk_position]
            lines_before = text_before_chunk.count('\n')

            # Count lines in the chunk itself
            lines_in_chunk = chunk_text.count('\n')

            # Calculate GLOBAL chunk range in the file
            chunk_line_start = page_line_start + lines_before
            chunk_line_end = chunk_line_start + lines_in_chunk

            # If chunk has content and does not end with \n, it occupies one more line
            if chunk_text and not chunk_text.endswith('\n'):
                chunk_line_end += 1

            chunk_metadata["embedding_line_start"] = chunk_line_start  # Chunk range
            chunk_metadata["embedding_line_end"] = chunk_line_end      # Chunk range

        logger.info("Chunk numbering: %d chunks processed", len(chunks))

    def _add_line_numbers_to_legacy_chunks(
            self,
            chunks: List[Dict[str, Any]],
            original_doc: Document
    ) -> None:
        """
        Adds to each legacy chunk:
        1. document_line_start/end - range of the SOURCE PAGE
        2. embedding_line_start/end - range of the CHUNK in the original file
        """
        page_line_start = original_doc.metadata.get("document_line_start", 1)
        page_line_end = original_doc.metadata.get("document_line_end", 1)
        page_text = original_doc.page_content

        current_position = 0

        for chunk in chunks:
            chunk_text = chunk["text"]
            chunk_metadata = chunk["metadata"]

            # 1. COPY page range
            chunk_metadata["document_line_start"] = page_line_start
            chunk_metadata["document_line_end"] = page_line_end

            # 2. CALCULATE chunk range
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

        logger.info("Legacy chunks: %d chunks processed", len(chunks))