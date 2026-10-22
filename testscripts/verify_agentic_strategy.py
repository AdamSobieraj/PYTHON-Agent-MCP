"""
Standalone verification for NewAgenticStrategy.
Stubs langchain deps and langchain_openai.ChatOpenAI (no live LLM endpoint
in this env) with a deterministic fake that groups numbered sentences by
topic and returns the JSON partition — so the real prompt/parse/validate/
fallback pipeline is exercised.
"""
import json
import os
import re
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


class _Resp:
    def __init__(self, content):
        self.content = content


class FakeChatOpenAI:
    calls = 0
    fail = False        # invoke() raises (endpoint down)
    bad_output = False  # invoke() returns non-JSON prose
    single_group = False  # LLM lumps everything into one group
    bad_first = False   # first invoke drops the last sentence (invalid partition)

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def invoke(self, messages):
        FakeChatOpenAI.calls += 1
        if FakeChatOpenAI.fail:
            raise RuntimeError("LLM endpoint unavailable")
        if FakeChatOpenAI.bad_output:
            return _Resp("Sorry, I cannot do that.")
        if FakeChatOpenAI.bad_first and FakeChatOpenAI.calls == 1:
            # invalid partition: drops the last sentence (mirrors the real model)
            human = messages[1]["content"]
            lines = re.findall(r"^\s*(\d+)\.\s(.+)$", human, flags=re.M)
            nums = [int(n) for n, _ in lines][:-1]
            return _Resp(json.dumps([nums[:2], nums[2:]]))

        human = messages[1]["content"]
        lines = re.findall(r"^\s*(\d+)\.\s(.+)$", human, flags=re.M)
        nums = [int(n) for n, _ in lines]
        if FakeChatOpenAI.single_group:
            groups = [nums]
        else:
            raw = []
            for num, text in ((int(n), t) for n, t in lines):
                topic = "cat" if "cat" in text.lower() else "other"
                if raw and raw[-1][0] == topic:
                    raw[-1][1].append(num)
                else:
                    raw.append([topic, [num]])
            groups = [nums for _, nums in raw]
        return _Resp(json.dumps(groups))


_stub("langchain_openai", ChatOpenAI=FakeChatOpenAI)

os.environ["CHAT_BASE_URL"] = "http://fake/v1"
os.environ["CHAT_MODEL"] = "fake-model"

from buissnes_agent.textchunker.langchain.base import ChunkingStrategy
from buissnes_agent.textchunker.langchain.strategies.new_agentic import NewAgenticStrategy

failures = []
TEXT = ("The cat sat on the mat. "
        "The cat and the mat were cozy. "
        "Stock markets rose. "
        "Stock markets and investors rose.")


def reset():
    FakeChatOpenAI.calls = 0
    FakeChatOpenAI.fail = False
    FakeChatOpenAI.bad_output = False
    FakeChatOpenAI.single_group = False
    FakeChatOpenAI.bad_first = False


def check(name, cond, detail=""):
    status = "PASS" if cond else "FAIL"
    print(f"[{status}] {name}" + (f" -- {detail}" if detail and not cond else ""))
    if not cond:
        failures.append(name)


# --------------------------------------------------------------- Test 1
reset()
s = NewAgenticStrategy(chunk_size=10000, chunk_overlap=0)
out = s.split_documents([Document(TEXT, {"page_number": 1, "document_line_start": 1})])
print("      chunks:", [d.page_content for d in out])
check("T1 LLM partition respected (2 chunks)", len(out) == 2, str(len(out)))
check("T1 topics separated",
      "cat" in out[0].page_content and "Stock" in out[1].page_content
      and "cat" not in out[1].page_content and "Stock" not in out[0].page_content,
      repr([d.page_content for d in out]))
check("T1 text preserved", "".join(d.page_content for d in out) == TEXT)
check("T1 one LLM call for one window", FakeChatOpenAI.calls == 1, str(FakeChatOpenAI.calls))

