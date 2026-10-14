"""
Etap 2 verification: cost counters and phase timings.

Covers:
1. LocalEmbeddingClient: http_requests / texts_embedded / reset_counters
   (real code path, only the HTTP session is faked).
2. NewAgenticStrategy: llm_calls / fallbacks (LLM failing -> fallback,
   LLM valid -> no fallback).
3. NewSemanticStrategy: injected client shares the counters.
4. SearchKnowledgebase end-to-end: per-document records in
   document_results with phase timings and consistent counters.
"""
import os
import sys
from types import SimpleNamespace

os.environ.setdefault("CHAT_BASE_URL", "http://fake.local/v1")
os.environ.setdefault("CHAT_MODEL", "fake-model")

from langchain_core.documents import Document  # noqa: E402

from buissnes_agent.EmbeddingClient import LocalEmbeddingClient  # noqa: E402

failures = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f" -- {detail}" if detail and not cond else ""))
    if not cond:
        failures.append(name)


# ---------------------------------------------------------------- fakes
class FakeResponse:
    def __init__(self, n, dim):
        self.status_code = 200
        self.text = "ok"
        self._n = n
        self._dim = dim

    def json(self):
        return {
            "data": [
                {"index": i, "embedding": [0.1] * self._dim}
                for i in range(self._n)
            ]
        }


def make_client(dim=8, batch_size=2):
    client = LocalEmbeddingClient(
        base_url="http://fake.local/embeddings",
        api_key="EMPTY",
        model="fake-model",
        dimensions=dim,
        batch_size=batch_size,
    )
    client.session.post = lambda *a, **k: FakeResponse(
        len(k["json"]["input"]), dim
    )
    return client


class LlmBoom:
    def invoke(self, messages):
        raise RuntimeError("simulated LLM outage")


class LlmGood:
    def invoke(self, messages):
        return SimpleNamespace(content="[[1,2],[3,4]]")


class FakeStore:
    def __init__(self):
        self.inserted = 0

    def count(self):
        return 0

    def insert_batch(self, items):
        self.inserted += len(items)

    def search(self, query_vector, limit=3):
        return []


class FakeLoader:
    def __init__(self, docs):
        self._docs = docs  # list of (key, text)

    def list_objects(self):
        for key, _ in self._docs:
            yield key

    def load_file_with_metadata(self, key):
        text = dict(self._docs)[key]
        return (
            [Document(page_content=text, metadata={"page_number": 1})],
            {"title": "test doc"},
        )


TEXT_4_SENT = "Alpha beta gamma. Delta epsilon zeta. Eta theta iota. Kappa lambda mu."

# --------------------------------------------------------------- Test 1
# LocalEmbeddingClient counters (real code path, faked HTTP only)
client = make_client(dim=8, batch_size=2)
vecs = client.embed_documents(["one two", "three four", "five six"])
check("T1 embed_documents count", len(vecs) == 3, str(len(vecs)))
check("T1 texts_embedded=3", client.texts_embedded == 3, str(client.texts_embedded))
check("T1 http_requests=2 (batch=2)", client.http_requests == 2, str(client.http_requests))

client.reset_counters()
client.embed_query("single text")
check("T1 reset + embed_query", client.http_requests == 1 and client.texts_embedded == 1,
      f"http={client.http_requests} texts={client.texts_embedded}")

# --------------------------------------------------------------- Test 2
# NewAgenticStrategy: llm_calls / fallbacks
from buissnes_agent.textchunker.langchain.strategies.new_agentic import (  # noqa: E402
    NewAgenticStrategy,
)

s = NewAgenticStrategy(chunk_size=1000, chunk_overlap=0)
s.llm = LlmBoom()
out = s.split_documents([Document(page_content=TEXT_4_SENT, metadata={"page_number": 1})])
check("T2 failing LLM -> chunks produced", len(out) > 0, str(len(out)))
check("T2 llm_calls=1", s.llm_calls == 1, str(s.llm_calls))
check("T2 fallbacks=1", s.fallbacks == 1, str(s.fallbacks))

