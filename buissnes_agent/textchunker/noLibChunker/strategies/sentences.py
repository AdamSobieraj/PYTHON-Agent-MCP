import re
from typing import List, Dict, Any
from ..base import BaseNoLibStrategy


class SentencesStrategy(BaseNoLibStrategy):
    """
    ### Strategy 2: Sentence Split

    **How it works:**
    1. Uses Regex to find sentence endings (.!?).
    2. Iterates over sentences and glues them into one chunk until `chunk_size` is exceeded.
    3. When the limit is reached, closes the chunk and starts a new one.
    4. At the end applies overlap using the inherited `_apply_overlap` method.

    **Usage:**
    Plain text, articles, emails. Much better than `fixed` because it does not cut words.
    """

    def split_text(self, text: str) -> List[str]:
        # Regex split lookbehind - splits after punctuation character
        sentences = re.split(r'(?<=[.!?])\s+', text)

        chunks, current = [], ""
        for sentence in sentences:
            # If current is not empty, we will add a space, so account for it
            needed_space = 1 if current else 0

            if len(current) + len(sentence) + needed_space <= self.chunk_size:
                if current:
                    current += " " + sentence
                else:
                    current = sentence
            else:
                # Save current chunk
                if current:
                    chunks.append(current.strip())
                # Start new chunk from current sentence
                current = sentence

        if current.strip():
            chunks.append(current.strip())

        return self._apply_overlap(chunks)

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
        chunks = self.split_text(text)

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