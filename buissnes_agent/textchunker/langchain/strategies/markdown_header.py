from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter

from buissnes_agent.textchunker.langchain.base import ChunkingStrategy
from buissnes_agent.textchunker.langchain.strategies.line_calculator import LineNumberCalculator


class MarkdownHeaderStrategy(ChunkingStrategy):
    """
    ### Strategy 1: Markdown Headers (Structural)

    Splits text at markdown header occurrences (#, ##, ###).
    Ideal for well-formatted technical documentation.

    **Advantage:** Preserves the header in metadata or content, giving great context.
    **Disadvantage:** If the section under a header is empty or gigantic,
    the strategy will not fix that on its own.

    **Implementation:**
    Logic has been isolated. The class does not need external parameters (chunk_size)
    because it splits strictly by document structure.
    """

    def split_documents(self, documents: List[Document]) -> List[Document]:
        headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
        markdown_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on,
            strip_headers=False
        )

        final_chunks = []
        for doc in documents:
            # Split content of a single page (doc)
            chunks = markdown_splitter.split_text(doc.page_content)

            # Manually add page metadata to new chunks
            for chunk in chunks:
                chunk.metadata.update(doc.metadata)
                final_chunks.append(chunk)

        # Add line numbers to all chunks at once
        LineNumberCalculator.add_line_numbers_to_chunks(
            final_chunks,
            documents,
            sequential=True
        )

        return final_chunks