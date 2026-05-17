from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from buissnes_agent.textchunker.langchain.base import ChunkingStrategy


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
        # from the input document
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