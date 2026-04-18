import asyncio
import json
import logging
import os

from collections import Counter
from collections.abc import AsyncIterable
from typing import Any, Literal

import httpx
from google.adk.tools.mcp_tool.mcp_tool import McpTool
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.tools import BaseTool
from langfuse import get_client
from langfuse.langchain import CallbackHandler
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel, Field, create_model

try:
    from .mcp_config import (
        AgentRuntimeConfig,
        expand_env_vars,
        matches_tool_filters,
        resolve_mcp_servers,
    )
    from . import patch_pydantic  # noqa: F401
except ImportError:
    from mcp_config import (  # type: ignore
        AgentRuntimeConfig,
        expand_env_vars,
        matches_tool_filters,
        resolve_mcp_servers,
    )
    import patch_pydantic  # type: ignore  # noqa: F401

logger = logging.getLogger(__name__)
memory = MemorySaver()

AGENT_SETTINGS = os.getenv("AGENT_SETTINGS", "Analyst agent")
SSL_VERIFY = os.getenv("SSL_VERIFY", 'False').lower() in ('true', '1', 't')

langfuse = None
langfuse_enabled = False
langfuse_handler = None
langfuse_initialized = False


def _ensure_langfuse_client():
    global langfuse
    global langfuse_enabled
    global langfuse_initialized

    if langfuse_initialized:
        return langfuse, langfuse_enabled

    langfuse_initialized = True
    langfuse = get_client()
    try:
        if langfuse.auth_check():
            logger.info("Langfuse is authenticated and ready.")
            langfuse_enabled = True
        else:
            logger.warning(
                "Langfuse authentication failed. Falling back to local config."
            )
    except Exception as exc:
        logger.warning(
            "Failed to connect to Langfuse. Falling back to local config. Error: %s",
            exc,
        )

    return langfuse, langfuse_enabled


def _get_langfuse_handler():
    global langfuse_handler

    _client, enabled = _ensure_langfuse_client()
    if not enabled:
        return None

    if langfuse_handler is None:
        langfuse_handler = CallbackHandler()

    return langfuse_handler


class ResponseFormat(BaseModel):
    """Respond to the user in this format."""
    
    status: Literal['input_required', 'completed', 'error'] = 'input_required'
    message: str



class McpToolWrapper(BaseTool):
    """Wrapper for Google ADK MCP Tool to be compatible with LangChain."""
    
    mcp_tool: Any = Field(exclude=True)
    
    def __init__(self, mcp_tool: McpTool):
        """Initialize the wrapper."""
        super().__init__(
            name=mcp_tool.name,
            description=mcp_tool.description or "",
            mcp_tool=mcp_tool,
        )
        self.args_schema = self._create_args_schema(mcp_tool)

    def _create_args_schema(self, mcp_tool: McpTool) -> type[BaseModel]:
        """Create Pydantic model from JSON schema."""
        schema = mcp_tool.raw_mcp_tool.inputSchema
        if not schema or "properties" not in schema:
            return create_model(f"{mcp_tool.name}Model")
            
        fields = {}
        required = set(schema.get("required", []))
        
        type_mapping = {
            "string": str,
            "integer": int,
            "number": float,
            "boolean": bool,
            "array": list,
            "object": dict,
            "null": type(None),
        }

        for prop_name, prop_def in schema["properties"].items():
            prop_type = type_mapping.get(prop_def.get("type"), Any)
            # Handle simple description
            field_info = {}
            if "description" in prop_def:
                field_info["description"] = prop_def["description"]
            
            is_required = prop_name in required
            if is_required:
                fields[prop_name] = (prop_type, Field(**field_info))
            else:
                fields[prop_name] = (prop_type | None, Field(default=None, **field_info))
                
        return create_model(f"{mcp_tool.name}Model", **fields)

    def _run(self, *args: Any, **kwargs: Any) -> Any:
        """Run tool synchronously - not implemented for async MCP."""
        raise NotImplementedError("MCP tools must be run asynchronously")

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        """Run tool asynchronously."""
        # Remove None values so we don't send explicit nulls for optional parameters
        # which can cause validation errors on the MCP server side
        clean_kwargs = {k: v for k, v in kwargs.items() if v is not None}
        return await self.mcp_tool.run_async(args=clean_kwargs, tool_context=None)


