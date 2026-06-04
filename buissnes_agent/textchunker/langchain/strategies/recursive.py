from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from buissnes_agent.textchunker.langchain.base import ChunkingStrategy
from buissnes_agent.textchunker.langchain.strategies.line_calculator import LineNumberCalculator


class RecursiveStrategy(ChunkingStrategy):
    """
    ### Strategy 2: Recursive (Mechanical / Fallback)

    Classic text splitting method. Attempts to split by separator hierarchy:
    1. Paragraphs (\\n\\n)
    2. Lines (\\n)
    3. Sentences (.)

    **Usage:**
    Used as the main strategy (when only size matters) or as a fallback
    when other methods fail. Guarantees that a chunk will not exceed the given size.
    """

    def __init__(self, chunk_size: int, chunk_overlap: int):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split_documents(self, documents: List[Document]) -> List[Document]:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=self.chunk_size,
            chunk_overlap=self.chunk_overlap,
            separators=["\n\n", "\n", ".", " ", ""]
        )

        # split_documents splits text while preserving page number (metadata)
        raw_chunks = text_splitter.split_documents(documents)

        # Add line numbers to all chunks
        LineNumberCalculator.add_line_numbers_to_chunks(
            raw_chunks,
            documents,
            sequential=True
        )

        return raw_chunks