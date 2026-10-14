"""
Chunking quality metrics (E1) — definitions from chapter 4:
- number of chunks,
- average / maximum chunk length,
- percentage of chunks exceeding the limit,
- content coverage,
- semantic coherence (formula def:semantic_coherence),
- number of empty or too-short chunks.
"""
import math
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional

from buissnes_agent.textchunker.langchain.strategies.new_sentence_based import (
    NewSentenceBasedStrategy,
)

# Shared, unlimited sentence splitter (used only for
# split_into_sentence_units).
_SENTENCE_SPLITER = NewSentenceBasedStrategy(chunk_size=0, chunk_overlap=0)


@dataclass
class ChunkingQuality:
    """Result of the quality metrics computation for one document."""
    num_chunks: int
    avg_chunk_len: float
    max_chunk_len: int
    empty_chunks: int
    too_short_chunks: int
    over_limit_chunks: int
    over_limit_ratio: float
    coverage: float
    # None: coherence cannot be computed (no embeddings
    # or no chunks with >1 sentence)
    coherence: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


def _normalize(vec: List[float]) -> List[float]:
    norm = math.sqrt(sum(x * x for x in vec))
    if norm == 0:
        return list(vec)
    return [x / norm for x in vec]


def _cosine(a: List[float], b: List[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def _chunk_coherence(vecs: List[List[float]]) -> float:
    """
    Semantic coherence of a chunk (def:semantic_coherence):
    average cosine similarity between sentence embeddings.
    Vectors must be normalized (cosine = dot product).
    """
    total = 0.0
    count = 0
    for i in range(len(vecs)):
        for j in range(i + 1, len(vecs)):
            total += _cosine(vecs[i], vecs[j])
            count += 1
    return total / count if count else 0.0


def _normalized(text: str) -> str:
    """Whitespace normalization for comparisons (coverage)."""
    return " ".join(text.split())


def compute_chunk_metrics(
        chunks: List[Dict[str, Any]],
        source_text: str,
        chunk_size: int = 0,
        min_chunk_len: int = 50,
        embeddings=None
) -> ChunkingQuality:
    """
    Computes chunking quality metrics for one document.

    Args:
        chunks: list of dictionaries with a "text" key
                (result of LangChainChunker.process_content)
        source_text: content of the source document
        chunk_size: size limit (0 = no limit)
        min_chunk_len: threshold for a "too short" chunk
        embeddings: embedding client for semantic coherence
                    (None -> coherence = None)
    """
    texts = [(c.get("text") or "") for c in chunks]
    lengths = [len(t) for t in texts]

    num_chunks = len(texts)
    avg_chunk_len = (sum(lengths) / num_chunks) if num_chunks else 0.0
    max_chunk_len = max(lengths) if lengths else 0

    empty_chunks = sum(1 for t in texts if not t.strip())
    too_short_chunks = sum(1 for L in lengths if 0 < L < min_chunk_len)

    if chunk_size > 0:
        over_limit_chunks = sum(1 for L in lengths if L > chunk_size)
        over_limit_ratio = (over_limit_chunks / num_chunks) if num_chunks else 0.0
    else:
        over_limit_chunks = 0
        over_limit_ratio = 0.0

    # Content coverage: fraction of source sentences present
    # in the joined chunk content (whitespace-insensitive).
    units = _SENTENCE_SPLITER.split_into_sentence_units(source_text) if source_text else []
    if units:
        joined = _normalized("".join(texts))
        covered = sum(1 for u in units if _normalized(u) and _normalized(u) in joined)
        coverage = covered / len(units)
    else:
        coverage = 1.0

    # Semantic coherence (def:semantic_coherence):
    # average over chunks (with >1 sentence) of the pairwise
    # sentence-embedding similarity.
    coherence: Optional[float] = None
    if embeddings is not None:
        per_chunk_units = [
            [u for u in _SENTENCE_SPLITER.split_into_sentence_units(t) if u.strip()]
            for t in texts
        ]
        valid = [us for us in per_chunk_units if len(us) >= 2]
        if valid:
            all_units = [u for us in valid for u in us]
            vectors = [_normalize(v) for v in embeddings.embed_documents(all_units)]
            coherences = []
            idx = 0
            for us in valid:
                m = len(us)
                coherences.append(_chunk_coherence(vectors[idx:idx + m]))
                idx += m
            coherence = sum(coherences) / len(coherences)

    return ChunkingQuality(
        num_chunks=num_chunks,
        avg_chunk_len=round(avg_chunk_len, 2),
        max_chunk_len=max_chunk_len,
        empty_chunks=empty_chunks,
        too_short_chunks=too_short_chunks,
        over_limit_chunks=over_limit_chunks,
        over_limit_ratio=round(over_limit_ratio, 4),
        coverage=round(coverage, 4),
        coherence=round(coherence, 4) if coherence is not None else None,
    )