class AnalysisAgent:
    """Analysis Agent - a specialized assistant for currency conversions."""

    FORMAT_INSTRUCTION = (
        'Set response status to input_required if the user needs to provide more information to complete the request.'
        'Set response status to error if there is an error while processing the request.'
        'Set response status to completed if the request is complete.'
    )

    def __init__(self):
        self.model = None
        self.tools = []
        self.graph = None
        self.runtime_config = None
        self.config_fingerprint = None
        self.toolsets = []
        self._stale_toolsets = []
        self._active_streams = 0
        self._init_lock = asyncio.Lock()
        self._sync_http_client = httpx.Client(verify=SSL_VERIFY)
        self._async_http_client = httpx.AsyncClient(verify=SSL_VERIFY)
        self._refresh_task = None
        self._refresh_stop_event = None

    async def initialize(self):
        async with self._init_lock:
            runtime_config = self._load_runtime_config()
            config_fingerprint = json.dumps(
                runtime_config.model_dump(mode="json", exclude_none=True),
                sort_keys=True,
            )
            if self.graph is not None and self.config_fingerprint == config_fingerprint:
                return
            if self.graph is None:
                logger.info("Initializing agent settings.")
            else:
                logger.info("Detected updated agent settings. Applying hot reload.")

            new_toolsets = []
            try:
                new_tools = await self._load_tools(runtime_config, new_toolsets)
                new_model = self._create_model(runtime_config)
                new_graph = create_react_agent(
                    new_model,
                    tools=new_tools,
                    checkpointer=memory,
                    prompt=runtime_config.prompt,
                    response_format=(self.FORMAT_INSTRUCTION, ResponseFormat),
                )
            except Exception:
                await self._close_toolsets(new_toolsets)
                if self.graph is None:
                    raise
                logger.exception(
                    "Failed to refresh agent configuration. Keeping the previous graph."
                )
                return

            previous_toolsets = list(self.toolsets)
            self.runtime_config = runtime_config
            self.config_fingerprint = config_fingerprint
            self.model = new_model
            self.tools = new_tools
            self.graph = new_graph
            self.toolsets = new_toolsets
            self._log_duplicate_tool_names()

            if previous_toolsets:
                self._stale_toolsets.extend(previous_toolsets)

            await self._maybe_close_stale_toolsets()

    def _load_runtime_config(self) -> AgentRuntimeConfig:
        langfuse_client, is_langfuse_enabled = _ensure_langfuse_client()
        if is_langfuse_enabled and langfuse_client is not None:
            try:
                prompt = langfuse_client.get_prompt(AGENT_SETTINGS, label="latest")
                return AgentRuntimeConfig(
                    prompt=expand_env_vars(prompt.prompt),
                    config=expand_env_vars(prompt.config or {}),
                )
            except Exception:
                if self.runtime_config is not None:
                    logger.exception(
                        "Failed to load Langfuse prompt '%s'. Reusing the last applied configuration.",
                        AGENT_SETTINGS,
                    )
                    return self.runtime_config
                logger.exception(
                    "Failed to load Langfuse prompt '%s'. Falling back to local default_config.json.",
                    AGENT_SETTINGS,
                )

        with open(
            os.path.join(os.path.dirname(__file__), 'default_config.json'),
            encoding='utf-8',
        ) as config_file:
            agent_config = json.load(config_file)

        return AgentRuntimeConfig(
            prompt=expand_env_vars(agent_config['prompt']),
            config=expand_env_vars(agent_config.get('config') or {}),
        )

    async def _load_tools(
        self,
        runtime_config: AgentRuntimeConfig,
        loaded_toolsets: list[McpToolset],
    ) -> list[BaseTool]:
        tools: list[BaseTool] = []

        for server_config in resolve_mcp_servers(runtime_config):
            server_name = server_config.resolved_name()
            logger.info(
                "Connecting to MCP server '%s' via %s",
                server_name,
                server_config.normalized_transport(),
            )
            try:
                toolset = McpToolset(
                    connection_params=server_config.build_connection_params(),
                    tool_name_prefix=server_config.tool_name_prefix,
                )
                server_tools = await toolset.get_tools()
                filtered_tools = self._filter_tools(server_tools, server_config)
                if not filtered_tools:
                    await toolset.close()
                    logger.info(
                        "Loaded 0/%s tools from MCP server '%s' after applying filters",
                        len(server_tools),
                        server_name,
                    )
                    continue

                loaded_toolsets.append(toolset)
                tools.extend(McpToolWrapper(tool) for tool in filtered_tools)
                logger.info(
                    "Loaded %s/%s tools from MCP server '%s'",
                    len(filtered_tools),
                    len(server_tools),
                    server_name,
                )
            except Exception as exc:
                logger.error(
                    "Failed to load tools from MCP server '%s': %s",
                    server_name,
                    exc,
                )

        return tools

    def _filter_tools(
        self,
        server_tools: list[McpTool],
        server_config,
    ) -> list[McpTool]:
        filtered_tools = []
        skipped_tool_names = []

        for tool in server_tools:
            tool_meta = getattr(tool.raw_mcp_tool, 'meta', None)
            if matches_tool_filters(tool.name, tool_meta, server_config):
                filtered_tools.append(tool)
            else:
                skipped_tool_names.append(tool.name)

        if skipped_tool_names:
            logger.info(
                "Filtered out %s tool(s) from MCP server '%s': %s",
                len(skipped_tool_names),
                server_config.resolved_name(),
                ", ".join(sorted(skipped_tool_names)),
            )

        return filtered_tools

    def _create_model(self, runtime_config: AgentRuntimeConfig) -> ChatOpenAI:
        default_headers = self._load_default_headers()
        return ChatOpenAI(
            model=os.getenv('CHAT_MODEL'),
            openai_api_key=os.getenv('CHAT_API_KEY', 'EMPTY'),
            openai_api_base=os.getenv('CHAT_BASE_URL'),
            temperature=float(runtime_config.temperature),
            tiktoken_model_name=None,
            default_headers=default_headers,
            http_client=self._sync_http_client,
            http_async_client=self._async_http_client,
        )

    def _load_default_headers(self) -> dict[str, Any]:
        raw_headers = os.getenv('DEFAULT_HEADERS')
        if not raw_headers:
            return {}

        try:
            parsed_headers = json.loads(raw_headers)
        except json.JSONDecodeError:
            logger.warning(
                "DEFAULT_HEADERS is not valid JSON. Ignoring the value."
            )
            return {}

        if not isinstance(parsed_headers, dict):
            logger.warning(
                "DEFAULT_HEADERS must be a JSON object. Ignoring the value."
            )
            return {}

        return parsed_headers

    def _log_duplicate_tool_names(self) -> None:
        duplicate_counts = Counter(tool.name for tool in self.tools)
        duplicates = sorted(
            tool_name
            for tool_name, count in duplicate_counts.items()
            if count > 1
        )
        if duplicates:
            logger.warning(
                "Duplicate MCP tool names detected: %s. Consider setting tool_name_prefix in the Langfuse MCP config.",
                ", ".join(duplicates),
            )

    async def _maybe_close_stale_toolsets(self) -> None:
        if self._active_streams != 0 or not self._stale_toolsets:
            return

        stale_toolsets = list(self._stale_toolsets)
        self._stale_toolsets.clear()
        await self._close_toolsets(stale_toolsets)

    async def _close_toolsets(self, toolsets: list[McpToolset]) -> None:
        for toolset in toolsets:
            try:
                await toolset.close()
            except Exception:
                logger.exception("Failed to close an MCP toolset cleanly")

    def get_refresh_interval_seconds(self) -> float:
        raw_value = os.getenv('AGENT_SETTINGS_REFRESH_INTERVAL_SECONDS', '30')
        try:
            interval_seconds = float(raw_value)
        except ValueError:
            logger.warning(
                "AGENT_SETTINGS_REFRESH_INTERVAL_SECONDS=%r is invalid. Falling back to 30 seconds.",
                raw_value,
            )
            return 30.0

        if interval_seconds < 0:
            logger.warning(
                "AGENT_SETTINGS_REFRESH_INTERVAL_SECONDS=%s is negative. Disabling automatic refresh.",
                raw_value,
            )
            return 0.0

        return interval_seconds

    async def start_auto_refresh(
        self,
        interval_seconds: float | None = None,
    ) -> None:
        if interval_seconds is None:
            interval_seconds = self.get_refresh_interval_seconds()

        await self.initialize()

        if interval_seconds <= 0:
            logger.info("Automatic agent settings refresh is disabled.")
            return

        if self._refresh_task is not None and not self._refresh_task.done():
            return

        self._refresh_stop_event = asyncio.Event()
        self._refresh_task = asyncio.create_task(
            self._auto_refresh_loop(interval_seconds),
            name='analysis-agent-settings-refresh',
        )
        logger.info(
            "Automatic agent settings refresh is enabled every %s seconds.",
            format(interval_seconds, 'g'),
        )

    async def stop_auto_refresh(self) -> None:
        if self._refresh_stop_event is not None:
            self._refresh_stop_event.set()

        if self._refresh_task is not None:
            try:
                await self._refresh_task
            except asyncio.CancelledError:
                pass

        self._refresh_task = None
        self._refresh_stop_event = None

    async def _auto_refresh_loop(self, interval_seconds: float) -> None:
        assert self._refresh_stop_event is not None
        stop_event = self._refresh_stop_event

        while True:
            try:
                await asyncio.wait_for(stop_event.wait(), timeout=interval_seconds)
                return
            except asyncio.TimeoutError:
                pass

            try:
                await self.initialize()
            except Exception:
                logger.exception("Automatic agent settings refresh failed.")

    async def close(self) -> None:
        await self.stop_auto_refresh()
        await self._close_toolsets(list(self.toolsets))
        self.toolsets = []
        await self._close_toolsets(list(self._stale_toolsets))
        self._stale_toolsets = []
        await self._async_http_client.aclose()
        self._sync_http_client.close()
        self.graph = None
        self.model = None
        self.tools = []

    async def stream(self, query, context_id) -> AsyncIterable[dict[str, Any]]:
        self._active_streams += 1
        try:
            await self.initialize()
            if self.graph is None:
                raise RuntimeError('Agent graph was not initialized.')

            graph = self.graph
            langfuse_callback_handler = _get_langfuse_handler()
            inputs = {'messages': [('user', query)]}
            config = {
                'configurable': {
                    'thread_id': context_id
                },
                "callbacks": [langfuse_callback_handler]
                if langfuse_callback_handler is not None
                else [],
                "metadata": {
                    "langfuse_session_id": context_id
                }
            }

            async for item in graph.astream(inputs, config, stream_mode='values'):
                message = item['messages'][-1]
                if (
                    isinstance(message, AIMessage)
                    and message.tool_calls
                    and len(message.tool_calls) > 0
                ):
                    yield {
                        'is_task_complete': False,
                        'require_user_input': False,
                        'content': f"Using tool {message.tool_calls[0]['name']} with args {message.tool_calls[0]['args']}",
                    }
                elif isinstance(message, ToolMessage):
                    yield {
                        'is_task_complete': False,
                        'require_user_input': False,
                        'content': 'Processing tool response..',
                    }

            yield self.get_agent_response(graph, config)
        finally:
            self._active_streams -= 1
            await self._maybe_close_stale_toolsets()

    def get_agent_response(self, graph, config):
        current_state = graph.get_state(config)
        
        last_ai_message = ""
        messages = current_state.values.get('messages', [])
        for msg in reversed(messages):
            if getattr(msg, 'type', '') == 'human':
                break
            if isinstance(msg, AIMessage) and getattr(msg, 'content', None):
                content = msg.content
                if isinstance(content, str):
                    last_ai_message = content.strip()
                elif isinstance(content, list):
                    texts = [b.get("text", "") for b in content if isinstance(b, dict) and b.get("type") == "text"]
                    if not texts:
                        texts = [b for b in content if isinstance(b, str)]
                    last_ai_message = " ".join(filter(None, texts)).strip()
                
                if last_ai_message:
                    break

        structured_response = current_state.values.get('structured_response')
        
        final_content = ""
        is_task_complete = False
        require_user_input = True

        if structured_response and isinstance(structured_response, ResponseFormat):
            final_content = structured_response.message
            
            # Combine if last_ai_message has additional meaningful content
            if last_ai_message and last_ai_message != structured_response.message:
                if structured_response.message in last_ai_message:
                    final_content = last_ai_message
                elif last_ai_message in structured_response.message:
                    final_content = structured_response.message
                else:
                    final_content = f"{last_ai_message}\n\n{structured_response.message}"
            
            if structured_response.status == 'input_required':
                is_task_complete = False
                require_user_input = True
            elif structured_response.status == 'error':
                is_task_complete = False
                require_user_input = True
            elif structured_response.status == 'completed':
                is_task_complete = True
                require_user_input = False
                
            return {
                'is_task_complete': is_task_complete,
                'require_user_input': require_user_input,
                'content': final_content,
            }
            
        return {
            'is_task_complete': False,
            'require_user_input': True,
            'content': last_ai_message or (
                'We are unable to process your request at the moment. '
                'Please try again.'
            ),
        }

    SUPPORTED_CONTENT_TYPES = ['text']
