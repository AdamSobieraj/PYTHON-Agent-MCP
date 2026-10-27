"""
BM25 index for the sparse (keyword) leg of hybrid search.

Why in the application:
    The installed qdrant-client (1.17.1) has no built-in BM25 encoder
    (SparseVectorParams has no "encoder" field, the "Document" query
    model is WIP/unimplemented, and fastembed is not installed).
    The corpus is static, so BM25 statistics are computed once,
    after ingestion, and stored as sparse vectors on the points
    (client.update_vectors). Query-time encoding is a cheap
    token -> index lookup with term-frequency values; the server-side
    dot product reproduces the BM25 ranking because document weights
    already carry the idf factor.

Model (standard BM25):
    idf(t)     = ln(1 + (N - df(t) + 0.5) / (df(t) + 0.5))
    w(t, d)    = idf(t) * tf(t,d) * (k1 + 1)
                 / (tf(t,d) + k1 * (1 - b + b * |d| / avgdl))

The index state (vocab + parameters) is persisted as JSON next to the
project root (collections/{collection}.bm25.json) and MUST be the same
instance at ingestion time and at query time.

CLI:
    python -m buissnes_agent.Bm25Index <collection_name>
        -- scroll the collection, build the index, write sparse vectors,
        -- save the JSON file.
"""
import argparse
import json
import logging
import math
import os
import re
import sys
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Sequence, Tuple

logger = logging.getLogger(__name__)

# Project root: buissnes_agent/ is a direct child of it
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# BM25 parameters (standard values)
K1 = 1.5
B = 0.75

# Minimum token length (single characters and single digits are noise)
MIN_TOKEN_LEN = 2

_TOKEN_RE = re.compile(r"[a-z0-9]+")

# Stop words: Polish + English (the technical corpus is bilingual;
# the list is in ASCII-folded form, matching the tokenizer output)
STOPWORDS = frozenset({
    # Polish
    "a", "aby", "acz", "aczkolwiek", "albo", "ale", "ani", "az", "bo",
    "by", "byc", "byl", "byla", "bylo", "byly", "bym", "bys", "byscie",
    "cala", "caly", "co", "cokolwiek", "cos", "czesto", "czy", "czyli",
    "czesc", "dla", "do", "duzo", "fakt", "gdzie", "gdy", "gdyby", "go",
    "i", "ich", "im", "inna", "inne", "inny", "ja", "jak", "jaka",
    "jakis", "jakos", "jako", "jakze", "jasne", "je", "jednak",
    "jednakze", "jezeli", "jesli", "jeszcze", "jest", "jestem", "juz",
    "kims", "kto", "ktokolwiek", "ktora", "ktore", "ktorego", "ktory",
    "ktos", "ku", "lecz", "ma", "megi", "mi", "mimo", "moja", "moje",
    "moim", "moge", "mowiac", "musi", "musim", "musisz", "musze", "my",
    "na", "nam", "nas", "nastepnie", "natomiast", "nawet", "nigdy",
    "nim", "nie", "niech", "no", "o", "od", "ona", "one", "oni",
    "ono", "on", "po", "pod", "potem", "przez", "przed", "przy",
    "przeciez", "raczej", "rzadko", "sam", "sama", "sie", "skad",
    "tak", "taka", "takie", "taki", "tego", "tej", "temu", "tym",
    "tymi", "tych", "tylko", "tez", "to", "tutaj", "twoja", "twoj",
    "u", "w", "wam", "was", "we", "wedlug", "wlasnie", "wreszcie",
    "za", "z", "ze", "znowu",
    # English
    "an", "the", "and", "or", "but", "if", "then", "else", "of",
    "in", "on", "at", "to", "for", "with", "by", "from", "as", "is",
    "are", "was", "were", "be", "been", "being", "it", "its", "this",
    "that", "these", "those", "there", "here", "when", "where", "which",
    "who", "whom", "whose", "what", "how", "why", "not", "no", "yes",
    "can", "will", "shall", "may", "might", "must", "should", "would",
    "do", "does", "did", "have", "has", "had", "i", "you", "he", "she",
    "we", "they", "me", "him", "her", "us", "them", "my", "your", "his",
    "our", "their", "so", "such", "than", "too", "very", "just", "also",
    "any", "all", "some", "each", "both", "few", "more", "most", "other",
    "about", "into", "over", "under", "again", "further", "once", "same",
})


