import logging
import os
import sys
import time
from datetime import datetime
from typing import Dict, Any, Callable, Generator, Optional, Tuple, Protocol, List

from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings

from buissnes_agent.config_loader import get_settings
# Chunkings
from buissnes_agent.textchunker.langchain.LangChainChunker import LangChainChunker

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
    2. **Logic Setup:** Selecting the chunking strategy (LangChain).
    3. **Execution (Pipeline):** Unified processing loop (Load -> Chunk -> Embed -> Store).
    """

    def __init__(
            self,
            client: Embeddings,
            database_store: VectorStoreInterface,
            data_loader: DataLoaderInterface,
            embedding_model: str,
            batch_size: int = 50,
            force_refresh: bool = False,
            strategy_name: Optional[str] = None,
            chunk_size: Optional[int] = None,
            chunk_overlap: Optional[int] = None,
            on_document: Optional[Callable] = None,
            persist_metrics: bool = True,
            metrics_run_id: Optional[str] = None
    ):
        self.client = client
        self.store = database_store
        self.model = embedding_model
        self.batch_size = batch_size
        self.data_loader = data_loader
        self._force_refresh = force_refresh

        # Explicit overrides (used by the experiment runner); when None,
        # the strategy/size/overlap come from the YAML configuration.
        self.strategy_override = strategy_name
        self.chunk_size_override = chunk_size
        self.chunk_overlap_override = chunk_overlap

        # Optional quality hook (evaluation layer):
        # on_document(object_key, documents_list, processed_chunks) -> dict
        # returned fields are merged into the per-document record
        self.on_document = on_document

        # Per-document records are persisted to the metrics DB on every
        # ingestion (metrics are always on). The experiment runner disables
        # this (persist_metrics=False) because it persists with its own
        # experiment_id.
        self.persist_metrics = persist_metrics
        self.metrics_run_id = metrics_run_id or (
            "ingestion_" + datetime.now().strftime("%Y%m%d_%H%M%S")
        )

        # E2 metrics: per-document results (phase timings + cost counters)
        self.document_results: List[dict] = []
        # Accumulated storage time in ms (all insert_batch calls)
        self._storage_ms_total = 0.0
        # Chunker used for the last processed document (counter access)
        self.last_chunker = None
        self.last_strategy_name = None

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

                # Counter baselines (for per-document deltas).
                # Note: only the embedding client and storage counters persist
                # across documents; the strategy object is created anew for
                # each document by the LangChainChunker factory, so its cost
                # counters (llm_calls, fallbacks) are read as absolutes below.
                emb_requests_before = getattr(self.client, "http_requests", 0)
                emb_texts_before = getattr(self.client, "texts_embedded", 0)
                storage_before = self._storage_ms_total

                doc_start = time.perf_counter()

                # 3. CHUNKING (Transform) - Pass LIST OF DOCUMENTS and file metadata
                t0 = time.perf_counter()
                processed_chunks = self._transform_to_chunks(object_key, documents_list, file_metadata)
                chunking_ms = (time.perf_counter() - t0) * 1000

                # 4. EMBEDDING & BATCHING
                t0 = time.perf_counter()
                self._embed_and_queue_batch(
                    object_key, processed_chunks, batch_items)
                embedding_ms = (time.perf_counter() - t0) * 1000

                total_ms = (time.perf_counter() - doc_start) * 1000

                # Quality hook (evaluation layer): computes e.g. coverage /
                # coherence and returns fields merged into the record
                extra: dict = {}
                if self.on_document:
                    extra = self.on_document(
                        object_key, documents_list, processed_chunks
                    ) or {}

                record = {
                    "source": object_key,
                    "strategy": self.last_strategy_name,
                    "num_chunks": len(processed_chunks),
                    "chunking_ms": round(chunking_ms, 2),
                    "embedding_ms": round(embedding_ms, 2),
                    "storage_ms": round(self._storage_ms_total - storage_before, 2),
                    "total_ms": round(total_ms, 2),
                    "embedding_http_requests":
                        getattr(self.client, "http_requests", 0) - emb_requests_before,
                    "texts_embedded":
                        getattr(self.client, "texts_embedded", 0) - emb_texts_before,
                    "llm_calls":
                        self._strategy_counters()["llm_calls"],
                    "fallbacks":
                        self._strategy_counters()["fallbacks"],
                    "timestamp": datetime.now().isoformat(),
                }
                record.update(extra)
                self.document_results.append(record)

                # Metrics are always on: the per-document record
                # is stored in the metrics database (best-effort, does not block ingestion)
                if self.persist_metrics:
                    self._persist_document_record(record)

                files_processed += 1

            except Exception as e:
                logger.error("Error processing file %s: %s", object_key, e)
                continue

        if batch_items:
            t0 = time.perf_counter()
            self.store.insert_batch(batch_items)
            final_flush_ms = (time.perf_counter() - t0) * 1000
            self._storage_ms_total += final_flush_ms
            # Attribute the final flush to the last processed document
            if self.document_results:
                self.document_results[-1]["storage_ms"] = round(
                    self.document_results[-1]["storage_ms"] + final_flush_ms, 2)

        logger.info("PROCESS COMPLETE. Files processed: %d", files_processed)

    def _strategy_counters(self) -> dict:
        """Read cost counters from the last used chunking strategy (if any)."""
        strategy = getattr(getattr(self, "last_chunker", None), "last_strategy", None)
        return {
            "llm_calls": getattr(strategy, "llm_calls", 0),
            "fallbacks": getattr(strategy, "fallbacks", 0),
        }

    def _persist_document_record(self, record: dict) -> None:
        """
        Best-effort save of the per-document record to the metrics database
        (rag_chunking_metrics). A save error does not abort ingestion.
        """
        try:
            import platform
            from dataclasses import fields

            try:
                from buissnes_agent.metrics import ChunkingRunMetrics, get_repository
            except ImportError:
                from metrics import ChunkingRunMetrics, get_repository  # type: ignore

            valid = {f.name for f in fields(ChunkingRunMetrics)}
            data = {k: v for k, v in record.items() if k in valid}
            data["experiment_id"] = self.metrics_run_id
            data.setdefault("num_chunks", 0)
            data.setdefault("timestamp", datetime.now().isoformat())
            data["batch_size"] = self.batch_size
            data["force_refresh"] = self._force_refresh
            data["embedding_model"] = self.model
            data["llm_model"] = os.getenv("CHAT_MODEL")
            data["python_version"] = platform.python_version()

            get_repository().insert_chunking_metrics(ChunkingRunMetrics(**data))
        except Exception as e:
            logger.warning(
                "Nie zapisano metryk dokumentu '%s': %s",
                record.get("source"), e
            )

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
        chunk_module = settings.get("chunking.module", "langchain")

        # All files arriving here are .md (pre-converted by Project 1).
        # We read the ORIGINAL extension from metadata to select the correct
        # chunking strategy (e.g., pdf -> recursive, xlsx -> def).
        # Falls back to 'def' if original extension is not stored in metadata.
        original_ext = base_metadata.get("extension", "")
        ext = original_ext if original_ext and original_ext != ".md" else ".md"

        chunk_size, chunk_overlap, strategy = self._get_chunk_config(chunk_module, ext)

        logger.info(
            "LOGIC LAYER: LangChainChunker selected. Strategy: %s",
            strategy
        )
        chunker_engine = LangChainChunker(
            strategy, chunk_size, chunk_overlap,
            embedding_client=self.client
        )
        self.last_chunker = chunker_engine
        self.last_strategy_name = strategy
        processed_chunks = chunker_engine.process_content(documents_list)

        # Add line numbers to chunks
        self._add_line_numbers_to_chunks(processed_chunks, documents_list)

        return processed_chunks

    def _embed_and_queue_batch(
            self,
            object_key: str,
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
            try:
                vec = self.client.embed_query(text_content)
            except Exception as e:
                # Embedding outage: the chunk cannot be indexed - skip it
                # but keep the document alive so the per-document metrics
                # record is still written (texts_embedded reflects the loss)
                logger.error(
                    "Embedding failed, chunk not indexed "
                    "(%s): %s", object_key, e)
                continue

            batch_items.append({
                "text": text_content,
                "vector": vec,
                "metadata": metadata
            })

            # Check batch size and send (timed: part of storage phase)
            if len(batch_items) >= self.batch_size:
                t0 = time.perf_counter()
                self.store.insert_batch(batch_items)
                self._storage_ms_total += (time.perf_counter() - t0) * 1000
                batch_items.clear()

    def _get_chunk_config(self, module_name: str, ext: str) -> tuple[int, int, str]:
        """
        Universal method for fetching chunking configuration from the settings object.
        Replaces hardcoded match/case.

        Logic:
        0. If an explicit override was provided (experiment runner), use it.
        1. Looks for config at: chunking.strategies.{module_name}.{ext_without_dot}
        2. If not found, looks at: chunking.strategies.{module_name}.def (module fallback)
        3. Fetches parameters, filling gaps with global default values.
        """
        settings = get_settings()

        if self.strategy_override is not None:
            size = (
                self.chunk_size_override
                if self.chunk_size_override is not None
                else settings.get("chunking.default_size")
            )
            overlap = (
                self.chunk_overlap_override
                if self.chunk_overlap_override is not None
                else settings.get("chunking.default_overlap")
            )
            return int(size), int(overlap), self.strategy_override

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

        strategy = ext_config.get("strategy", "recursive")

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