import logging
import math
from typing import List

from langchain_core.documents import Document

from buissnes_agent.EmbeddingClient import LocalEmbeddingClient
from buissnes_agent.textchunker.langchain.base import ChunkingStrategy
from buissnes_agent.textchunker.langchain.strategies.line_calculator import LineNumberCalculator
from buissnes_agent.textchunker.langchain.strategies.new_sentence_based import NewSentenceBasedStrategy

logger = logging.getLogger(__name__)


class NewSemanticStrategy(ChunkingStrategy):
    """
    ### Strategy 7: Semantic (Self-contained / Adaptive)

    Splits text at topic changes detected via sentence embeddings.
    Self-contained: sentence detection, similarity computation and
    breakpoint selection are done here in pure Python, using the
    project's local embedding client.

    **How it works:**
    1. Text is split into sentences (via NewSentenceBasedStrategy).
    2. Each sentence is embedded (LocalEmbeddingClient, batched).
    3. Cosine similarity between adjacent sentences is computed.
    4. A topic change (breakpoint) is a sentence pair whose similarity falls
       below the `breakpoint_percentile`-th percentile of the document's own
       similarity distribution. Higher percentile -> more breakpoints.
    5. Groups smaller than `min_chunk_size` are merged with the previous group.
    6. Groups larger than `chunk_size` are subdivided at sentence boundaries
       with `chunk_overlap` (semantic first, size bounded second).

    **Usage:**
    Documents with clear topic shifts (long articles, changelogs, manuals).
    Requires a running embeddings endpoint (EMBEDDING_* env vars).
    """

    def __init__(
            self,
            chunk_size: int,
            chunk_overlap: int,
            breakpoint_percentile: float = 50.0,
            min_chunk_size: int = 100,
            embeddings=None
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.breakpoint_percentile = breakpoint_percentile
        self.min_chunk_size = min_chunk_size

        # Initialize the embeddings client
        # (an external client can be injected to share cost counters)
        try:
            self.embeddings = embeddings or LocalEmbeddingClient()
            logger.info("NewSemanticStrategy: Initialized EmbeddingClient successfully.")
        except Exception as e:
            logger.error("NewSemanticStrategy: Failed to initialize embeddings. Error: %s", e)
            raise e

        # Reused: sentence detection + size-bounded regrouping with overlap
        self._sentence_strategy = NewSentenceBasedStrategy(chunk_size, chunk_overlap)

        # Cost counters (E4 metrics) - number of fallbacks to
        # deterministic sentence packing after an embedding failure
        self.fallbacks = 0

    def reset_counters(self) -> None:
        """Reset cost counters (call between documents / experiments)."""
        self.fallbacks = 0

    # ------------------------------------------------------------------
    # INTERFACE (ChunkingStrategy)
    # ------------------------------------------------------------------
    def split_documents(self, documents: List[Document]) -> List[Document]:
        if not self.embeddings:
            raise ValueError("Embeddings not initialized.")

        final_chunks: List[Document] = []

        for doc in documents:
            text = doc.page_content
            if not text or not text.strip():
                continue

            units = self._sentence_strategy.split_into_sentence_units(text)
            if not units:
                continue

            for chunk_text in self._chunk_texts(units):
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
    # Helpers
    # ------------------------------------------------------------------
    def _chunk_texts(self, units: List[str]) -> List[str]:
        """Semantic groups, then size bounding. Returns chunk texts."""
        try:
            groups = self._semantic_groups(units)
        except Exception as e:
            # Embedding endpoint failure -> deterministic sentence
            # packing fallback (ingestion is never blocked by the
            # embedding service)
            logger.warning(
                "NewSemanticStrategy: embedding failed (%s); "
                "falling back to sentence grouping", e)
            self.fallbacks += 1
            return self._sentence_strategy.group_units(units)

        result: List[str] = []
        for group in groups:
            group_text = "".join(group)
            if self.chunk_size > 0 and len(group_text) > self.chunk_size:
                # Topic too long for the limit -> subdivide at sentence
                # boundaries (whole sentences, with overlap)
                result.extend(self._sentence_strategy.group_units(group))
            else:
                result.append(group_text)
        return result

    def _semantic_groups(self, units: List[str]) -> List[List[str]]:
        """Groups sentences by detected topic changes."""
        if len(units) <= 1:
            return [units] if units else []

        vectors = self._embed_sentences(units)
        similarities = [
            self._cosine(vectors[i - 1], vectors[i])
            for i in range(1, len(vectors))
        ]

        threshold = self._percentile(similarities, self.breakpoint_percentile)

        groups: List[List[str]] = [[units[0]]]
        for i, sim in enumerate(similarities, start=1):
            if sim < threshold:
                groups.append([units[i]])
            else:
                groups[-1].append(units[i])

        # Merge groups smaller than min_chunk_size into the previous group
        if self.min_chunk_size > 0 and len(groups) > 1:
            groups = self._enforce_min_size(groups)

        return groups

    def _enforce_min_size(self, groups: List[List[str]]) -> List[List[str]]:
        """Merges too-small groups so no chunk falls below min_chunk_size."""
        merged: List[List[str]] = []
        for group in groups:
            if merged and sum(len(u) for u in group) < self.min_chunk_size:
                merged[-1].extend(group)
            else:
                merged.append(list(group))

        # A tiny first group merges with its successor instead
        if len(merged) > 1 and sum(len(u) for u in merged[0]) < self.min_chunk_size:
            merged[1] = merged[0] + merged[1]
            del merged[0]

        return merged

    def _embed_sentences(self, units: List[str]) -> List[List[float]]:
        vectors = self.embeddings.embed_documents(units)
        if len(vectors) != len(units):
            raise ValueError(
                f"Embedding mismatch: expected {len(units)} vectors, got {len(vectors)}"
            )
        return [self._normalize(v) for v in vectors]

    @staticmethod
    def _normalize(vec: List[float]) -> List[float]:
        norm = math.sqrt(sum(x * x for x in vec))
        if norm == 0:
            return vec
        return [x / norm for x in vec]

    @staticmethod
    def _cosine(a: List[float], b: List[float]) -> float:
        # Vectors are pre-normalized -> cosine is a plain dot product
        return sum(x * y for x, y in zip(a, b))

    @staticmethod
    def _percentile(values: List[float], pct: float) -> float:
        """Linear-interpolated percentile (0-100 scale)."""
        if not values:
            return 0.0
        ordered = sorted(values)
        if len(ordered) == 1:
            return ordered[0]
        k = (len(ordered) - 1) * (pct / 100.0)
        f = math.floor(k)
        c = math.ceil(k)
        if f == c:
            return ordered[int(k)]
        return ordered[f] * (c - k) + ordered[c] * (k - f)
