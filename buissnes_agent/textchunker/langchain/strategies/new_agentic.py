import json
import logging
import os
import re
from typing import Any, List, Optional

from langchain_core.documents import Document
from langchain_openai import ChatOpenAI

from buissnes_agent.textchunker.langchain.base import ChunkingStrategy
from buissnes_agent.textchunker.langchain.strategies.line_calculator import LineNumberCalculator
from buissnes_agent.textchunker.langchain.strategies.new_sentence_based import NewSentenceBasedStrategy

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are a document chunking assistant. "
    "You find where new topics begin in a list of numbered sentences. "
    "You must respond with ONLY a JSON array of integers, "
    "without any commentary or code fences."
)

_THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL | re.IGNORECASE)


class NewAgenticStrategy(ChunkingStrategy):
    """
    ### Strategy 8: Agentic (LLM-proposed boundaries)

    Uses a language model to propose where chunks should start.
    The model is set in the .env file (CHAT_BASE_URL, CHAT_API_KEY, CHAT_MODEL).

    **How it works:**
    1. Text is split into sentences (via NewSentenceBasedStrategy).
    2. Sentences are sent to the LLM in windows (max_sentences_per_request).
       The model returns only the numbers of the sentences that START a new
       chunk, e.g. [1, 4, 9]. The code turns that into a contiguous,
       in-order partition, so the result is valid by construction
       (no gaps, no duplicates). Messy answers such as [[1,7],[8,14]] are
       tolerated: the first number of each element is used as a start.
    3. If no usable answer comes back, one retry is made. If that also
       fails, or the LLM call itself fails, the window falls back to
       deterministic sentence packing (warning logged; ingestion never
       crashes because of the LLM).
    4. Groups larger than chunk_size are subdivided at sentence boundaries.
    5. chunk_overlap carries trailing sentences into the next chunk.

    **Usage:**
    Documents where fixed/semantic heuristics under-perform and a local
    LLM endpoint (LM Studio, vLLM, ...) is available.
    """

    def __init__(
            self,
            chunk_size: int,
            chunk_overlap: int,
            max_sentences_per_request: int = 25,
            temperature: float = 0.0
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.max_sentences_per_request = max_sentences_per_request
        self.temperature = temperature

        # Cost counters (E2/E4 metrics)
        self.llm_calls = 0
        self.fallbacks = 0

        # Initialize the LLM client (model is configured in .env)
        try:
            base_url = os.getenv("CHAT_BASE_URL")
            model = os.getenv("CHAT_MODEL")
            if not base_url or not model:
                raise ValueError(
                    "CHAT_BASE_URL and CHAT_MODEL must be set (.env) for NewAgenticStrategy."
                )
            self.llm = ChatOpenAI(
                model=model,
                openai_api_key=os.getenv("CHAT_API_KEY", "EMPTY"),
                openai_api_base=base_url,
                temperature=self.temperature,
                tiktoken_model_name=None,
            )
            logger.info("NewAgenticStrategy: LLM initialized: %s @ %s", model, base_url)
        except Exception as e:
            logger.error("NewAgenticStrategy: Failed to initialize LLM. Error: %s", e)
            raise

        # Reused: sentence detection
        self._sentence_strategy = NewSentenceBasedStrategy(chunk_size, chunk_overlap)

    def reset_counters(self) -> None:
        """Reset cost counters (call between documents / experiments)."""
        self.llm_calls = 0
        self.fallbacks = 0

    # ------------------------------------------------------------------
    # INTERFACE (ChunkingStrategy)
    # ------------------------------------------------------------------
    def split_documents(self, documents: List[Document]) -> List[Document]:
        if not self.llm:
            raise ValueError("LLM not initialized.")

        final_chunks: List[Document] = []

        for doc in documents:
            text = doc.page_content
            if not text or not text.strip():
                continue

            units = self._sentence_strategy.split_into_sentence_units(text)
            if not units:
                continue

            for group in self._propose_groups(units):
                # Copy page metadata (e.g., page_number) to generated chunks
                final_chunks.append(Document(
                    page_content="".join(group),
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
    def _propose_groups(self, units: List[str]) -> List[List[str]]:
        """Full pipeline: LLM proposal -> size bounding -> overlap."""
        if len(units) <= 1:
            return [units]

        groups: List[List[str]] = []
        for i in range(0, len(units), self.max_sentences_per_request):
            window = units[i:i + self.max_sentences_per_request]
            groups.extend(self._groups_for_window(window))

        groups = self._size_bound(groups)
        groups = self._apply_overlap(groups)
        return groups

    def _groups_for_window(self, window: List[str]) -> List[List[str]]:
        """Asks the LLM where new chunks start within the window.

        One retry when the answer contains no usable numbers, then a
        deterministic sentence-packing fallback. Transport failures
        (endpoint down) skip the retry and go straight to the fallback.
        """
        n = len(window)
        messages = self._build_prompt(window)

        try:
            content = self._invoke_and_log(messages)
        except Exception as e:
            self.fallbacks += 1
            logger.warning(
                "NewAgenticStrategy: LLM call failed (%s); "
                "falling back to sentence packing for %d sentence(s).", e, n
            )
            return self._pack_units(window)

        numbers = self._starts_to_groups(self._extract_json(content), n)
        if numbers is not None:
            return [[window[i - 1] for i in nums] for nums in numbers]

        logger.info(
            "NewAgenticStrategy: no usable chunk starts; retrying once. Raw response: %s",
            repr(content)[:300],
        )
        retry_messages = messages + [
            {"role": "assistant", "content": content},
            {"role": "user", "content": self._correction_prompt(n)},
        ]
        try:
            content = self._invoke_and_log(retry_messages)
            numbers = self._starts_to_groups(self._extract_json(content), n)
        except Exception:
            numbers = None

        if numbers is None:
            self.fallbacks += 1
            logger.warning(
                "NewAgenticStrategy: no usable chunk starts even after one retry; "
                "falling back to sentence packing for %d sentence(s). Raw response: %s",
                n, repr(content)[:300],
            )
            return self._pack_units(window)
        return [[window[i - 1] for i in nums] for nums in numbers]

    def _invoke_and_log(self, messages: List[dict]) -> str:
        """One LLM call (counted, usage logged); returns the raw content."""
        self.llm_calls += 1
        response = self.llm.invoke(messages)
        self._log_llm_usage(response, messages)
        return response.content if hasattr(response, "content") else str(response)

    def _log_llm_usage(self, response, prompt) -> None:
        """
        Cost usage hook: report token usage of the LLM call
        (section=chunking_agentic). When the model reports nothing,
        the tokens are estimated from the prompt/response texts.
        Never raises.
        """
        try:
            usage = getattr(response, "usage_metadata", None) or {}
            if usage.get("input_tokens") is None:
                token_usage = (getattr(response, "additional_kwargs", {}) or {}).get(
                    "token_usage", {}
                )
                usage = {
                    "input_tokens": token_usage.get("prompt_tokens", 0),
                    "output_tokens": token_usage.get("completion_tokens", 0),
                }
            input_tokens = int(usage.get("input_tokens") or 0)
            output_tokens = int(usage.get("output_tokens") or 0)
            estimated = False
            if not input_tokens and not output_tokens:
                from buissnes_agent.tools.rag_metrics import estimate_tokens

                content = response.content if hasattr(response, "content") else str(response)
                input_tokens = sum(
                    estimate_tokens(str(m.get("content", ""))) for m in prompt
                )
                output_tokens = estimate_tokens(str(content))
                estimated = True
            if input_tokens or output_tokens:
                from buissnes_agent.tools.rag_metrics import log_cost_usage

                log_cost_usage(
                    model=os.getenv("CHAT_MODEL") or os.getenv("LLM_MODEL") or "unknown",
                    section="chunking_agentic",
                    input_tokens=input_tokens,
                    output_tokens=output_tokens,
                    provider=os.getenv("CHAT_PROVIDER", "local"),
                    estimated=estimated,
                )
        except Exception:
            pass

    def _build_prompt(self, window: List[str]) -> List[dict]:
        numbered = "\n".join(f"{i + 1}. {u.strip()}" for i, u in enumerate(window))
        size_hint = (
            f"- Chunks should be at most about {self.chunk_size} characters.\n"
            if self.chunk_size > 0 else ""
        )
        user = (
            "Below are numbered sentences. Decide where a NEW chunk (topic) begins.\n"
            "Rules:\n"
            "- Output a JSON array of the sentence numbers that START a new chunk.\n"
            "- The first number must be 1.\n"
            "- Numbers must be in increasing order.\n"
            f"{size_hint}"
            "Example: [1, 4, 9, 15] means chunks 1-3, 4-8, 9-14 and 15-end.\n"
            "Respond with ONLY the JSON array.\n\n"
            f"{numbered}"
        )
        return [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user},
        ]

    @staticmethod
    def _correction_prompt(n: int) -> str:
        """Follow-up after an answer with no usable numbers."""
        return (
            "Your previous answer could not be used.\n"
            "Answer again with ONLY a JSON array of integers: the numbers of the "
            f"sentences (between 1 and {n}) that start a new chunk, in increasing "
            "order, beginning with 1. Example: [1, 4, 9]."
        )

    @staticmethod
    def _extract_json(content: Any) -> Optional[list]:
        """Parses the first JSON array out of an LLM response (fences and <think> tolerated)."""
        if content is None:
            return None
        if isinstance(content, (list, tuple)):
            content = "".join(
                part.get("text", "") if isinstance(part, dict) else str(part)
                for part in content
            )
        text = _THINK_RE.sub("", str(content)).strip()
        if text.startswith("```"):
            text = text.strip("` \n")
            if text.lower().startswith("json"):
                text = text[4:].lstrip()
        start, end = text.find("["), text.rfind("]")
        if start == -1 or end <= start:
            return None
        try:
            parsed = json.loads(text[start:end + 1])
        except (json.JSONDecodeError, ValueError):
            return None
        return parsed if isinstance(parsed, list) else None

    @staticmethod
    def _starts_to_groups(parsed: Any, n: int) -> Optional[List[List[int]]]:
        """
        Builds a valid, contiguous partition of 1..n from chunk START numbers.

        Tolerates messy answers: nested lists ([[1,7],[8,14]] -> starts 1, 8),
        numeric strings, duplicates, unsorted or out-of-range numbers.
        Sentence 1 is always a start. Returns None only if nothing usable is found.
        """
        if not isinstance(parsed, list) or not parsed or n < 1:
            return None
        starts = set()
        for item in parsed:
            if isinstance(item, (list, tuple)):
                if not item:
                    continue
                item = item[0]
            if isinstance(item, str) and item.strip().isdigit():
                item = int(item.strip())
            if isinstance(item, bool) or not isinstance(item, int):
                continue
            if 1 <= item <= n:
                starts.add(item)
        if not starts:
            return None
        starts.add(1)
        bounds = sorted(starts) + [n + 1]
        return [list(range(bounds[i], bounds[i + 1])) for i in range(len(bounds) - 1)]

    def _pack_units(self, units: List[str]) -> List[List[str]]:
        """Deterministic sentence packing within chunk_size (no overlap)."""
        packed: List[List[str]] = []
        current: List[str] = []
        for u in units:
            if (self.chunk_size > 0 and current
                    and sum(len(x) for x in current) + len(u) > self.chunk_size):
                packed.append(current)
                current = []
            current.append(u)
        if current:
            packed.append(current)
        return packed

    def _size_bound(self, groups: List[List[str]]) -> List[List[str]]:
        """Subdivides groups that exceed chunk_size (whole sentences)."""
        if self.chunk_size <= 0:
            return groups
        result: List[List[str]] = []
        for group in groups:
            if sum(len(u) for u in group) > self.chunk_size:
                result.extend(self._pack_units(group))
            else:
                result.append(group)
        return result

    def _apply_overlap(self, groups: List[List[str]]) -> List[List[str]]:
        """Carries trailing sentences of each chunk into the next one."""
        if not groups or self.chunk_overlap <= 0:
            return groups

        result: List[List[str]] = [groups[0]]
        for i in range(1, len(groups)):
            current = groups[i]
            budget = self.chunk_overlap
            if self.chunk_size > 0:
                budget = min(budget, self.chunk_size - sum(len(u) for u in current))
            if budget > 0:
                carried: List[str] = []
                used = 0
                for prev in reversed(groups[i - 1]):
                    if used + len(prev) > budget:
                        break
                    carried.append(prev)
                    used += len(prev)
                result.append(list(reversed(carried)) + current)
            else:
                result.append(current)
        return result