s.reset_counters()
s.llm = LlmGood()
out2 = s.split_documents([Document(page_content=TEXT_4_SENT, metadata={"page_number": 1})])
check("T2 valid LLM -> 2 chunks", len(out2) == 2, str(len(out2)))
check("T2 llm_calls=1", s.llm_calls == 1, str(s.llm_calls))
check("T2 fallbacks=0", s.fallbacks == 0, str(s.fallbacks))

# --------------------------------------------------------------- Test 3
# NewSemanticStrategy: injected client shares counters
from buissnes_agent.textchunker.langchain.strategies.new_semantic import (  # noqa: E402
    NewSemanticStrategy,
)

client.reset_counters()
sem = NewSemanticStrategy(
    chunk_size=1000, chunk_overlap=0, min_chunk_size=10, embeddings=client
)
sem.split_documents([Document(page_content=TEXT_4_SENT, metadata={"page_number": 1})])
check("T3 semantic used injected client", client.texts_embedded == 4,
      str(client.texts_embedded))
check("T3 same client instance", sem.embeddings is client)

# --------------------------------------------------------------- Test 4
# SearchKnowledgebase end-to-end: document_results records
from buissnes_agent.KnowledgebasePipeline import SearchKnowledgebase  # noqa: E402

client = make_client(dim=8, batch_size=2)
store = FakeStore()
loader = FakeLoader([
    ("doc1.md", TEXT_4_SENT),
    ("doc2.md", "Pierwsze zdanie. Drugie zdanie. Trzecie zdanie. Czwarte zdanie. "
                "Piate zdanie. Siate zdanie."),
])

kb = SearchKnowledgebase(
    client=client,
    database_store=store,
    data_loader=loader,
    embedding_model="fake-model",
    batch_size=50,
    force_refresh=True,
)

check("T4 two documents recorded", len(kb.document_results) == 2,
      str(len(kb.document_results)))

for i, rec in enumerate(kb.document_results, start=1):
    check(f"T4 doc{i} strategy=sentenceBased", rec["strategy"] == "sentenceBased",
          str(rec["strategy"]))
    check(f"T4 doc{i} num_chunks>0", rec["num_chunks"] > 0, str(rec["num_chunks"]))
    check(f"T4 doc{i} texts_embedded == num_chunks",
          rec["texts_embedded"] == rec["num_chunks"],
          f"texts={rec['texts_embedded']} chunks={rec['num_chunks']}")
    check(f"T4 doc{i} embedding_http_requests == num_chunks",
          rec["embedding_http_requests"] == rec["num_chunks"],
          f"http={rec['embedding_http_requests']} chunks={rec['num_chunks']}")
    check(f"T4 doc{i} no LLM/fallbacks",
          rec["llm_calls"] == 0 and rec["fallbacks"] == 0,
          f"llm={rec['llm_calls']} fb={rec['fallbacks']}")
    check(f"T4 doc{i} timings >= 0",
          all(rec[k] >= 0 for k in ("chunking_ms", "embedding_ms",
                                    "storage_ms", "total_ms")),
          str({k: rec[k] for k in ("chunking_ms", "embedding_ms", "storage_ms", "total_ms")}))
    check(f"T4 doc{i} total >= chunking + embedding",
          rec["total_ms"] >= rec["chunking_ms"] + rec["embedding_ms"] - 0.01,
          str(rec["total_ms"]))

total_chunks = sum(r["num_chunks"] for r in kb.document_results)
check("T4 store received all chunks", store.inserted == total_chunks,
      f"inserted={store.inserted} expected={total_chunks}")

print()
if failures:
    print(f"RESULT: {len(failures)} FAILED -> {failures}")
    sys.exit(1)
print("RESULT: ALL CHECKS PASSED")
