import os
import unittest

from unittest.mock import patch

from buissnes_agent.mcp_server.server import (
    DEFAULT_GENERIC_RAG_TOOL_DESCRIPTION,
    resolve_generic_rag_tool_description,
    run_generic_collection_rag,
)


class KnowledgeBaseMcpServerTests(unittest.IsolatedAsyncioTestCase):
    async def test_run_generic_collection_rag_passes_trimmed_collection_name(self) -> None:
        captured: dict[str, str] = {}

        def fake_run_rag(query: str, collection_name: str) -> str:
            captured["query"] = query
            captured["collection_name"] = collection_name
            return "ok"

        result = await run_generic_collection_rag(
            "Explain pacs.008",
            "  iso20022_business  ",
            run_rag=fake_run_rag,
        )

        self.assertEqual(result, "ok")
        self.assertEqual(captured["query"], "Explain pacs.008")
        self.assertEqual(captured["collection_name"], "iso20022_business")

    async def test_run_generic_collection_rag_requires_collection_name(self) -> None:
        with self.assertRaisesRegex(ValueError, "collection_name"):
            await run_generic_collection_rag(
                "Explain pacs.008",
                "   ",
                run_rag=lambda query, collection_name: "unused",
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
