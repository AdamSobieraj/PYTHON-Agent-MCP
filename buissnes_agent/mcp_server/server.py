from __future__ import annotations

import argparse
import asyncio
import logging
import os
import sys
from collections.abc import Callable

from fastmcp import FastMCP


logging.basicConfig(level=logging.INFO, stream=sys.stderr)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)

DEFAULT_MCP_SERVER_NAME = "Knowledge Base RAG Service"
GENERIC_RAG_TOOL_DESCRIPTION_ENV_VAR = "KNOWLEDGE_BASE_RAG_TOOL_DESCRIPTION"
DEFAULT_GENERIC_RAG_TOOL_DESCRIPTION = (
    "Retrieve relevant chunks from a Qdrant knowledge-base collection for a "
    "simple RAG workflow. Provide the user's query and the target "
    "collection_name. Use this tool when you need raw supporting passages "
    "with metadata. The tool does not answer the question for you; it returns "
    "retrieved chunks and metadata so you can decide what to do next."
)

RunGenericRag = Callable[[str, str], str]


def _default_run_generic_rag(query: str, collection_name: str) -> str:
    from buissnes_agent.tools.tool_iso_rag import run_generic_rag

    return run_generic_rag(query, collection_name)


def resolve_generic_rag_tool_description() -> str:
    description = os.getenv(GENERIC_RAG_TOOL_DESCRIPTION_ENV_VAR, "").strip()
    if description:
        return description
    return DEFAULT_GENERIC_RAG_TOOL_DESCRIPTION


def _normalize_collection_name(collection_name: str) -> str:
    normalized = collection_name.strip()
    if not normalized:
        raise ValueError("collection_name must be a non-empty string.")
    return normalized


async def run_generic_collection_rag(
    query: str,
    collection_name: str,
    *,
    run_rag: RunGenericRag = _default_run_generic_rag,
) -> str:
    normalized_collection_name = _normalize_collection_name(collection_name)
    return await asyncio.to_thread(run_rag, query, normalized_collection_name)


def create_mcp_server(
    *,
    server_name: str = DEFAULT_MCP_SERVER_NAME,
    run_rag: RunGenericRag = _default_run_generic_rag,
) -> FastMCP:
    mcp = FastMCP(server_name)

    @mcp.tool(description=resolve_generic_rag_tool_description())
    async def query_knowledge_base(query: str, collection_name: str) -> str:
        """Retrieve chunks from a selected Qdrant collection."""

        return await run_generic_collection_rag(
            query,
            collection_name,
            run_rag=run_rag,
        )

    return mcp


def _build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run the MCP server for the business-agent knowledge base."
    )
    parser.add_argument(
        "--transport",
        default="stdio",
        choices=["stdio", "sse", "http"],
        help=(
            "Transport mode: 'stdio' (default), 'sse' for SSE, or 'http' "
            "for streamable HTTP."
        ),
    )
    parser.add_argument(
        "--port",
        default=8000,
        type=int,
        help="Listening port for SSE or HTTP transport (default: 8000).",
    )
    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="Listening host for SSE or HTTP transport (default: 0.0.0.0).",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    parser = _build_arg_parser()
    args = parser.parse_known_args(argv)[0]

    mcp = create_mcp_server()
    print(
        "Starting Knowledge Base MCP Server in mode: "
        f"{args.transport.upper()} {args.port} {args.host}...",
        file=sys.stderr,
    )

    if args.transport == "sse":
        mcp.host = args.host
        mcp.port = args.port
        mcp.run(transport="sse")
        return

    if args.transport == "http":
        mcp.run(transport="http", host=args.host, port=args.port)
        return

    mcp.run(transport="stdio")
