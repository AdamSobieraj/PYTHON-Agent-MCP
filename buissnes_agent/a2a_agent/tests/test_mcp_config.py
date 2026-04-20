import os
import unittest

from unittest.mock import patch

from pydantic import ValidationError

from buissnes_agent.a2a_agent.mcp_config import (
    AgentRuntimeConfig,
    McpServerConfig,
    expand_env_vars,
    matches_tool_filters,
    resolve_mcp_servers,
)


class McpConfigTests(unittest.TestCase):
    def test_expand_env_vars_supports_defaults(self) -> None:
        with patch.dict(os.environ, {"PRIMARY_MCP_URL": "http://primary/mcp"}):
            expanded = expand_env_vars(
                {
                    "url": "${PRIMARY_MCP_URL:-http://fallback/mcp}",
                    "headers": {
                        "Authorization": "Bearer ${MISSING_TOKEN:-demo-token}",
                    },
                }
            )

        self.assertEqual(expanded["url"], "http://primary/mcp")
        self.assertEqual(
            expanded["headers"]["Authorization"],
            "Bearer demo-token",
        )

    def test_expand_env_vars_tolerates_missing_closing_brace(self) -> None:
        with patch.dict(
            os.environ,
            {"ATLASSIAN_MCP_URL": "http://atlassian.example/mcp/"},
        ):
            expanded = expand_env_vars(
                "${ATLASSIAN_MCP_URL:-http://localhost:9002/mcp/"
            )

        self.assertEqual(expanded, "http://atlassian.example/mcp/")

    def test_resolve_mcp_servers_falls_back_to_legacy_env_urls(self) -> None:
        with patch.dict(
            os.environ,
            {
                "INTERNAL_MCP_URL": "http://internal.example/mcp",
                "ATLASSIAN_MCP_URL": "http://atlassian.example/mcp/",
            },
        ):
            runtime_config = AgentRuntimeConfig(prompt="test", config={})
            servers = resolve_mcp_servers(runtime_config)

        self.assertEqual(len(servers), 2)
        self.assertEqual(servers[0].url, "http://internal.example/mcp")
        self.assertEqual(servers[1].url, "http://atlassian.example/mcp/")

    def test_resolve_mcp_servers_respects_explicit_empty_list(self) -> None:
        runtime_config = AgentRuntimeConfig(
            prompt="test",
            config={"mcp_servers": []},
        )

        self.assertEqual(resolve_mcp_servers(runtime_config), [])

    def test_runtime_config_accepts_camel_case_langfuse_keys(self) -> None:
        runtime_config = AgentRuntimeConfig(
            prompt="test",
            config={
                "mcpServers": [
                    {
                        "name": "atlassian",
                        "url": "http://localhost:9002/mcp/",
                        "blockedPlugins": ["confluence_comments"],
                    }
                ]
            },
        )

        servers = resolve_mcp_servers(runtime_config)
        self.assertEqual(len(servers), 1)
        self.assertEqual(servers[0].blocked_plugins, ["confluence_comments"])

    def test_server_config_rejects_both_tool_filter_modes(self) -> None:
        with self.assertRaises(ValidationError):
            McpServerConfig(
                name="atlassian",
                allowed_tools=["confluence_search"],
                blocked_tools=["confluence_delete_page"],
            )

    def test_server_config_rejects_both_plugin_filter_modes(self) -> None:
        with self.assertRaises(ValidationError):
            McpServerConfig(
                name="atlassian",
                allowed_plugins=["confluence_pages"],
                blocked_plugins=["confluence_comments"],
            )

    def test_matches_tool_filters_supports_allowed_tools_whitelist(self) -> None:
        server_config = McpServerConfig(
            name="atlassian",
            allowed_tools=["confluence_search", "confluence_get_page"],
        )
        pages_meta = {"_fastmcp": {"tags": ["toolset:confluence_pages", "read"]}}

        self.assertTrue(
            matches_tool_filters(
                "confluence_search",
                pages_meta,
                server_config,
            )
        )
        self.assertFalse(
            matches_tool_filters(
                "confluence_get_comments",
                pages_meta,
                server_config,
            )
        )

    def test_matches_tool_filters_supports_fastmcp_toolset_aliases(self) -> None:
        server_config = McpServerConfig(
            name="atlassian",
            allowed_plugins=["confluence_pages"],
            blocked_tools=["confluence_delete_page"],
        )
        pages_meta = {"_fastmcp": {"tags": ["toolset:confluence_pages", "read"]}}
        comments_meta = {
            "_fastmcp": {"tags": ["toolset:confluence_comments", "read"]}
        }

        self.assertTrue(
            matches_tool_filters(
                "confluence_search",
                pages_meta,
                server_config,
            )
        )
        self.assertFalse(
            matches_tool_filters(
                "confluence_get_comments",
                comments_meta,
                server_config,
            )
        )
        self.assertFalse(
            matches_tool_filters(
                "confluence_delete_page",
                pages_meta,
                server_config,
            )
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
