import logging
import os
import tempfile
from typing import List
from langchain_core.documents import Document

from buissnes_agent.textchunker.langchain.base import ChunkingStrategy

logger = logging.getLogger(__name__)


class UnstructuredStrategy(ChunkingStrategy):
    """
    ### Strategy 3: Unstructured Library

    Uses an external library for intelligent Markdown parsing.
    Can recognize lists, tables and footers better than plain regex.

    **Resource management:**
    The `unstructured` library operates on files on disk. This class encapsulates (hides)
    all logic for creating and deleting temporary files (tempfile).

    **Modes:**
    - 'single': Entire text as one element (with cleaned formatting).
    - 'elements': Splits into logical elements (Title, NarrativeText, ListItem).
    """

    def __init__(self, mode: str = "single"):
        self.mode = mode

    def split_documents(self, documents: List[Document]) -> List[Document]:
        try:
            from langchain_community.document_loaders import UnstructuredMarkdownLoader
        except ImportError:
            raise ImportError(
                "Missing unstructured. Run: pip install unstructured markdown"
            )

        final_chunks = []
        suffix = ".md"

        # Process EACH PAGE (Document) separately to assign its number to the result
        for doc in documents:
            page_line_start = doc.metadata.get("document_line_start", 1)
            page_text = doc.page_content

            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
                temp_file.write(page_text.encode("utf-8"))
                temp_file_path = temp_file.name

            try:
                loader = UnstructuredMarkdownLoader(temp_file_path, mode=self.mode)
                unstructured_docs = loader.load()

                for u_doc in unstructured_docs:
                    # Add page metadata (e.g., page number) to generated chunks
                    u_doc.metadata.update(doc.metadata)

                    # Calculate md_start_line and md_end_line for this chunk
                    chunk_text = u_doc.page_content
                    chunk_position = page_text.find(chunk_text)

                    if chunk_position == -1:
                        # Fallback - chunk not found, use page range
                        u_doc.metadata["md_start_line"] = page_line_start
                        u_doc.metadata["md_end_line"] = page_line_start + page_text.count('\n')
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

                        u_doc.metadata["md_start_line"] = chunk_line_start
                        u_doc.metadata["md_end_line"] = chunk_line_end

                    final_chunks.append(u_doc)

            except Exception as e:
                logger.error("Error during Unstructured processing: %s", e)
            finally:
                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)

        return final_chunks