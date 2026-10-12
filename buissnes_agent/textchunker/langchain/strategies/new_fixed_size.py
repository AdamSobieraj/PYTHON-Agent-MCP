from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter

from buissnes_agent.textchunker.langchain.base import ChunkingStrategy
from buissnes_agent.textchunker.langchain.strategies.line_calculator import LineNumberCalculator


class NewFixedSizeStrategy(ChunkingStrategy):
    """
    Strategy: Fixed Size (strictly size-driven).

    Splits text into chunks of exactly `chunk_size` characters (the last chunk
    of a document may be shorter), with `chunk_overlap` characters shared
    between consecutive chunks. Cut positions ignore any text structure.
    """

    def __init__(self, chunk_size: int, chunk_overlap: int):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be > 0")
        if not 0 <= chunk_overlap < chunk_size:
            raise ValueError("chunk_overlap must be >= 0 and < chunk_size")

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self._splitter = CharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separator="",             # split per character -> strict size
            keep_separator=False,
            strip_whitespace=False,   # keep text exactly as in the source
            add_start_index=True,     # exact offset in metadata["start_index"]
        )

    def split_documents(self, documents: List[Document]) -> List[Document]:
        chunks = self._splitter.split_documents(documents)
        LineNumberCalculator.add_line_numbers_to_chunks(chunks, documents, sequential=True)
        return chunks