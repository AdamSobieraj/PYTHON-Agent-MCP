from typing import List
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter

from buissnes_agent.textchunker.langchain.base import ChunkingStrategy


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
            # Get page line start from parent document metadata
            page_line_start = doc.metadata.get("document_line_start", 1)
            page_text = doc.page_content

            # Split content of a single page (doc)
            chunks = markdown_splitter.split_text(doc.page_content)

            for chunk in chunks:
                # Manually add page metadata to new chunks
                chunk.metadata.update(doc.metadata)

                # Calculate md_start_line and md_end_line for this chunk
                chunk_text = chunk.page_content
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

                final_chunks.append(chunk)

        return final_chunks