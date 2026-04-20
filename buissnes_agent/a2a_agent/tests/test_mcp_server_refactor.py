import os
import unittest

from unittest.mock import patch

from buissnes_agent.mcp_server.server import (
    DEFAULT_GENERIC_RAG_TOOL_DESCRIPTION,
    DEFAULT_S3_DOCUMENT_RANGE_TOOL_DESCRIPTION,
    DEFAULT_S3_DOCUMENT_TOOL_DESCRIPTION,
    resolve_generic_rag_tool_description,
    resolve_s3_document_range_tool_description,
    resolve_s3_document_tool_description,
    run_generic_collection_rag,
)
from buissnes_agent.mcp_server.s3_documents import (
    ResolvedS3Object,
    fetch_markdown_document,
    fetch_markdown_document_range,
    parse_s3_uri,
)
from buissnes_agent.DataLoaderS3Service import S3TextObject
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

    def test_resolve_s3_document_tool_description_uses_env_override(self) -> None:
        with patch.dict(
            os.environ,
            {"S3_DOCUMENT_TOOL_DESCRIPTION": "Custom S3 document tool."},
        ):
            self.assertEqual(
                resolve_s3_document_tool_description(),
                "Custom S3 document tool.",
            )

    def test_resolve_s3_document_tool_description_falls_back_for_blank_value(self) -> None:
        with patch.dict(
            os.environ,
            {"S3_DOCUMENT_TOOL_DESCRIPTION": "   "},
        ):
            self.assertEqual(
                resolve_s3_document_tool_description(),
                DEFAULT_S3_DOCUMENT_TOOL_DESCRIPTION,
            )

    def test_resolve_s3_document_range_tool_description_uses_env_override(self) -> None:
        with patch.dict(
            os.environ,
            {"S3_DOCUMENT_RANGE_TOOL_DESCRIPTION": "Custom S3 range tool."},
        ):
            self.assertEqual(
                resolve_s3_document_range_tool_description(),
                "Custom S3 range tool.",
            )

    def test_resolve_s3_document_range_tool_description_falls_back_for_blank_value(self) -> None:
        with patch.dict(
            os.environ,
            {"S3_DOCUMENT_RANGE_TOOL_DESCRIPTION": "   "},
        ):
            self.assertEqual(
                resolve_s3_document_range_tool_description(),
                DEFAULT_S3_DOCUMENT_RANGE_TOOL_DESCRIPTION,
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


class S3DocumentHelperTests(unittest.TestCase):
    def test_parse_s3_uri_extracts_bucket_and_key(self) -> None:
        self.assertEqual(
            parse_s3_uri("s3://agent-documents/business/General/file.md"),
            ResolvedS3Object(
                bucket_name="agent-documents",
                object_key="business/General/file.md",
            ),
        )

    def test_parse_s3_uri_rejects_blank_value(self) -> None:
        with self.assertRaisesRegex(ValueError, "s3_uri"):
            parse_s3_uri("   ")

    def test_fetch_markdown_document_formats_response(self) -> None:
        class FakeS3Service:
            def download_text_response(
                self,
                bucket_name: str,
                object_key: str,
            ) -> S3TextObject:
                self.bucket_name = bucket_name
                self.object_key = object_key
                return S3TextObject(
                    text="# Header\n\nFull markdown body.\n",
                    content_length=29,
                    etag="etag-123",
                )

        fake_service = FakeS3Service()

        result = fetch_markdown_document(
            s3_uri="s3://agent-documents/business/General/file.md",
            s3_service=fake_service,
        )

        self.assertEqual(fake_service.bucket_name, "agent-documents")
        self.assertEqual(fake_service.object_key, "business/General/file.md")
        self.assertIn(
            "Source (file): s3://agent-documents/business/General/file.md",
            result,
        )
        self.assertIn("Returned bytes: 29", result)
        self.assertIn("# Header", result)

    def test_fetch_markdown_document_range_uses_requested_range(self) -> None:
        class FakeS3Service:
            def download_text_range(
                self,
                bucket_name: str,
                object_key: str,
                start_byte: int,
                end_byte: int | None = None,
            ) -> S3TextObject:
                self.bucket_name = bucket_name
                self.object_key = object_key
                self.start_byte = start_byte
                self.end_byte = end_byte
                return S3TextObject(
                    text="## Partial\n\nExcerpt",
                    content_length=18,
                    content_range="bytes 100-140/1024",
                    etag="etag-456",
                )

        fake_service = FakeS3Service()

        result = fetch_markdown_document_range(
            s3_uri="s3://agent-documents/business/General/file.md",
            start_byte=100,
            end_byte=140,
            s3_service=fake_service,
        )

        self.assertEqual(fake_service.bucket_name, "agent-documents")
        self.assertEqual(fake_service.object_key, "business/General/file.md")
        self.assertEqual(fake_service.start_byte, 100)
        self.assertEqual(fake_service.end_byte, 140)
        self.assertIn("Requested range: bytes=100-140", result)
        self.assertIn("S3 content range: bytes 100-140/1024", result)
        self.assertIn("## Partial", result)

    def test_fetch_markdown_document_range_rejects_invalid_ranges(self) -> None:
        with self.assertRaisesRegex(ValueError, "end_byte"):
            fetch_markdown_document_range(
                s3_uri="s3://agent-documents/business/General/file.md",
                start_byte=20,
                end_byte=10,
            )
