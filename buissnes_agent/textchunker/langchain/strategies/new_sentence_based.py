import re
from typing import List, Optional

from langchain_core.documents import Document

from buissnes_agent.textchunker.langchain.base import ChunkingStrategy
from buissnes_agent.textchunker.langchain.strategies.line_calculator import LineNumberCalculator


class NewSentenceBasedStrategy(ChunkingStrategy):
    """
    ### Strategy 6: Sentence Based (Boundary-aware / Low-cost)

    Splits text on sentence boundaries and greedily packs whole sentences
    into chunks of at most `chunk_size` characters.

    **How it works:**
    1. Detects sentence units:
       - sentence-ending punctuation (.!?…), optionally followed by a closing
         quote/bracket, when the next word starts with an uppercase letter
         (any Unicode alphabet, e.g. Polish "Ł", "Ż"), a digit, a quote or
         a bracket
       - every line break (markdown lines, headers, list items)
       The following do NOT end a sentence:
       - abbreviations ("e.g.", "etc.", "np.", "prof.")
       - multi-letter initials ("J.R.R.", "U.S.A.") and single letters ("A.")
       - list numbering at the start of a line ("1.", "12.")
       - "No."/"Fig."/"Vol." style abbreviations followed by a number
    2. Glues whole sentences into a chunk until `chunk_size` would be exceeded
       (never cuts inside a sentence).
    3. Applies `chunk_overlap` by carrying the trailing sentences of the
       previous chunk to the beginning of the next one.

    **Whitespace handling:**
    Whitespace that follows a sentence stays attached to the END of that
    sentence, so no chunk starts with a space or a line break. Joining all
    units back together yields the original text exactly.

    **Usage:**
    Plain text, articles, emails. Better than fixed-size splitting because it
    never breaks a word or a sentence. A single sentence longer than
    `chunk_size` is kept as its own chunk (the orchestrator's hard-limit
    enforcer trims it as a last resort). No overlap is carried across such an
    oversized sentence, because it can never fit into the overlap budget.

    **Known limitations (heuristic approach):**
    - Hard-wrapped text (e.g. extracted from PDF) is split at every line
      break, so a sentence may be cut at a wrapped line.
    - A sentence ending with a single letter ("Vitamin C. Next") or with an
      abbreviation from the list ("... and so on, etc. Next") is not split.
    """

    # Abbreviations that never end a sentence when followed by a capital letter.
    # Deliberately excludes ordinary words that often end a sentence
    # (json, xml, url, min, max, co, ...). Dotted initials such as
    # "e.g", "i.e", "w.r.t", "U.S.A" are handled by _INITIALS_RE instead.
    _ABBREVIATIONS = {
        # English
        "etc", "vs", "cf", "approx",
        "inc", "ltd", "corp", "dr", "mr", "mrs", "ms", "st", "jr", "sr", "prof",
        # Polish
        "np", "tzn", "tj", "tzw", "itd", "itp", "zob", "por", "wg", "ww",
        "ul", "al", "pl", "godz", "ok", "tys", "mln", "mld",
        "mgr", "hab", "inz", "inż", "ang", "łac",
    }

    # Abbreviations that are only abbreviations when a number follows
    # ("No. 5", "Fig. 3", "Nr 7"). Otherwise they are normal words
    # ("I said no. Then he left.").
    _NUMBER_ABBREVIATIONS = {"no", "nr", "fig", "vol", "sec", "art", "para", "annex"}

    # Boundary candidates (matched whitespace is part of the match):
    # 1. spaces/tabs after sentence-ending punctuation (optionally followed by a
    #    closing quote/bracket). Only [ \t] is used, NOT \s, so a line break
    #    is never swallowed here and is always handled by alternative 2.
    # 2. every line break
    # Whether the NEXT word may start a sentence is verified in code
    # (str.isupper), which works for every alphabet, not only ASCII.
    _BOUNDARY_RE = re.compile(
        r'(?:(?<=[.!?…])|(?<=[.!?…]["\'”)\]]))[ \t]+(?=\S)|\n'
    )

    # Last word-like token before the boundary (Unicode letters, digits, dots, dashes)
    _TOKEN_RE = re.compile(r'[^\W\d_][\w.\-]*$')
    # Dotted initials: "e.g", "i.e", "j.r.r", "u.s.a"
    _INITIALS_RE = re.compile(r'(?:[^\W\d_]\.)+[^\W\d_]')
    # Line prefix that is only list numbering: "1.", "  12."
    _LIST_MARKER_RE = re.compile(r'\s*\d+\.')
    # Characters (besides uppercase letters/digits) that may open a sentence
    _SENTENCE_OPENERS = set('"\'„“”([{')

    # How many characters before a boundary are inspected for the last token.
    # Keeps the check O(1) per boundary instead of O(n).
    _TOKEN_WINDOW = 40

    def __init__(self, chunk_size: int, chunk_overlap: int, strip_chunks: bool = True):
        """
        :param chunk_size: max chunk length in characters (<= 0 disables the limit,
                           the whole document becomes one chunk).
        :param chunk_overlap: max number of characters carried over from the end of
                              the previous chunk (whole sentences only).
        :param strip_chunks: strip leading/trailing whitespace of every chunk.
                             Chunks remain exact substrings of the source text.
        """
        if chunk_overlap < 0:
            raise ValueError("chunk_overlap must be >= 0")
        if chunk_size > 0 and chunk_overlap >= chunk_size:
            raise ValueError("chunk_overlap must be smaller than chunk_size")

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.strip_chunks = strip_chunks

    # ------------------------------------------------------------------
    # INTERFACE (ChunkingStrategy)
    # ------------------------------------------------------------------
    def split_documents(self, documents: List[Document]) -> List[Document]:
        final_chunks: List[Document] = []

        for doc in documents:
            text = doc.page_content
            if not text or not text.strip():
                continue

            units = self.split_into_sentence_units(text)
            for chunk_text in self.group_units(units):
                if self.strip_chunks:
                    chunk_text = chunk_text.strip()
                if not chunk_text:
                    continue

                # Copy page metadata (e.g., page_number) to generated chunks
                final_chunks.append(Document(
                    page_content=chunk_text,
                    metadata=dict(doc.metadata)
                ))

        # Add line numbers to all chunks
        LineNumberCalculator.add_line_numbers_to_chunks(
            final_chunks,
            documents,
            sequential=True
        )

        return final_chunks

    # ------------------------------------------------------------------
    # Reusable helpers (public: also used by other strategies)
    # ------------------------------------------------------------------
    def split_into_sentence_units(self, text: str) -> List[str]:
        """
        Cuts text at sentence boundaries.
        Trailing whitespace stays attached to the sentence it follows.
        Joining the returned units back together yields the original text.
        """
        raw: List[str] = []
        start = 0

        for match in self._BOUNDARY_RE.finditer(text):
            if self._is_valid_boundary(text, match):
                raw.append(text[start:match.end()])
                start = match.end()

        raw.append(text[start:])

        # Merge whitespace-only pieces (e.g. blank lines) into the neighbouring
        # unit, so every unit contains real text.
        units: List[str] = []
        pending = ""  # leading whitespace-only piece, attached to the first unit
        for seg in raw:
            if not seg:
                continue
            if not seg.strip():
                if units:
                    units[-1] += seg
                else:
                    pending += seg
            else:
                units.append(pending + seg)
                pending = ""

        if pending:  # text consists of whitespace only
            units.append(pending)

        return units

    def _is_valid_boundary(self, text: str, match: "re.Match[str]") -> bool:
        """
        Decides whether a boundary candidate is a real sentence end.

        A line break is always a valid boundary. A punctuation boundary is
        rejected when:
        - the next character cannot start a sentence (e.g. lowercase letter),
        - the line so far is only list numbering ("1."),
        - the last token is an abbreviation, dotted initials, or a single letter.
        """
        pos = match.start()
        if text[pos] == "\n":
            return True

        # 1. Next character must look like a sentence start (any alphabet)
        nxt = text[match.end()] if match.end() < len(text) else ""
        if not (nxt.isupper() or nxt.isdigit() or nxt in self._SENTENCE_OPENERS):
            return False

        # 2. List numbering at the start of the line: "1. Item"
        line_start = text.rfind("\n", 0, pos) + 1
        if self._LIST_MARKER_RE.fullmatch(text, line_start, pos):
            return False

        # 3. Inspect the last token (bounded window -> no O(n^2) behaviour)
        token_match = self._TOKEN_RE.search(text, max(0, pos - self._TOKEN_WINDOW), pos)
        if not token_match:
            return True

        token = token_match.group(0).rstrip('.-').lower()
        if not token:
            return True
        if len(token) <= 1:                      # single-letter initial: "A."
            return False
        if self._INITIALS_RE.fullmatch(token):   # "e.g", "J.R.R", "U.S.A"
            return False
        if token in self._ABBREVIATIONS:
            return False
        if token in self._NUMBER_ABBREVIATIONS and nxt.isdigit():
            return False                         # "No. 5", "Fig. 3"

        return True

    def group_units(self, units: List[str]) -> List[str]:
        """
        Greedily packs sentence units into chunks of at most `chunk_size`
        characters, carrying trailing sentences into the next chunk as overlap.
        """
        if not units:
            return []

        # No size limit configured -> the whole text is a single chunk
        if self.chunk_size <= 0:
            return ["".join(units)]

        chunks: List[str] = []
        current: List[str] = []
        current_len = 0
        last_units: List[str] = []

        for unit in units:
            unit_len = len(unit)

            # A single unit that already reaches the limit becomes its own chunk
            # (the orchestrator's hard-limit enforcer trims it if needed).
            # No overlap is carried across it: it cannot fit into the budget.
            if unit_len >= self.chunk_size:
                if current:
                    chunks.append("".join(current))
                    current, current_len = [], 0
                chunks.append(unit)
                last_units = [unit]
                continue

            if current and current_len + unit_len > self.chunk_size:
                # Close the current chunk and start a new one
                chunks.append("".join(current))
                last_units = current
                current, current_len = [], 0

                # Overlap: carry trailing sentences of the previous chunk
                # (bounded by the overlap AND by the remaining space in the new chunk)
                budget = min(self.chunk_overlap, self.chunk_size - unit_len)
                if budget > 0:
                    carried: List[str] = []
                    carried_len = 0
                    for prev in reversed(last_units):
                        if carried_len + len(prev) > budget:
                            break
                        carried.append(prev)
                        carried_len += len(prev)
                    current = list(reversed(carried))
                    current_len = carried_len

            current.append(unit)
            current_len += unit_len

        if current:
            chunks.append("".join(current))

        return chunks