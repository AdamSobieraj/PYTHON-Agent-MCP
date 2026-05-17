import hashlib
import logging
import sys
from typing import List, Dict, Any

from .base import BaseNoLibStrategy
from .strategies import (
    FixedStrategy,
    SentencesStrategy,
    MarkdownStrategy,
    SemanticStrategy
)
from ...MetadataModels import ChunkMetadata

logging.basicConfig(level=logging.INFO, stream=sys.stderr, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# =========================================================
# CLASS: CHUNKER (LEGACY / BASE / NOLIB)
# =========================================================
#
# ### Architecture: Orchestrator (Context)
#
# **Responsibilities:**
# 1. **Factory / Router:** Selects the appropriate splitting strategy (_get_strategy)
#    based on configuration.
# 2. **Execution Engine:** Splits raw text into smaller fragments (chunks).
# 3. **Safety Net:** Enforces hard character limits (_enforce_limit) if the
#    logical strategy fails.
# 4. **Interface Adapter:** Transforms raw strings into the unified List[Dict] format,
#    compatible with LangChainChunker (adds UUID and metadata).
#
# **Key difference from LangChainChunker:**
# This class has no external dependencies (except optional Semantic).
# It is "lightweight", fast and runs on pure Python.
# =========================================================
class NoLibChunker:
    def __init__(self, chunk_strategy: str, chunk_size: int = 600, chunk_overlap: int = 100):
        """
        Initializes the Chunker with strategy selection and configuration.

        Args:
            chunk_strategy (str): Strategy name (e.g., 'auto', 'sentences', 'markdown').
            chunk_size (int): Maximum fragment length (in characters).
            chunk_overlap (int): Number of overlapping characters between fragments (context).
        """
        self.chunk_strategy = chunk_strategy
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

        logger.info(
            "NoLibChunker initialized. Strategy: %s, Max Chunk Size: %d, Overlap: %d",
            chunk_strategy,
            chunk_size,
            chunk_overlap
        )

    def _get_strategy(self, text: str) -> BaseNoLibStrategy:
        """
        ### Heuristic strategy selector (Router / Factory Method)

        **How it works:**
        Based on `self.chunk_strategy`, selects the appropriate class implementing
        `BaseNoLibStrategy`. For the 'auto' option, analyzes the text to make
        the decision dynamically.
        """
        # "Auto" logic - Router
        if self.chunk_strategy == "auto":
            # Analyzes the text. If it finds Markdown structure (header `# `),
            # uses the Markdown strategy.
            if "# " in text:
                return MarkdownStrategy(self.chunk_size, self.chunk_overlap)
            else:
                return SentencesStrategy(self.chunk_size, self.chunk_overlap)

        # Map names to strategy classes
        if self.chunk_strategy == "fixed":
            return FixedStrategy(self.chunk_size, self.chunk_overlap)
        elif self.chunk_strategy in ["sentences", "by_sentences"]:
            return SentencesStrategy(self.chunk_size, self.chunk_overlap)
        elif self.chunk_strategy in ["markdown", "by_markdown_headers"]:
            return MarkdownStrategy(self.chunk_size, self.chunk_overlap)
        elif self.chunk_strategy == "semanticChunker":
            return SemanticStrategy(self.chunk_size, self.chunk_overlap)
        else:
            # Fallback - default to sentences
            logger.warning(
                "Unknown strategy '%s', using SentencesStrategy.",
                self.chunk_strategy
            )
            return SentencesStrategy(self.chunk_size, self.chunk_overlap)

    def split_text(self, text: str) -> List[str]:
        """
        Main logical method (Low-level).
        Delegates the text splitting task to the selected strategy.
        Returns raw strings (not dictionaries).
        """
        if not text:
            return []

        strategy = self._get_strategy(text)
        return strategy.split_text(text)

    # =========================================================================
    # METHOD: process_content (Unified Interface)
    # =========================================================================
    def process_content(
            self,
            content: str,
            base_metadata: Dict[str, Any] = None
    ) -> List[Dict[str, Any]]:
        """
        ### Main Processing Pipeline

        Unifies the interface with `LangChainChunker`. Thanks to this, the rest
        of the application does not need to know which chunker it is using.

        **Process stages:**
        1. **Primary Split:** Calls the logical strategy (e.g., sentences/markdown).
        2. **Safety Net (_enforce_limit):** Checks that chunks have not exceeded
           the character limit.
        3. **Metadata Injection & Formatting:** Wraps strings in dictionaries
           and assigns UUIDs.

        Args:
            content (str): Text to split.
            base_metadata (Dict): Source file metadata (e.g., file name).
        """
        if not content:
            return []

        if base_metadata is None:
            base_metadata = {}

        # 1. Fetch raw strings from the strategy (may be too long!)
        raw_chunks: List[str] = self.split_text(content)

        # 2. Hard Limit Enforcer (Safety Net)
        # Guarantees that no chunk exceeds chunk_size.
        safe_chunks: List[str] = self._enforce_limit(raw_chunks)

        # 3. Format to unified standard (List[Dict])
        results = []
        for idx, chunk_text in enumerate(safe_chunks):

            # A. Prepare ID
            source_uri = base_metadata.get("source", "unknown")
            unique_str = f"{source_uri}_{idx}_{chunk_text[:20]}"
            chunk_id = hashlib.md5(unique_str.encode("utf-8")).hexdigest()

            # B. Separate known fields from "extra"
            # Extract known fields from the loader dict, rest goes to extra_data
            known_fields = {
                "source":               source_uri,
                "title":                base_metadata.get("title"),
                "url":                  base_metadata.get("url"),
                "extension":            base_metadata.get("extension"),
                "domain":               base_metadata.get("domain"),
                "tags":                 base_metadata.get("tags", []),
                "page_number":          base_metadata.get("page_number"),
                # Line range of the entire source page in markdown
                "document_line_start":  base_metadata.get("document_line_start"),
                "document_line_end":    base_metadata.get("document_line_end"),
                # Line range of this specific chunk in markdown  ← NEW
                "md_start_line":        base_metadata.get("md_start_line"),
                "md_end_line":          base_metadata.get("md_end_line"),
                # Original PDF page number the chunk was taken from  ← NEW
                "pdf_page":             base_metadata.get("pdf_page"),
            }

            # Everything not in known_fields goes to extras
            extras = {
                k: v for k, v in base_metadata.items()
                if k not in known_fields
            }

            # C. Instantiate Dataclass
            meta_obj = ChunkMetadata(
                source=known_fields["source"],
                phrase=chunk_text,          # Mandatory content
                phrase_metadata_id=chunk_id, # Mandatory ID

                title=known_fields["title"],
                url=known_fields["url"],
                extension=known_fields["extension"],
                domain=known_fields["domain"],
                tags=known_fields["tags"],
                page_number=known_fields["page_number"],

                # Line range of the entire source page in markdown
                document_line_start=known_fields["document_line_start"],
                document_line_end=known_fields["document_line_end"],

                # Line range of this specific chunk in markdown  ← NEW
                md_start_line=known_fields["md_start_line"],
                md_end_line=known_fields["md_end_line"],

                # Original PDF page number  ← NEW
                pdf_page=known_fields["pdf_page"],

                extra_data=extras
            )

            # D. Build result
            results.append({
                "text": chunk_text,             # For embedding
                "metadata": meta_obj.to_payload()  # For database (flat dict)
            })

        return results

    def _enforce_limit(self, chunks: List[str]) -> List[str]:
        """
        ### Helper method: "Size Safety Net" (Hard Limit Enforcer - NoLib Version)

        **Goal:** Technical guarantee.
        Logical strategies (e.g., Markdown) care about context ("don't cut in the
        middle of a section"), but may ignore the character limit if the section
        is huge.

        **How it works:**
        Iterates over generated chunks. If chunk > `chunk_size`, splits it into
        smaller pieces "hard" (Fixed Size Logic).

        **Why manual implementation?**
        Unlike `LangChainChunker`, we do not import `RecursiveCharacterTextSplitter`
        here to keep the class lightweight and independent of external libraries
        (Pure Python).
        """
        final_chunks = []

        for chunk in chunks:
            if len(chunk) <= self.chunk_size:
                final_chunks.append(chunk)
            else:
                # If chunk is too large -> split in a loop (FixedStrategy logic)
                start = 0
                step = self.chunk_size - self.chunk_overlap

                # Guard against infinite loop (if overlap >= size)
                if step <= 0:
                    step = self.chunk_size

                while start < len(chunk):
                    end = start + self.chunk_size
                    # Cut out the sub-chunk
                    sub_chunk = chunk[start:end]
                    final_chunks.append(sub_chunk)

                    # Stop condition if we reached the end
                    if end >= len(chunk):
                        break

                    start += step

        return final_chunks