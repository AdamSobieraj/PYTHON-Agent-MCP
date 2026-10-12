"""
Standalone verification for NewSemanticStrategy.
Stubs the langchain dependencies and LocalEmbeddingClient (no live endpoint
in this env) with deterministic word-overlap vectors so the real
similarity/breakpoint logic is exercised.
"""
import math
import sys
import types


def _stub(name, **attrs):
    mod = types.ModuleType(name)
    for k, v in attrs.items():
        setattr(mod, k, v)
    sys.modules[name] = mod
    return mod


class Document:
    def __init__(self, page_content="", metadata=None):
        self.page_content = page_content
        self.metadata = metadata or {}


class _Dummy:
    def __init__(self, *a, **k):
        pass


lc = _stub("langchain_core")
lc_docs = _stub("langchain_core.documents", Document=Document)
lc.documents = lc_docs
_stub("langchain_text_splitters",
      CharacterTextSplitter=_Dummy,
      RecursiveCharacterTextSplitter=_Dummy,
      MarkdownHeaderTextSplitter=_Dummy)
le = _stub("langchain_experimental")
le_ts = _stub("langchain_experimental.text_splitter", SemanticChunker=_Dummy)
le.text_splitter = le_ts

# Deterministic "embeddings": word-overlap vectors over a small vocabulary
VOCAB = ["cat", "mat", "cozy", "stock", "markets", "investors", "apple", "fig", "date"]


class FakeLocalEmbeddingClient:
    fail = False  # flip to True to simulate an endpoint outage

    def __init__(self):
        if FakeLocalEmbeddingClient.fail:
            raise RuntimeError("embedding endpoint unavailable")

    def embed_documents(self, texts):
        if FakeLocalEmbeddingClient.fail:
            raise RuntimeError("embedding endpoint unavailable")
        out = []
        for t in texts:
            words = [w.lower() for w in t.split()]
            vec = [words.count(w) for w in VOCAB]
            norm = math.sqrt(sum(x * x for x in vec))
            out.append([x / norm for x in vec] if norm else vec)
        return out

    def embed_query(self, text):
        return self.embed_documents([text])[0]


_stub("buissnes_agent.EmbeddingClient", LocalEmbeddingClient=FakeLocalEmbeddingClient)
_stub("langchain_openai", ChatOpenAI=_Dummy)

from buissnes_agent.textchunker.langchain.base import ChunkingStrategy
from buissnes_agent.textchunker.langchain.strategies.new_semantic import NewSemanticStrategy

failures = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f" -- {detail}" if detail and not cond else ""))
    if not cond:
        failures.append(name)


# --------------------------------------------------------------- Test 1
# Two clear topics -> exactly one breakpoint between them
text = ("The cat sat on the mat. "
        "The cat and the mat were cozy. "
        "Stock markets rose. "
        "Stock markets and investors rose.")
s = NewSemanticStrategy(chunk_size=10000, chunk_overlap=0, min_chunk_size=10)
out = s.split_documents([Document(text, {"page_number": 1, "document_line_start": 1})])
print("      chunks:", [d.page_content for d in out])
check("T1 two topics -> two chunks", len(out) == 2, str(len(out)))
check("T1 topics separated",
      "cat" in out[0].page_content and "Stock" in out[1].page_content
      and "cat" not in out[1].page_content and "Stock" not in out[0].page_content,
      repr([d.page_content for d in out]))
check("T1 text preserved", "".join(d.page_content for d in out) == text)

# --------------------------------------------------------------- Test 2
# Size bounding: same topics, small chunk_size -> subdivided at sentence
# boundaries, every chunk within the limit, all sentences still covered
s2 = NewSemanticStrategy(chunk_size=40, chunk_overlap=10, min_chunk_size=10)
out2 = s2.split_documents([Document(text, {"page_number": 1})])
print("      chunks:", [d.page_content for d in out2])
check("T2 size limit respected", all(len(d.page_content) <= 40 for d in out2),
      str([len(d.page_content) for d in out2]))
joined = " ".join(" ".join(d.page_content.split()) for d in out2)
check("T2 all sentences covered",
      all(sent in joined for sent in [
          "The cat sat on the mat.",
          "The cat and the mat were cozy.",
          "Stock markets rose.",
          "Stock markets and investors rose."]),
      repr(joined))

# --------------------------------------------------------------- Test 3
# Single sentence -> single chunk (no similarity pairs to compare)
out3 = NewSemanticStrategy(100, 0, min_chunk_size=10).split_documents(
    [Document("The cat sat on the mat.", {"page_number": 1})])
check("T3 single sentence -> one chunk",
      len(out3) == 1 and out3[0].page_content == "The cat sat on the mat.",
      repr([d.page_content for d in out3]))

# --------------------------------------------------------------- Test 4
# Whitespace-only document -> skipped
out4 = NewSemanticStrategy(100, 0).split_documents([Document("   ", {"page_number": 1})])
check("T4 whitespace doc skipped", out4 == [])

# --------------------------------------------------------------- Test 5
# Endpoint outage -> constructor raises (same pattern as SemanticStrategy)
FakeLocalEmbeddingClient.fail = True
raised = False
try:
    NewSemanticStrategy(100, 0)
except RuntimeError:
    raised = True
FakeLocalEmbeddingClient.fail = False
check("T5 embedding failure raises", raised)

# --------------------------------------------------------------- Test 6
# min_chunk_size merging (direct unit test of the helper)
s6 = NewSemanticStrategy(10000, 0, min_chunk_size=10)
groups = [["a b c d. "], ["x. "], ["e f g h i j. "]]
merged = s6._enforce_min_size(groups)
print("      merged:", merged)
check("T6 tiny middle group merged",
      len(merged) == 2 and merged[0] == ["a b c d. ", "x. "] and merged[1] == ["e f g h i j. "],
      repr(merged))

# --------------------------------------------------------------- Test 7
# Metadata + line numbers attached
out7 = NewSemanticStrategy(10000, 0, min_chunk_size=10).split_documents([
    Document(text, {"page_number": 1, "document_line_start": 1}),
    Document("Apple fig date. Date fig apple.", {"page_number": 2, "document_line_start": 9}),
])
check("T7 metadata preserved", all(d.metadata.get("page_number") in (1, 2) for d in out7),
      repr([d.metadata for d in out7]))
check("T7 line numbers attached",
      all("md_start_line" in d.metadata and "md_end_line" in d.metadata for d in out7),
      repr([d.metadata for d in out7]))

# --------------------------------------------------------------- Test 8
# Interface conformance + percentile helper
check("T8 implements ChunkingStrategy", isinstance(s, ChunkingStrategy))
check("T8 percentile median", abs(NewSemanticStrategy._percentile([0.816, 0.0, 0.866], 50) - 0.816) < 1e-9)
check("T8 percentile interpolation", abs(NewSemanticStrategy._percentile([0.0, 1.0], 25) - 0.25) < 1e-9)

print()
if failures:
    print(f"RESULT: {len(failures)} FAILED -> {failures}")
    sys.exit(1)
print("RESULT: ALL CHECKS PASSED")
