import re
from typing import List, Dict, Any
from ..base import BaseNoLibStrategy


class MarkdownStrategy(BaseNoLibStrategy):
    """
    ### Strategy 3: Markdown Headers (Regex)

    **How it works:**
    Uses Regex (multiline) to find Markdown headers (#, ##, ###).
    Splits text at header occurrences.

    **Usage:**
    Technical documentation, README.md. Allows preserving logical section coherence.
    """

    def split_text(self, text: str) -> List[str]:
        # Split text using lookahead (?=...), which keeps the header in the next block
        blocks = re.split(r'(?=^#{1,3}\s)', text, flags=re.MULTILINE)
        blocks = [b.strip() for b in blocks if b.strip()]

        return self._apply_overlap(blocks)

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
        blocks = re.split(r'(?=^#{1,3}\s)', text, flags=re.MULTILINE)
        blocks = [b.strip() for b in blocks if b.strip()]
        chunks = self._apply_overlap(blocks)

        results = []
        last_position = 0

        for chunk_text in chunks:
            chunk_position = text.find(chunk_text, last_position)

            if chunk_position == -1:
                # Fallback - chunk not found, use last position
                chunk_position = last_position

            # Count lines before this chunk
            lines_before = text[:chunk_position].count('\n')

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

            last_position = chunk_position + len(chunk_text)

        return results