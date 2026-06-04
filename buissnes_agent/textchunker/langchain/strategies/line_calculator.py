from typing import List, Optional
from langchain_core.documents import Document


class LineNumberCalculator:
    """
    Utility class for calculating line numbers (md_start_line, md_end_line)
    for chunks based on their position in the original document.

    Handles edge cases where chunk text might not be found exactly in the original text
    due to text processing/normalization by splitters.
    """

    @staticmethod
    def calculate_line_numbers(
            chunk: Document,
            parent_text: str,
            parent_line_start: int,
            current_position: int = 0
    ) -> tuple[int, int, int]:
        """
        Calculate start and end line numbers for a chunk.

        Args:
            chunk: The chunk document to calculate line numbers for
            parent_text: The original/parent document text
            parent_line_start: Starting line number of the parent document
            current_position: Current search position in parent_text (for sequential processing)

        Returns:
            tuple: (chunk_line_start, chunk_line_end, new_position)
                  new_position is updated position for next chunk in sequence
        """
        chunk_text = chunk.page_content

        # Try to find chunk in parent text from current position
        chunk_position = parent_text.find(chunk_text, current_position)

        if chunk_position != -1:
            # Exact match found
            return LineNumberCalculator._calculate_from_exact_match(
                chunk_text, parent_text, chunk_position, parent_line_start
            )
        else:
            # Exact match not found - try fuzzy matching by first non-empty line
            return LineNumberCalculator._calculate_from_fuzzy_match(
                chunk_text, parent_text, parent_line_start, current_position
            )

    @staticmethod
    def _calculate_from_exact_match(
            chunk_text: str,
            parent_text: str,
            chunk_position: int,
            parent_line_start: int
    ) -> tuple[int, int, int]:
        """Calculate line numbers when exact text match is found."""
        lines_before = parent_text[:chunk_position].count('\n')
        lines_in_chunk = chunk_text.count('\n')

        chunk_line_start = parent_line_start + lines_before
        chunk_line_end = chunk_line_start + lines_in_chunk

        # If chunk doesn't end with \n, it occupies one more line
        if chunk_text and not chunk_text.endswith('\n'):
            chunk_line_end += 1

        new_position = chunk_position + len(chunk_text)

        return chunk_line_start, chunk_line_end, new_position

    @staticmethod
    def _calculate_from_fuzzy_match(
            chunk_text: str,
            parent_text: str,
            parent_line_start: int,
            current_position: int
    ) -> tuple[int, int, int]:
        """
        Calculate line numbers using fuzzy matching when exact match fails.
        Searches for first non-empty line of chunk in parent text.
        """
        chunk_lines = [line for line in chunk_text.split('\n') if line.strip()]

        if not chunk_lines:
            # Empty chunk - return fallback
            return parent_line_start, parent_line_start, current_position

        first_line = chunk_lines[0].strip()
        remaining_text = parent_text[current_position:]

        # Search for matching line in remaining parent text
        for i, line in enumerate(remaining_text.split('\n')):
            if first_line in line:
                # Found matching line
                lines_before = parent_text[:current_position].count('\n') + i
                lines_in_chunk = chunk_text.count('\n')

                chunk_line_start = parent_line_start + lines_before
                chunk_line_end = chunk_line_start + lines_in_chunk

                if chunk_text and not chunk_text.endswith('\n'):
                    chunk_line_end += 1

                # Calculate new position (approximate)
                lines_to_skip = lines_in_chunk + 1
                new_position = current_position + sum(
                    len(l) + 1 for l in remaining_text.split('\n')[:lines_to_skip]
                )

                return chunk_line_start, chunk_line_end, new_position

        # Fallback - couldn't find match
        return (
            parent_line_start,
            parent_line_start + parent_text.count('\n'),
            current_position
        )

    @staticmethod
    def add_line_numbers_to_chunks(
            chunks: List[Document],
            parent_documents: List[Document],
            sequential: bool = True
    ) -> List[Document]:
        """
        Add md_start_line and md_end_line metadata to all chunks.

        Args:
            chunks: List of chunk documents
            parent_documents: List of original/parent documents
            sequential: If True, process chunks sequentially tracking position.
                       If False, search independently for each chunk.

        Returns:
            List of chunks with added line number metadata
        """
        # Create lookup dict for parent documents by page_number
        parent_lookup = {
            doc.metadata.get("page_number"): doc
            for doc in parent_documents
        }

        # Track position per parent document
        position_tracker = {}

        for chunk in chunks:
            page_number = chunk.metadata.get("page_number")
            parent_doc = parent_lookup.get(page_number)

            if parent_doc is None:
                # No parent found - use fallback
                page_line_start = chunk.metadata.get("document_line_start", 1)
                chunk.metadata["md_start_line"] = page_line_start
                chunk.metadata["md_end_line"] = page_line_start
                continue

            page_line_start = parent_doc.metadata.get("document_line_start", 1)
            parent_text = parent_doc.page_content

            # Get current position for this parent document
            if sequential:
                current_position = position_tracker.get(page_number, 0)
            else:
                current_position = 0

            # Calculate line numbers
            chunk_line_start, chunk_line_end, new_position = (
                LineNumberCalculator.calculate_line_numbers(
                    chunk, parent_text, page_line_start, current_position
                )
            )

            chunk.metadata["md_start_line"] = chunk_line_start
            chunk.metadata["md_end_line"] = chunk_line_end

            # Update position tracker
            if sequential:
                position_tracker[page_number] = new_position

        return chunks