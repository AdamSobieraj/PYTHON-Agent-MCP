from __future__ import annotations

import os
import re

from typing import Any

from google.adk.tools.mcp_tool.mcp_session_manager import (
    SseConnectionParams,
    StdioConnectionParams,
    StreamableHTTPConnectionParams,
)
from mcp import StdioServerParameters
from pydantic import AliasChoices, BaseModel, ConfigDict, Field, model_validator

_ENV_VAR_PATTERN = re.compile(
    r"\$\{(?P<braced>[A-Za-z_][A-Za-z0-9_]*)(?::-(?P<default>[^}]*))?\}"
    r"|\$(?P<plain>[A-Za-z_][A-Za-z0-9_]*)"
)
_MALFORMED_FULL_ENV_VAR_PATTERN = re.compile(
    r"^\$\{(?P<braced>[A-Za-z_][A-Za-z0-9_]*)(?::-(?P<default>.*))?$"
)


def _expand_env_string(value: str) -> str:
    malformed_match = _MALFORMED_FULL_ENV_VAR_PATTERN.match(value)
    if malformed_match is not None:
        variable_name = malformed_match.group("braced")
        default_value = malformed_match.group("default")
        resolved = os.getenv(variable_name)
        if resolved is None or resolved == "":
            return default_value or ""
        return resolved

    def replace(match: re.Match[str]) -> str:
        variable_name = match.group("braced") or match.group("plain")
        default_value = match.group("default")
        resolved = os.getenv(variable_name)
        if resolved is None or resolved == "":
            return default_value or ""
        return resolved

    return _ENV_VAR_PATTERN.sub(replace, value)


def expand_env_vars(value: Any) -> Any:
    if isinstance(value, str):
        return _expand_env_string(value)
    if isinstance(value, list):
        return [expand_env_vars(item) for item in value]
    if isinstance(value, dict):
        return {
            key: expand_env_vars(item)
            for key, item in value.items()
        }
    return value


def normalize_identifier(value: str) -> str:
    return value.strip().lower().replace("-", "_").replace(" ", "_")


def extract_tool_tags(tool_meta: Any) -> set[str]:
    if not isinstance(tool_meta, dict):
        return set()

    tags: set[str] = set()

    fastmcp_meta = tool_meta.get("_fastmcp")
    if isinstance(fastmcp_meta, dict):
        for tag in fastmcp_meta.get("tags", []) or []:
            if isinstance(tag, str) and tag.strip():
                tags.add(normalize_identifier(tag))

    for key in ("tags", "plugin", "toolset"):
        value = tool_meta.get(key)
        if isinstance(value, str) and value.strip():
            tags.add(normalize_identifier(value))
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, str) and item.strip():
                    tags.add(normalize_identifier(item))

    return tags


def extract_tool_plugin_aliases(tool_name: str, tool_meta: Any) -> set[str]:
    normalized_name = normalize_identifier(tool_name)
    aliases = set(extract_tool_tags(tool_meta))
    aliases.add(normalized_name)

    if "_" in normalized_name:
        aliases.add(normalized_name.split("_", 1)[0])

    for tag in list(aliases):
        if tag.startswith("toolset:"):
            aliases.add(tag.split(":", 1)[1])

    return aliases


