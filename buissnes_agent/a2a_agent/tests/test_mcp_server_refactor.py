import os
import unittest

from unittest.mock import patch

from buissnes_agent.mcp_server.server import (
    DEFAULT_GENERIC_RAG_TOOL_DESCRIPTION,
    resolve_generic_rag_tool_description,
    run_generic_collection_rag,
)
from buissnes_agent.tools.tool_iso_rag import (
    DEFAULT_VECTOR_AMOUNT_RAG,
    resolve_top_k,
)


class KnowledgeBaseMcpServerTests(unittest.IsolatedAsyncioTestCase):
    async def test_run_generic_collection_rag_passes_trimmed_collection_name(self) -> None:
        captured: dict[str, object] = {}

        def fake_run_rag(
            query: str,
            collection_name: str,
            top_k: int | None = None,
        ) -> str:
            captured["query"] = query
            captured["collection_name"] = collection_name
            captured["top_k"] = top_k
            return "ok"

        result = await run_generic_collection_rag(
            "Explain pacs.008",
            "  iso20022_business  ",
            7,
            run_rag=fake_run_rag,
        )

        self.assertEqual(result, "ok")
        self.assertEqual(captured["query"], "Explain pacs.008")
        self.assertEqual(captured["collection_name"], "iso20022_business")
        self.assertEqual(captured["top_k"], 7)

    async def test_run_generic_collection_rag_requires_collection_name(self) -> None:
        with self.assertRaisesRegex(ValueError, "collection_name"):
            await run_generic_collection_rag(
                "Explain pacs.008",
                "   ",
                run_rag=lambda query, collection_name, top_k=None: "unused",
            )


class KnowledgeBaseMcpServerConfigTests(unittest.TestCase):
    def test_resolve_generic_rag_tool_description_uses_env_override(self) -> None:
        with patch.dict(
            os.environ,
            {"KNOWLEDGE_BASE_RAG_TOOL_DESCRIPTION": "Custom MCP tool description."},
        ):
            self.assertEqual(
                resolve_generic_rag_tool_description(),
                "Custom MCP tool description.",
            )

    def test_resolve_generic_rag_tool_description_falls_back_for_blank_value(self) -> None:
        with patch.dict(
            os.environ,
            {"KNOWLEDGE_BASE_RAG_TOOL_DESCRIPTION": "   "},
        ):
            self.assertEqual(
                resolve_generic_rag_tool_description(),
                DEFAULT_GENERIC_RAG_TOOL_DESCRIPTION,
            )


class GenericRagTopKTests(unittest.TestCase):
    def test_resolve_top_k_prefers_explicit_value(self) -> None:
        with patch.dict(os.environ, {"VECTOR_AMOUNT_RAG": "25"}):
            self.assertEqual(resolve_top_k(3), 3)

    def test_resolve_top_k_reads_env_when_value_not_provided(self) -> None:
        with patch.dict(os.environ, {"VECTOR_AMOUNT_RAG": "12"}):
            self.assertEqual(resolve_top_k(), 12)

    def test_resolve_top_k_falls_back_to_code_default_for_invalid_env(self) -> None:
        with patch.dict(os.environ, {"VECTOR_AMOUNT_RAG": "invalid"}):
            self.assertEqual(resolve_top_k(), DEFAULT_VECTOR_AMOUNT_RAG)

    def test_resolve_top_k_rejects_non_positive_explicit_value(self) -> None:
        with self.assertRaisesRegex(ValueError, "top_k"):
            resolve_top_k(0)
