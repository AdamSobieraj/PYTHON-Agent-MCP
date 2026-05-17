import hashlib
import logging
import sys
from typing import List, Dict, Any

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from buissnes_agent.textchunker.langchain.base import ChunkingStrategy
from .strategies import (
    MarkdownHeaderStrategy,
    RecursiveStrategy,
    UnstructuredStrategy,
    SemanticStrategy
)
from ...MetadataModels import ChunkMetadata

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logger = logging.getLogger(__name__)


class LangChainChunker:
    """
    ### Main Class: Orchestrator (Context)

    Responsible for transforming raw text into vectors ready for indexing.
    In the new architecture it acts as the "Context" for the Strategy pattern.

    **Responsibilities:**
    1. **Factory:** Selects the appropriate strategy class based on configuration (_get_strategy).
    2. **Orchestration:** Manages data flow (Primary Split -> Metadata -> Secondary Split).
    3. **Safety Net:** Applies the "Hard Limit Enforcer" independently of the selected strategy.

    **Key change:**
    The class no longer contains logic for "how to split text" (that is done by strategies
    in separate files), but "how to manage the splitting process".
    """

    def __init__(self, chunk_strategy: str, chunk_size: int, chunk_overlap: int):
        self.chunk_strategy = chunk_strategy
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        logger.info(
            "LangChainChunker initialized. Strategy: %s, Max Chunk Size: %d",
            chunk_strategy,
            chunk_size
        )

    def _get_strategy(self) -> ChunkingStrategy:
        """
        Factory Method.
        Maps strategy name (string) to a concrete strategy class instance.
        """
        if self.chunk_strategy == "markdownHeaderTextSplitter":
            return MarkdownHeaderStrategy()
        elif self.chunk_strategy == "unstructuredMarkdownLoaderSingle":
            return UnstructuredStrategy(mode="single")
        elif self.chunk_strategy == "unstructuredMarkdownLoaderElements":
            return UnstructuredStrategy(mode="elements")
        elif self.chunk_strategy == "semanticChunker":
            return SemanticStrategy()
        elif self.chunk_strategy == "recursive":
            return RecursiveStrategy(self.chunk_size, self.chunk_overlap)
        else:
            # Fallback - if strategy unknown, use safe recursive
            logger.warning(
                "Unknown strategy '%s', utilizing recursive fallback.",
                self.chunk_strategy
            )
            return RecursiveStrategy(self.chunk_size, self.chunk_overlap)

    # =========================================================================
    # METHOD: process_content (Unified entry point)
    # =========================================================================
    def process_content(self, documents: List[Document]) -> List[Dict[str, Any]]:
        """
        Returns a list of dictionaries ready for vectorization and storage in the database.
        Structure: [{"text": "...", "metadata": {"page_number": 1, ...}}]

        ### Main Processing Pipeline

        Combines the selected splitting strategy with limit management.

        **Process stages:**
        1. **Primary Split (Delegation):** Delegates splitting to the specialized strategy class.
        2. **Metadata Cleanup:** Unification of metadata keys.
        3. **Secondary Split (Hard Limit Enforcer):** Checks whether logical chunks are not too large.
        4. **Formatting:** Assigns unique IDs and returns dictionary structure.
        """

        if not documents:
            return []

        # Step 1: Select strategy and execute split (Primary Split)
        strategy = self._get_strategy()
        splits: List[Document] = strategy.split_documents(documents)

        # Step 2: Smart Metadata Cleanup
        # Since file metadata was already merged in the Orchestrator, here we only
        # fix key names if needed (e.g., LangChain sometimes creates key "page" instead of "page_number").
        for doc in splits:
            if "page" in doc.metadata:
                if doc.metadata.get("page_number") is None:
                    doc.metadata["page_number"] = doc.metadata.pop("page")
                else:
                    doc.metadata.pop("page")  # Remove any duplicate

        # Step 3: Secondary Split (Hard Limit / Safety Net)
        # Logical strategies (Header/Semantic) may return a 5000-char chunk if the chapter was long.
        # _enforce_limit splits it into smaller pieces while preserving metadata.
        final_documents = splits
        if self.chunk_size > 0:
            final_documents = self._enforce_limit(splits)

        # Step 4: Format output
        results = []
        for idx, doc in enumerate(final_documents):

            # A. Fetch data from merged document metadata
            meta_dict = doc.metadata
            source_uri = meta_dict.get("source", "unknown")

            # B. Generate ID
            content_snippet = doc.page_content[:50]
            unique_str = f"{source_uri}_{idx}_{content_snippet}"
            chunk_id = hashlib.md5(unique_str.encode("utf-8")).hexdigest()

            # C. Separate known fields from "extra"
            # Define which keys map directly onto the dataclass fields
            known_keys = {
                "source",
                "title",
                "url",
                "extension",
                "domain",
                "tags",
                "page_number",
                # Line range of the entire source page in markdown
                "document_line_start",
                "document_line_end",
                # Line range of this specific chunk in markdown  ← NEW
                "md_start_line",
                "md_end_line",
                # Original PDF page number the chunk was taken from  ← NEW
                "pdf_page",
            }

            # Extract known fields
            schema_data = {k: meta_dict.get(k) for k in known_keys}

            # Set default source if empty
            if not schema_data["source"]:
                schema_data["source"] = "unknown"

            # Everything else goes into extras (e.g., PDF-specific metadata)
            # Skip technical keys that we generate ourselves or are noise
            exclude_keys = known_keys | {
                "phrase",
                "phrase_metadata_id",
                "_chunk_id",
                "loc",
                # Old field names - excluded to avoid duplicates in payload
                "embedding_line_start",
                "embedding_line_end",
                "line_start",
                "line_end",
            }
            extras = {k: v for k, v in meta_dict.items() if k not in exclude_keys}

            # D. Instantiate Dataclass
            meta_obj = ChunkMetadata(
                source=schema_data["source"],
                phrase=doc.page_content,
                phrase_metadata_id=chunk_id,

                title=schema_data["title"],
                url=schema_data["url"],
                extension=schema_data["extension"],
                domain=schema_data["domain"],
                tags=schema_data["tags"] or [],
                page_number=schema_data["page_number"],

                # Line range of the entire source page in markdown
                document_line_start=schema_data["document_line_start"],
                document_line_end=schema_data["document_line_end"],

                # Line range of this specific chunk in markdown  ← NEW
                md_start_line=schema_data["md_start_line"],
                md_end_line=schema_data["md_end_line"],

                # Original PDF page number  ← NEW
                pdf_page=schema_data["pdf_page"],

                extra_data=extras
            )

            # E. Output
            results.append({
                "text": doc.page_content,
                "metadata": meta_obj.to_payload()
            })

        return results

    def _enforce_limit(self, documents: List[Document]) -> List[Document]:
        """
        ### Helper method: "Size Safety Net" (Hard Limit Enforcer)

        **Goal:** Technical guarantee.
        Logical strategies care about context ("don't cut in the middle of a sentence"),
        but may ignore the character limit.
        This method is shared across all strategies and acts as the "last line of defense".

        If a chunk is larger than `self.chunk_size`, we use "precision scissors"
        (RecursiveCharacterTextSplitter) to trim it down.
        """
        final_docs = []

        # Use Recursive as the universal trimming method
        recursive_cutter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=["\n\n", "\n", ".", " ", ""]  # Cutting hierarchy
        )

        for doc in documents:
            if len(doc.page_content) > self.chunk_size:
                # If too large -> split recursively
                # split_documents automatically copies parent metadata to children
                sub_docs = recursive_cutter.split_documents([doc])
                final_docs.extend(sub_docs)
            else:
                # If within limit -> pass through unchanged
                final_docs.append(doc)

        return final_docs