class McpServerConfig(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    name: str | None = None
    enabled: bool = True
    transport: str = Field(
        default="streamable_http",
        validation_alias=AliasChoices(
            "transport",
            "type",
            "connection_type",
            "connectionType",
        ),
    )
    url: str | None = None
    headers: dict[str, Any] | None = None
    timeout: float = 5.0
    sse_read_timeout: float = 60 * 5.0
    terminate_on_close: bool = True
    command: str | None = None
    args: list[str] = Field(default_factory=list)
    env: dict[str, str] | None = None
    cwd: str | None = None
    encoding: str = "utf-8"
    encoding_error_handler: str = "strict"
    tool_name_prefix: str | None = Field(
        default=None,
        validation_alias=AliasChoices("tool_name_prefix", "toolNamePrefix"),
    )
    allowed_tools: list[str] = Field(
        default_factory=list,
        validation_alias=AliasChoices(
            "allowed_tools",
            "allowedTools",
            "include_tools",
            "includeTools",
            "tool_filter",
            "toolFilter",
        ),
    )
    blocked_tools: list[str] = Field(
        default_factory=list,
        validation_alias=AliasChoices(
            "blocked_tools",
            "blockedTools",
            "disallowed_tools",
            "disallowedTools",
            "exclude_tools",
            "excludeTools",
        ),
    )
    allowed_plugins: list[str] = Field(
        default_factory=list,
        validation_alias=AliasChoices(
            "allowed_plugins",
            "allowedPlugins",
            "allowed_toolsets",
            "allowedToolsets",
            "plugins",
        ),
    )
    blocked_plugins: list[str] = Field(
        default_factory=list,
        validation_alias=AliasChoices(
            "blocked_plugins",
            "blockedPlugins",
            "disallowed_plugins",
            "disallowedPlugins",
            "blocked_toolsets",
            "blockedToolsets",
            "disallowed_toolsets",
            "disallowedToolsets",
        ),
    )

    @model_validator(mode="after")
    def validate_filter_modes(self) -> "McpServerConfig":
        if self.allowed_tools and self.blocked_tools:
            raise ValueError(
                f"MCP server '{self.resolved_name()}' cannot define both allowed_tools and blocked_tools."
            )

        if self.allowed_plugins and self.blocked_plugins:
            raise ValueError(
                f"MCP server '{self.resolved_name()}' cannot define both allowed_plugins and blocked_plugins."
            )

        return self

    def normalized_transport(self) -> str:
        return normalize_identifier(self.transport or "streamable_http")

    def resolved_name(self) -> str:
        if self.name:
            return self.name
        if self.url:
            return self.url
        if self.command:
            return self.command
        return "mcp_server"

    def build_connection_params(
        self,
    ) -> StreamableHTTPConnectionParams | SseConnectionParams | StdioConnectionParams:
        transport = self.normalized_transport()
        if transport in {"streamable_http", "streamablehttp"}:
            if not self.url:
                raise ValueError(
                    f"MCP server '{self.resolved_name()}' requires a url for streamable_http transport."
                )
            if "${" in self.url or "$" in self.url:
                raise ValueError(
                    f"MCP server '{self.resolved_name()}' has an unresolved url value: {self.url!r}"
                )
            return StreamableHTTPConnectionParams(
                url=self.url,
                headers=self.headers,
                timeout=self.timeout,
                sse_read_timeout=self.sse_read_timeout,
                terminate_on_close=self.terminate_on_close,
            )

        if transport == "sse":
            if not self.url:
                raise ValueError(
                    f"MCP server '{self.resolved_name()}' requires a url for sse transport."
                )
            if "${" in self.url or "$" in self.url:
                raise ValueError(
                    f"MCP server '{self.resolved_name()}' has an unresolved url value: {self.url!r}"
                )
            return SseConnectionParams(
                url=self.url,
                headers=self.headers,
                timeout=self.timeout,
                sse_read_timeout=self.sse_read_timeout,
            )

        if transport == "stdio":
            if not self.command:
                raise ValueError(
                    f"MCP server '{self.resolved_name()}' requires a command for stdio transport."
                )
            return StdioConnectionParams(
                server_params=StdioServerParameters(
                    command=self.command,
                    args=self.args,
                    env=self.env,
                    cwd=self.cwd,
                    encoding=self.encoding,
                    encoding_error_handler=self.encoding_error_handler,
                ),
                timeout=self.timeout,
            )

        raise ValueError(
            f"MCP server '{self.resolved_name()}' uses unsupported transport '{self.transport}'."
        )

    def normalized_allowed_tools(self) -> set[str]:
        return {
            normalize_identifier(tool_name)
            for tool_name in self.allowed_tools
            if tool_name and tool_name.strip()
        }

    def normalized_blocked_tools(self) -> set[str]:
        return {
            normalize_identifier(tool_name)
            for tool_name in self.blocked_tools
            if tool_name and tool_name.strip()
        }

    def normalized_allowed_plugins(self) -> set[str]:
        return {
            normalize_identifier(plugin_name)
            for plugin_name in self.allowed_plugins
            if plugin_name and plugin_name.strip()
        }

    def normalized_blocked_plugins(self) -> set[str]:
        return {
            normalize_identifier(plugin_name)
            for plugin_name in self.blocked_plugins
            if plugin_name and plugin_name.strip()
        }


class AgentModelConfig(BaseModel):
    model_config = ConfigDict(extra="ignore", populate_by_name=True)

    temperature: float = 0
    mcp_servers: list[McpServerConfig] | None = Field(
        default=None,
        validation_alias=AliasChoices("mcp_servers", "mcpServers"),
    )


class AgentRuntimeConfig(BaseModel):
    model_config = ConfigDict(extra="ignore")

    prompt: str
    config: AgentModelConfig = Field(default_factory=AgentModelConfig)

    @property
    def temperature(self) -> float:
        return self.config.temperature


def build_legacy_mcp_servers() -> list[McpServerConfig]:
    return [
        McpServerConfig(
            name="knowledge_base",
            transport="streamable_http",
            url=os.getenv("INTERNAL_MCP_URL") or "http://localhost:8011/mcp",
        ),
        McpServerConfig(
            name="atlassian",
            transport="streamable_http",
            url=os.getenv("ATLASSIAN_MCP_URL") or "http://localhost:9002/mcp/",
        ),
    ]


def resolve_mcp_servers(runtime_config: AgentRuntimeConfig) -> list[McpServerConfig]:
    configured_servers = runtime_config.config.mcp_servers
    if configured_servers is None:
        return [server for server in build_legacy_mcp_servers() if server.enabled]
    return [server for server in configured_servers if server.enabled]


def matches_tool_filters(
    tool_name: str,
    tool_meta: Any,
    server_config: McpServerConfig,
) -> bool:
    normalized_tool_name = normalize_identifier(tool_name)
    allowed_tools = server_config.normalized_allowed_tools()
    blocked_tools = server_config.normalized_blocked_tools()
    allowed_plugins = server_config.normalized_allowed_plugins()
    blocked_plugins = server_config.normalized_blocked_plugins()
    plugin_aliases = extract_tool_plugin_aliases(tool_name, tool_meta)

    if allowed_tools and normalized_tool_name not in allowed_tools:
        return False
    if normalized_tool_name in blocked_tools:
        return False
    if allowed_plugins and not (plugin_aliases & allowed_plugins):
        return False
    if blocked_plugins and (plugin_aliases & blocked_plugins):
        return False
    return True
