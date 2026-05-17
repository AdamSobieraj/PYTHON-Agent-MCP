import logging
from typing import List
from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker

from buissnes_agent.EmbeddingClient import LocalEmbeddingClient
from buissnes_agent.textchunker.langchain.base import ChunkingStrategy

logger = logging.getLogger(__name__)


class SemanticStrategy(ChunkingStrategy):
    """
    ### Strategy 4: Semantic Chunking (Meaning-based / AI)

    The most advanced method. Does not look at newline characters or headers.
    Analyzes sentence vectors (embeddings).

    **How it works:**
    1. Converts sentences into numbers (vectors).
    2. Calculates similarity between adjacent sentences.
    3. If similarity drops below a threshold (breakpoint threshold),
       it recognizes a topic change and makes a cut.
    """

    def __init__(self):
        # Initialize the embeddings client
        try:
            self.embeddings = LocalEmbeddingClient()
            logger.info("SemanticStrategy: Initialized EmbeddingClient successfully.")
        except Exception as e:
            logger.error("SemanticStrategy: Failed to initialize embeddings. Error: %s", e)
            raise e

    def split_documents(self, documents: List[Document]) -> List[Document]:
        """
        Splits text into semantic fragments.
        """
        if not self.embeddings:
            raise ValueError("Embeddings not initialized.")

        text_splitter = SemanticChunker(
            self.embeddings,
            breakpoint_threshold_type="percentile",
            breakpoint_threshold_amount=95.0,
            min_chunk_size=200
        )

        try:
            # SemanticChunker also supports split_documents and metadata inheritance
            raw_chunks = text_splitter.split_documents(documents)

            # Calculate md_start_line and md_end_line for each chunk
            for chunk in raw_chunks:
                page_line_start = chunk.metadata.get("document_line_start", 1)

                # Find parent document to locate chunk position in original text
                chunk_text = chunk.page_content
                parent_doc = next(
                    (doc for doc in documents
                     if doc.metadata.get("page_number") == chunk.metadata.get("page_number")),
                    None
                )

                if parent_doc is None:
                    chunk.metadata["md_start_line"] = page_line_start
                    chunk.metadata["md_end_line"] = page_line_start
                    continue

                page_text = parent_doc.page_content
                chunk_position = page_text.find(chunk_text)

                if chunk_position == -1:
                    # Fallback - chunk not found, use page range
                    chunk.metadata["md_start_line"] = page_line_start
                    chunk.metadata["md_end_line"] = page_line_start + page_text.count('\n')
                else:
                    # Count lines before chunk within the page
                    lines_before = page_text[:chunk_position].count('\n')

                    # Count lines in chunk
                    lines_in_chunk = chunk_text.count('\n')

                    chunk_line_start = page_line_start + lines_before
                    chunk_line_end = chunk_line_start + lines_in_chunk

                    # If chunk has content and does not end with \n, it occupies one more line
                    if chunk_text and not chunk_text.endswith('\n'):
                        chunk_line_end += 1

                    chunk.metadata["md_start_line"] = chunk_line_start
                    chunk.metadata["md_end_line"] = chunk_line_end

            return raw_chunks

        except Exception as e:
            logger.error("SemanticStrategy: Error during semantic split: %s", e)
            raise e