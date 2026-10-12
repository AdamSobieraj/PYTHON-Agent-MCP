"""
Standalone verification for NewSentenceBasedStrategy.
Stubs the langchain dependencies (not installed in this env) so the pure-Python
splitting logic can be exercised directly.
"""
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
_stub("buissnes_agent.EmbeddingClient", LocalEmbeddingClient=_Dummy)
_stub("langchain_openai", ChatOpenAI=_Dummy)

from buissnes_agent.textchunker.langchain.strategies.new_sentence_based import (
    NewSentenceBasedStrategy,
)

failures = []


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f" -- {detail}" if detail and not cond else ""))
    if not cond:
        failures.append(name)


# ---------------------------------------------------------------- Test 1
# Text round-trip: overlap=0 -> rejoining chunks reproduces the original text
text = ("Alpha beta gamma. Delta epsilon zeta. Eta theta iota. "
        "Kappa lambda mu. Nu xi omicron.")
s = NewSentenceBasedStrategy(chunk_size=40, chunk_overlap=0)
out = s.split_documents([Document(text, {"page_number": 1, "document_line_start": 1})])
check("T1 round-trip (overlap=0)", "".join(d.page_content for d in out) == text,
      repr([d.page_content for d in out]))
check("T1 size limit", all(len(d.page_content) <= 40 for d in out),
      str([len(d.page_content) for d in out]))

# ---------------------------------------------------------------- Test 2
# No cut inside a sentence: every chunk must end at a sentence/unit boundary
units = s.split_into_sentence_units(text)
print("      units:", units)
# boundary cut sits after the punctuation; the separating space travels with the next unit
expected = ["Alpha beta gamma.", " Delta epsilon zeta.", " Eta theta iota.",
            " Kappa lambda mu.", " Nu xi omicron."]
check("T2 sentence units", units == expected, repr(units))

# ---------------------------------------------------------------- Test 3
# Abbreviations / initials must not close a sentence
abbr_text = "See e.g. ISO 20022 for details. The next sentence follows. U.S. A. company replied."
units3 = NewSentenceBasedStrategy(1000, 0).split_into_sentence_units(abbr_text)
print("      abbr units:", units3)
check("T3 no split after 'e.g.'",
      any("See e.g. ISO 20022 for details." in u for u in units3), repr(units3))
check("T3 no split after 'U.S. A.'",
      any("U.S. A. company replied." in u for u in units3), repr(units3))

# ---------------------------------------------------------------- Test 4
# Overlap: trailing sentence of chunk N appears at the start of chunk N+1
s_ov = NewSentenceBasedStrategy(chunk_size=40, chunk_overlap=20)
out_ov = s_ov.split_documents([Document(text, {"page_number": 1})])
print("      overlap chunks:", [d.page_content for d in out_ov])
ok = all(out_ov[i + 1].page_content.startswith(out_ov[i].page_content[-20:].strip())
         or out_ov[i].page_content.rsplit(". ", 1)[-1].strip() in out_ov[i + 1].page_content
         for i in range(len(out_ov) - 1))
check("T4 overlap carries context", ok, repr([d.page_content for d in out_ov]))
check("T4 size limit with overlap", all(len(d.page_content) <= 40 for d in out_ov),
      str([len(d.page_content) for d in out_ov]))

# ---------------------------------------------------------------- Test 5
# Multiple documents: metadata preserved, line numbers attached
docs = [
    Document("First page. Second page sentence here. Third one.", {"page_number": 1, "document_line_start": 1}),
    Document("Page two. Another sentence on page two.", {"page_number": 2, "document_line_start": 5}),
]
out5 = NewSentenceBasedStrategy(30, 0).split_documents(docs)
check("T5 metadata preserved",
      all(d.metadata.get("page_number") in (1, 2) for d in out5),
      repr([d.metadata for d in out5]))
check("T5 line numbers attached",
      all("md_start_line" in d.metadata and "md_end_line" in d.metadata for d in out5),
      repr([d.metadata for d in out5]))

# ---------------------------------------------------------------- Test 6
# Edge cases
empty = NewSentenceBasedStrategy(50, 10).split_documents([Document("   ", {"page_number": 1})])
check("T6 whitespace-only doc skipped", empty == [], repr(empty))
giant = NewSentenceBasedStrategy(20, 5).split_documents(
    [Document("One word. " * 50, {"page_number": 1})])
check("T6 all sentences covered",
      "".join(d.page_content for d in giant).replace(" ", "") ==
      ("One word." * 50).replace(" ", ""), "round-trip mismatch")
nosize = NewSentenceBasedStrategy(0, 0).split_documents(
    [Document("A. B. C.", {"page_number": 1})])
check("T6 chunk_size=0 -> single chunk", len(nosize) == 1 and nosize[0].page_content == "A. B. C.",
      repr([d.page_content for d in nosize]))

# ---------------------------------------------------------------- Test 7
# Interface conformance
from buissnes_agent.textchunker.langchain.base import ChunkingStrategy
check("T7 implements ChunkingStrategy", isinstance(NewSentenceBasedStrategy(10, 0), ChunkingStrategy))
check("T7 split_documents signature",
      NewSentenceBasedStrategy.split_documents.__name__ == "split_documents")

print()
if failures:
    print(f"RESULT: {len(failures)} FAILED -> {failures}")
    sys.exit(1)
print("RESULT: ALL CHECKS PASSED")
