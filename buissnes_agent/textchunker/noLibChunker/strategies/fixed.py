from typing import List, Dict, Any
from ..base import BaseNoLibStrategy


class FixedStrategy(BaseNoLibStrategy):
    """
    ### Strategy 1: Fixed Size

    **How it works:**
    Iterates over the text and cuts fragments of fixed length (e.g., 600 characters),
    sliding the window by (chunk_size - chunk_overlap).

    **Usage:**
    Binary files, hex, base64 or very "dirty" data where splitting by sentences
    makes no sense or is impossible.

    **Disadvantage:**
    Cuts words in half, which may make it harder for LLM to understand.

    **Implementation:**
    This strategy calculates overlap mathematically in a `while` loop,
    so it does not use the `_apply_overlap` helper method.
    """

    def split_text(self, text: str) -> List[str]:
        chunks = []
        start = 0

        # Calculate window sliding step
        step = self.chunk_size - self.chunk_overlap
        if step <= 0:
            step = self.chunk_size  # Guard against infinite loop

        while start < len(text):
            end = start + self.chunk_size
            chunks.append(text[start:end])
            start += step

        return chunks

    def split_text_with_lines(self, text: str, page_line_start: int = 1) -> List[Dict[str, Any]]:
        """
        Extended version of split_text that also calculates
        md_start_line and md_end_line for each chunk.

        Args:
            text: Text to split
            page_line_start: Line number where the parent page starts in markdown

        Returns:
            List of dicts with 'text', 'md_start_line', 'md_end_line'
        """
        results = []
        start = 0

        step = self.chunk_size - self.chunk_overlap
        if step <= 0:
            step = self.chunk_size

        while start < len(text):
            end = start + self.chunk_size
            chunk_text = text[start:end]

            # Count lines before this chunk
            lines_before = text[:start].count('\n')

            # Count lines in this chunk
            lines_in_chunk = chunk_text.count('\n')

            chunk_line_start = page_line_start + lines_before
            chunk_line_end = chunk_line_start + lines_in_chunk

            # If chunk has content and does not end with \n, it occupies one more line
            if chunk_text and not chunk_text.endswith('\n'):
                chunk_line_end += 1

            results.append({
                "text": chunk_text,
                "md_start_line": chunk_line_start,
                "md_end_line": chunk_line_end
            })

            start += step

        return results