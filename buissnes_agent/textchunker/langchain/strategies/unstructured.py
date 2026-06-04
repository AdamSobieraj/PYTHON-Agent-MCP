import logging
import os
import tempfile
from typing import List
from langchain_core.documents import Document

from buissnes_agent.textchunker.langchain.base import ChunkingStrategy
from buissnes_agent.textchunker.langchain.strategies.line_calculator import LineNumberCalculator

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
                    final_chunks.append(u_doc)

            except Exception as e:
                logger.error("Error during Unstructured processing: %s", e)
            finally:
                if os.path.exists(temp_file_path):
                    os.remove(temp_file_path)

        # Add line numbers to all chunks at once using LineNumberCalculator
        LineNumberCalculator.add_line_numbers_to_chunks(
            final_chunks,
            documents,
            sequential=True
        )

        return final_chunks