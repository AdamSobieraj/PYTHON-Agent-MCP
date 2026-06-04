import logging
from typing import List
from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker

from buissnes_agent.EmbeddingClient import LocalEmbeddingClient
from buissnes_agent.textchunker.langchain.base import ChunkingStrategy
from buissnes_agent.textchunker.langchain.strategies.line_calculator import LineNumberCalculator

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

            # Add line numbers to all chunks using LineNumberCalculator
            LineNumberCalculator.add_line_numbers_to_chunks(
                raw_chunks,
                documents,
                sequential=True
            )

            return raw_chunks

        except Exception as e:
            logger.error("SemanticStrategy: Error during semantic split: %s", e)
            raise e