def tokenize(text: str) -> List[str]:
    """
    Tokenizer shared by ingestion and query time.

    NFKD-fold to ASCII, lowercase, keep [a-z0-9]+ tokens,
    drop stop words and tokens shorter than MIN_TOKEN_LEN.
    """
    if not text:
        return []
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii").lower()
    tokens = _TOKEN_RE.findall(text)
    return [t for t in tokens if len(t) >= MIN_TOKEN_LEN and t not in STOPWORDS]


class Bm25Index:
    """
    BM25 statistics for a static corpus.

    The vocab order is deterministic (alphabetical), so token indices
    are stable across rebuilds.
    """

    def __init__(self, collection: str, k1: float = K1, b: float = B):
        self.collection = collection
        self.k1 = k1
        self.b = b
        self.vocab: Dict[str, int] = {}
        self.df: List[int] = []
        self.doc_len: List[int] = []
        self.n_docs: int = 0
        self.avgdl: float = 0.0

    # ------------------------------------------------------------------
    # Building
    # ------------------------------------------------------------------
    def build(self, documents: Sequence[Tuple[str, str]]) -> None:
        """
        Build the index from (point_id, raw_text) pairs.

        The raw text is the chunk content WITHOUT the EOS suffix
        appended by the embedding client (that token would pollute
        the vocab).
        """
        # pass 1: token counts per document
        doc_token_counts: List[Dict[str, int]] = []
        df: Dict[str, int] = {}
        total_len = 0

        for _point_id, text in documents:
            tokens = tokenize(text)
            counts: Dict[str, int] = {}
            for t in tokens:
                counts[t] = counts.get(t, 0) + 1
            doc_token_counts.append(counts)
            total_len += len(tokens)
            for t in counts:
                df[t] = df.get(t, 0) + 1

        self.n_docs = len(doc_token_counts)
        self.avgdl = (total_len / self.n_docs) if self.n_docs else 0.0
        sorted_tokens = sorted(df)
        # deterministic vocab order
        self.vocab = {t: i for i, t in enumerate(sorted_tokens)}
        self.df = [df[t] for t in sorted_tokens]
        self.doc_len = [len(t) for t in doc_token_counts]
        logger.info(
            f"BM25: {self.n_docs} dokumentów, słownik {len(self.vocab)} tokenów, "
            f"avgdl={self.avgdl:.2f}"
        )

    # ------------------------------------------------------------------
    # Scoring
    # ------------------------------------------------------------------
    def idf(self, token: str) -> float:
        idx = self.vocab.get(token)
        if idx is None:
            return 0.0
        d = self.df[idx]
        return math.log(1.0 + (self.n_docs - d + 0.5) / (d + 0.5))

    def point_weights(self, text: str) -> Tuple[List[int], List[float]]:
        """
        Sparse vector for one document: BM25 weights per token.
        """
        tokens = tokenize(text)
        if not tokens:
            return [], []
        counts: Dict[str, int] = {}
        for t in tokens:
            if t in self.vocab:
                counts[t] = counts.get(t, 0) + 1
        if not counts:
            return [], []
        dl = len(tokens)
        denom_factor = 1.0 - self.b + self.b * (dl / self.avgdl if self.avgdl else 1.0)
        indices: List[int] = []
        values: List[float] = []
        for t, tf in sorted(counts.items()):
            w = self.idf(t) * (tf * (self.k1 + 1.0)) / (tf + self.k1 * denom_factor)
            if w > 0.0:
                indices.append(self.vocab[t])
                values.append(round(w, 6))
        return indices, values

    def encode_query(self, text: str) -> Tuple[List[int], List[float]]:
        """
        Sparse query vector: token indices + term frequencies in the
        query (values = tf). Unknown tokens are dropped.
        """
        tokens = tokenize(text)
        counts: Dict[str, int] = {}
        for t in tokens:
            if t in self.vocab:
                counts[t] = counts.get(t, 0) + 1
        if not counts:
            return [], []
        indices: List[int] = []
        values: List[float] = []
        for t, tf in sorted(counts.items()):
            indices.append(self.vocab[t])
            values.append(float(tf))
        return indices, values

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------
    def to_dict(self) -> Dict:
        return {
            "collection": self.collection,
            "created_at": datetime.now().isoformat(),
            "n_docs": self.n_docs,
            "avgdl": self.avgdl,
            "k1": self.k1,
            "b": self.b,
            "vocab": self.vocab,
        }

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(self.to_dict(), f, ensure_ascii=False, indent=1)
        logger.info(f"BM25: zapisano indeks: {path}")

    @classmethod
    def from_dict(cls, data: Dict) -> "Bm25Index":
        idx = cls(data.get("collection", ""), k1=data.get("k1", K1), b=data.get("b", B))
        idx.vocab = {t: int(i) for t, i in data.get("vocab", {}).items()}
        idx.n_docs = int(data.get("n_docs", 0))
        idx.avgdl = float(data.get("avgdl", 0.0))
        # df is not needed at query time (idf is baked into point weights)
        return idx

    @classmethod
    def load(cls, path: Path) -> Optional["Bm25Index"]:
        try:
            with open(path, "r", encoding="utf-8") as f:
                return cls.from_dict(json.load(f))
        except FileNotFoundError:
            return None
        except Exception as e:
            logger.error(f"BM25: błąd odczytu indeksu {path}: {e}")
            return None