# --------------------------------------------------------------- Test 2
# LLM down -> deterministic fallback, ingestion still succeeds,
# and NO retry (a correction prompt cannot fix a dead endpoint)
reset(); FakeChatOpenAI.fail = True
s2 = NewAgenticStrategy(10000, 0)
out2 = s2.split_documents([Document(TEXT, {"page_number": 1})])
check("T2 LLM failure falls back (no crash)",
      len(out2) == 1 and "".join(d.page_content for d in out2) == TEXT,
      repr([d.page_content for d in out2]))
check("T2 no retry on transport failure (1 call, 1 fallback)",
      FakeChatOpenAI.calls == 1 and s2.llm_calls == 1 and s2.fallbacks == 1,
      f"calls={FakeChatOpenAI.calls} llm={s2.llm_calls} fb={s2.fallbacks}")

# --------------------------------------------------------------- Test 3
# LLM returns garbage -> one retry, then fallback
reset(); FakeChatOpenAI.bad_output = True
s3 = NewAgenticStrategy(10000, 0)
out3 = s3.split_documents([Document(TEXT, {"page_number": 1})])
check("T3 invalid LLM output falls back",
      len(out3) == 1 and "".join(d.page_content for d in out3) == TEXT,
      repr([d.page_content for d in out3]))
check("T3 retried once, then fallback (2 calls, 1 fallback)",
      FakeChatOpenAI.calls == 2 and s3.llm_calls == 2 and s3.fallbacks == 1,
      f"calls={FakeChatOpenAI.calls} llm={s3.llm_calls} fb={s3.fallbacks}")

# --------------------------------------------------------------- Test 4
# LLM lumps everything into one group -> size bounding subdivides it
reset(); FakeChatOpenAI.single_group = True
out4 = NewAgenticStrategy(40, 0).split_documents([Document(TEXT, {"page_number": 1})])
print("      chunks:", [d.page_content for d in out4])
check("T4 oversized group subdivided",
      len(out4) >= 2 and all(len(d.page_content) <= 40 for d in out4),
      repr([len(d.page_content) for d in out4]))
joined = " ".join(" ".join(d.page_content.split()) for d in out4)
check("T4 all sentences covered",
      all(sent in joined for sent in TEXT.split(". ")), repr(joined))

# --------------------------------------------------------------- Test 5
# Overlap pass carries trailing sentence across an LLM boundary
reset()
short = "The cat sat. The cat drank. Stock rose. Stock fell."
out5 = NewAgenticStrategy(100, 15).split_documents([Document(short, {"page_number": 1})])
print("      chunks:", [d.page_content for d in out5])
check("T5 two LLM groups", len(out5) == 2, str(len(out5)))
check("T5 overlap carries trailing sentence",
      len(out5) == 2 and out5[1].page_content.startswith("The cat drank."),
      repr([d.page_content for d in out5]))

# --------------------------------------------------------------- Test 6
reset()
out6 = NewAgenticStrategy(100, 0).split_documents(
    [Document("The cat sat on the mat.", {"page_number": 1})])
check("T6 single sentence -> one chunk, no LLM call",
      len(out6) == 1 and out6[0].page_content == "The cat sat on the mat."
      and FakeChatOpenAI.calls == 0,
      f"chunks={len(out6)} calls={FakeChatOpenAI.calls}")

# --------------------------------------------------------------- Test 7
out7 = NewAgenticStrategy(100, 0).split_documents([Document("   ", {"page_number": 1})])
check("T7 whitespace doc skipped", out7 == [])

# --------------------------------------------------------------- Test 8
# Missing .env config -> clear error at construction
saved = {k: os.environ.pop(k, None) for k in ("CHAT_BASE_URL", "CHAT_MODEL")}
raised = False
try:
    NewAgenticStrategy(100, 0)
except ValueError:
    raised = True
finally:
    for k, v in saved.items():
        if v is not None:
            os.environ[k] = v
