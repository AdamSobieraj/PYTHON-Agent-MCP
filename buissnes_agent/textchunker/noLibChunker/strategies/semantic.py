import logging
from typing import List, Dict, Any

from ..base import BaseNoLibStrategy

logger = logging.getLogger(__name__)


class SemanticStrategy(BaseNoLibStrategy):
    """
    ### Strategy 4: Semantic Chunker (LangChain Wrapper)

    This is the only strategy in the NoLib package that actually uses a library (LangChain).
    It was placed here to maintain compatibility with the original `NoLibChunker` code.

    **Error handling:**
    If the `langchain_experimental` library is not installed or an embedding
    configuration error occurs, the class will log the error and return
    the text as a single chunk.
    """

    def __init__(self, chunk_size: int, chunk_overlap: int):
        super().__init__(chunk_size, chunk_overlap)
        self.splitter = None

        try:
            # Conditional import - only if strategy is used
            from langchain_experimental.text_splitter import SemanticChunker
            from buissnes_agent.embeddings.local_client import LocalEmbeddingClient

            # Initialize client (fetches URL and Key from .env automatically)
            embeddings = LocalEmbeddingClient()

            logger.info("SemanticStrategy: Using EmbeddingClient (Bypass OpenAI API).")

            # Initialize splitter
            self.splitter = SemanticChunker(
                embeddings,
                breakpoint_threshold_type="percentile",
            )

        except ImportError as e:
            logger.error("Missing required libraries for SemanticStrategy: %s", e)
            logger.warning("Install: langchain_experimental and requests")
        except Exception as e:
            logger.error("SemanticStrategy initialization error: %s", e)

    def split_text(self, text: str) -> List[str]:
        if not self.splitter:
            logger.warning(
                "Semantic splitter was not initialized (error in __init__). "
                "Returning text unchanged."
            )
            return [text]

        try:
            # SemanticChunker returns Document objects
            docs = self.splitter.create_documents([text])

            # NoLibChunker expects a simple list of strings, so we map the result
            return [doc.page_content for doc in docs]

        except Exception as e:
            logger.error("Error during semantic text splitting: %s", e)
            # Fallback in case of embedding API failure
            return [text]

    def split_text_with_lines(self, text: str, page_line_start: int = 1) -> List[Dict[str, Any]]:
        """
        Extended version of split_text that also calculates
        md_start_line and md_end_line for each chunk.

        Args:
            text: Text to split
            page_line_start: Line number where the parent page starts in markdown

        Returns:
            List of dicts with 'text', 'md_start_line', 'md_end_line'
        """
        chunks = self.split_text(text)

        results = []
        last_position = 0

        for chunk_text in chunks:
            chunk_position = text.find(chunk_text, last_position)

            if chunk_position == -1:
                # Fallback - chunk not found, use last position
                chunk_position = last_position

            # Count lines before this chunk
            lines_before = text[:chunk_position].count('\n')

            # Count lines in this chunk
            lines_in_chunk = chunk_text.count('\n')

            chunk_line_start = page_line_start + lines_before
            chunk_line_end = chunk_line_start + lines_in_chunk

            # If chunk has content and does not end with \n, it occupies one more line
            if chunk_text and not chunk_text.endswith('\n'):
                chunk_line_end += 1

            results.append({
                "text": chunk_text,
                "md_start_line": chunk_line_start,
                "md_end_line": chunk_line_end
            })

            last_position = chunk_position + len(chunk_text)

        return results