def index_path_for(collection_name: str) -> Path:
    """Where the index JSON for a collection lives."""
    return PROJECT_ROOT / "collections" / f"{collection_name}.bm25.json"


def build_sparse_vectors(
        client,
        collection_name: str,
        index_path: Optional[Path] = None,
        scroll_batch: int = 512,
        update_batch: int = 500,
) -> Bm25Index:
    """
    Post-ingestion BM25 pass (NOT part of the chunking pipeline,
    so E2 storage/total times are unaffected):

    1. scroll the collection (payload field "phrase"),
    2. build the index over the raw chunk text,
    3. save the index JSON (must be identical at query time),
    4. write per-point BM25 weights via update_vectors (sparse).
    """
    from qdrant_client.models import SparseVector

    index_path = index_path or index_path_for(collection_name)

    # 1. Scroll the whole collection
    documents: List[Tuple[str, str]] = []
    offset = None
    while True:
        points, offset = client.scroll(
            collection_name=collection_name,
            limit=scroll_batch,
            offset=offset,
            with_payload=True,
            with_vectors=False,
        )
        for p in points:
            payload = p.payload or {}
            text = payload.get("phrase") or payload.get("text") or ""
            documents.append((str(p.id), text))
        if offset is None:
            break
    if not documents:
        raise RuntimeError(
            f"Kolekcja '{collection_name}' jest pusta -- nic do zaindeksowania."
        )

    # 2. Build
    index = Bm25Index(collection_name)
    index.build(documents)

    # 3. Persist
    index.save(index_path)

    # 4. Write sparse vectors in batches
    updated = 0
    batch: List[Dict] = []
    for point_id, text in documents:
        indices, values = index.point_weights(text)
        batch.append({
            "id": point_id,
            "vector": {"sparse": SparseVector(indices=indices, values=values)},
        })
        if len(batch) >= update_batch:
            client.update_vectors(collection_name=collection_name, points=batch)
            updated += len(batch)
            batch = []
            logger.info(f"BM25: zapisano {updated}/{len(documents)} wektorów sparse")
    if batch:
        client.update_vectors(collection_name=collection_name, points=batch)
        updated += len(batch)
    logger.info(f"BM25: gotowe -- {updated} punktów z wagami sparse w '{collection_name}'")
    return index


def load_index(collection_name: str) -> Optional[Bm25Index]:
    """Load the persisted index for a collection (None if missing)."""
    return Bm25Index.load(index_path_for(collection_name))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build the BM25 sparse index for a Qdrant collection."
    )
    parser.add_argument("collection", help="Qdrant collection name")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    from dotenv import load_dotenv
    import qdrant_client

    load_dotenv(PROJECT_ROOT / ".env")
    url = os.getenv("QDRANT_API")
    if not url:
        print("Brak QDRANT_API w .env", file=sys.stderr)
        return 1

    client = qdrant_client.QdrantClient(url=url)
    build_sparse_vectors(client, args.collection)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