check("T8 missing CHAT_* env raises", raised)

# --------------------------------------------------------------- Test 9
reset()
out9 = NewAgenticStrategy(10000, 0).split_documents([
    Document(TEXT, {"page_number": 1, "document_line_start": 1}),
    Document(short, {"page_number": 2, "document_line_start": 9}),
])
check("T9 metadata preserved", all(d.metadata.get("page_number") in (1, 2) for d in out9),
      repr([d.metadata for d in out9]))
check("T9 line numbers attached",
      all("md_start_line" in d.metadata and "md_end_line" in d.metadata for d in out9),
      repr([d.metadata for d in out9]))

# --------------------------------------------------------------- Test 10
check("T10 implements ChunkingStrategy", isinstance(s, ChunkingStrategy))
check("T10 split_documents signature",
      str(s.split_documents.__code__.co_varnames[:1]) == "(['documents'])"
      or s.split_documents.__code__.co_varnames[1] == "documents")

# --------------------------------------------------------------- Test 11
# Windowing: 2 sentences per request -> 2 LLM calls, groups reassembled
reset()
out11 = NewAgenticStrategy(10000, 0, max_sentences_per_request=2).split_documents(
    [Document(TEXT, {"page_number": 1})])
check("T11 windowed LLM calls", FakeChatOpenAI.calls == 2, str(FakeChatOpenAI.calls))
check("T11 groups reassembled",
      len(out11) == 2 and "cat" in out11[0].page_content and "Stock" in out11[1].page_content,
      repr([d.page_content for d in out11]))

# --------------------------------------------------------------- Test 12
# Partition validator unit tests
V = NewAgenticStrategy._validate_partition
check("T12 valid partition", V([[1, 2], [3, 4]], 4) == [[1, 2], [3, 4]])
check("T12 single group ok", V([[1, 2, 3, 4]], 4) == [[1, 2, 3, 4]])
check("T12 missing sentence rejected", V([[1], [3, 4]], 4) is None)
check("T12 out-of-order rejected", V([[2, 1], [3, 4]], 4) is None)
check("T12 duplicate rejected", V([[1, 2], [2, 3]], 4) is None)
check("T12 non-int rejected", V([[1, "a"]], 2) is None)
check("T12 extra sentence rejected", V([[1, 2, 3, 4, 5]], 4) is None)
check("T12 empty rejected", V([], 4) is None)

# --------------------------------------------------------------- Test 13
# JSON extraction: code fences, prose around JSON
E = NewAgenticStrategy._extract_json
check("T13 plain JSON", E("[[1,2],[3]]") == [[1, 2], [3]])
check("T13 fenced JSON", E("```json\n[[1,2],[3]]\n```") == [[1, 2], [3]])
check("T13 prose around JSON", E("Here is the grouping: [[1,2],[3]] done.") == [[1, 2], [3]])
check("T13 no JSON -> None", E("I cannot do that.") is None)
check("T13 list content blocks", E([{"type": "text", "text": "[[1]]"}]) == [[1]])

# --------------------------------------------------------------- Test 14
# Invalid partition (drops last sentence) -> one correction retry -> valid
reset(); FakeChatOpenAI.bad_first = True
s14 = NewAgenticStrategy(10000, 0)
out14 = s14.split_documents([Document(TEXT, {"page_number": 1})])
check("T14 retry after invalid partition",
      len(out14) == 2 and "".join(d.page_content for d in out14) == TEXT,
      repr([d.page_content for d in out14]))
check("T14 two LLM calls (1 + retry), no fallback",
      FakeChatOpenAI.calls == 2 and s14.llm_calls == 2 and s14.fallbacks == 0,
      f"calls={FakeChatOpenAI.calls} llm={s14.llm_calls} fb={s14.fallbacks}")

print()
if failures:
    print(f"RESULT: {len(failures)} FAILED -> {failures}")
    sys.exit(1)
print("RESULT: ALL CHECKS PASSED")
