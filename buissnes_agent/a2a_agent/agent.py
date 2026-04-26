import asyncio
import json
import logging
import os
import re

from collections import Counter
from collections.abc import AsyncIterable, Callable
from dataclasses import dataclass, field
from typing import Any, Literal, TypedDict

import httpx
from google.adk.tools.mcp_tool.mcp_tool import McpTool
from google.adk.tools.mcp_tool.mcp_toolset import McpToolset
from langchain_core.messages import AIMessage, BaseMessage, ToolMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.config import get_stream_writer
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel, Field, create_model

try:
    from . import patch_pydantic  # noqa: F401
    from .mcp_config import (
        AgentRuntimeConfig,
        McpServerConfig,
        expand_env_vars,
        matches_tool_filters,
        resolve_mcp_servers,
    )
except ImportError:
    from buissnes_agent.a2a_agent import patch_pydantic  # type: ignore  # noqa: F401
    from buissnes_agent.a2a_agent.mcp_config import (  # type: ignore
        AgentRuntimeConfig,
        McpServerConfig,
        expand_env_vars,
        matches_tool_filters,
        resolve_mcp_servers,
    )


logger = logging.getLogger(__name__)
memory = MemorySaver()

DEFAULT_AGENT_SETTINGS = 'Analyst agent'
SSL_VERIFY = os.getenv('SSL_VERIFY', 'False').lower() in ('true', '1', 't')

MAX_STATUS_TEXT_LENGTH = 280
MAX_TOOL_ARG_PREVIEW_LENGTH = 220
MAX_TOOL_RESULT_PREVIEW_LENGTH = 200
LANGFUSE_TRACE_ID_PATTERN = re.compile(r'^[0-9a-f]{32}$')


def get_agent_settings_name() -> str:
    configured_name = os.getenv('AGENT_SETTINGS')
    if configured_name is None:
        return DEFAULT_AGENT_SETTINGS
    return configured_name


class AgentStreamItem(TypedDict, total=False):
    content: str
    status_message: str
    task_state: Literal['working', 'completed', 'input_required', 'failed']
    is_task_complete: bool
    require_user_input: bool
    metadata: dict[str, Any]


class ResponseFormat(BaseModel):
    """Respond to the user in this format."""

    status: Literal['input_required', 'completed', 'error'] = 'input_required'
    message: str


@dataclass(slots=True)
class LangfuseRequest:
    input_text: str
    session_id: str
    trace_name: str = 'Deep Research Agent request'
    trace_id: str | None = None
    user_id: str | None = None
    tags: list[str] = field(default_factory=lambda: ['a2a', 'langgraph'])
    trace_metadata: dict[str, str] = field(default_factory=dict)
    observation_metadata: dict[str, Any] = field(default_factory=dict)
    langchain_metadata: dict[str, Any] = field(default_factory=dict)


def _langfuse_requested() -> bool:
    enabled = os.getenv('LANGFUSE_ENABLED')
    if enabled is not None and enabled.lower() in {'0', 'false', 'no', 'off'}:
        return False

    return bool(
        os.getenv('LANGFUSE_PUBLIC_KEY') and os.getenv('LANGFUSE_SECRET_KEY')
    )


def _truncate_text(
    value: str,
    *,
    limit: int,
    suffix: str = '...',
) -> str:
    text = ' '.join(value.split())
    if len(text) <= limit:
        return text
    return text[: limit - len(suffix)].rstrip() + suffix


def _preview_json(
    value: Any,
    *,
    limit: int,
) -> str:
    try:
        text = json.dumps(value, default=str, ensure_ascii=True, sort_keys=True)
    except TypeError:
        text = str(value)
    return _truncate_text(text, limit=limit)


def _extract_message_text(message: BaseMessage) -> str:
    content = getattr(message, 'content', '')
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        text_parts: list[str] = []
        for block in content:
            if isinstance(block, str):
                text_parts.append(block)
                continue
            if isinstance(block, dict) and block.get('type') == 'text':
                text = block.get('text')
                if isinstance(text, str):
                    text_parts.append(text)
        return ' '.join(part.strip() for part in text_parts if part).strip()
    return str(content).strip()


def _message_key(message: BaseMessage) -> str:
    message_id = getattr(message, 'id', None)
    if message_id:
        return str(message_id)

    if isinstance(message, AIMessage):
        return _preview_json(
            {
                'type': 'ai',
                'content': _extract_message_text(message),
                'tool_calls': message.tool_calls,
            },
            limit=512,
        )

    if isinstance(message, ToolMessage):
        return _preview_json(
            {
                'type': 'tool',
                'tool_call_id': message.tool_call_id,
                'status': message.status,
                'content': _extract_message_text(message),
            },
            limit=512,
        )

    return _preview_json(
        {'type': getattr(message, 'type', 'unknown'), 'content': str(message)},
        limit=512,
    )


def _is_valid_langfuse_trace_id(value: str | None) -> bool:
    return bool(value and LANGFUSE_TRACE_ID_PATTERN.fullmatch(value))


def _expand_langchain_prompt_messages(messages: list[Any]) -> list[Any]:
    expanded_messages: list[Any] = []
    for message in messages:
        if (
            isinstance(message, tuple)
            and len(message) == 2
            and isinstance(message[1], str)
        ):
            expanded_messages.append((message[0], expand_env_vars(message[1])))
            continue
        expanded_messages.append(message)
    return expanded_messages


class McpToolWrapper(BaseTool):
    """Wrapper for Google ADK MCP Tool to be compatible with LangChain."""

    mcp_tool: Any = Field(exclude=True)

    def __init__(self, mcp_tool: McpTool):
        super().__init__(
            name=mcp_tool.name,
            description=mcp_tool.description or '',
            mcp_tool=mcp_tool,
        )
        self.args_schema = self._create_args_schema(mcp_tool)

    def _create_args_schema(self, mcp_tool: McpTool) -> type[BaseModel]:
        """Create Pydantic model from JSON schema."""
        schema = mcp_tool.raw_mcp_tool.inputSchema
        if not schema or 'properties' not in schema:
            return create_model(f'{mcp_tool.name}Model')

        fields = {}
        required = set(schema.get('required', []))

        type_mapping = {
            'string': str,
            'integer': int,
            'number': float,
            'boolean': bool,
            'array': list,
            'object': dict,
            'null': type(None),
        }

        for prop_name, prop_def in schema['properties'].items():
            prop_type = type_mapping.get(prop_def.get('type'), Any)
            field_info = {}
            if 'description' in prop_def:
                field_info['description'] = prop_def['description']

            if prop_name in required:
                fields[prop_name] = (prop_type, Field(**field_info))
            else:
                fields[prop_name] = (
                    prop_type | None,
                    Field(default=None, **field_info),
                )

        return create_model(f'{mcp_tool.name}Model', **fields)

    def _run(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError('MCP tools must be run asynchronously')

    def _emit_tool_event(self, payload: dict[str, Any]) -> None:
        try:
            writer = get_stream_writer()
        except RuntimeError:
            return
        writer(payload)

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        clean_kwargs = {
            key: value for key, value in kwargs.items() if value is not None
        }
        self._emit_tool_event(
            {
                'event': 'tool_started',
                'tool_name': self.name,
                'tool_args': clean_kwargs,
            }
        )

        try:
            result = await self.mcp_tool.run_async(
                args=clean_kwargs,
                tool_context=None,
            )
        except Exception as exc:
            self._emit_tool_event(
                {
                    'event': 'tool_failed',
                    'tool_name': self.name,
                    'tool_args': clean_kwargs,
                    'error_type': type(exc).__name__,
                    'error_message': _truncate_text(
                        str(exc),
                        limit=MAX_TOOL_RESULT_PREVIEW_LENGTH,
                    ),
                }
            )
            raise

        self._emit_tool_event(
            {
                'event': 'tool_finished',
                'tool_name': self.name,
                'tool_args': clean_kwargs,
                'result_preview': _preview_json(
                    result,
                    limit=MAX_TOOL_RESULT_PREVIEW_LENGTH,
                ),
            }
        )
        return result


class AnalysisAgent:
    """Analysis Agent for system analysis and research tasks."""

    FORMAT_INSTRUCTION = (
        'Set response status to input_required if the user needs to provide more '
        'information to complete the request. '
        'Set response status to error if there is an error while processing the request. '
        'Set response status to completed if the request is complete.'
    )

    SUPPORTED_CONTENT_TYPES = ['text']

    def __init__(self) -> None:
        self.model: ChatOpenAI | None = None
        self.tools: list[BaseTool] = []
        self.graph = None
        self.runtime_config: AgentRuntimeConfig | None = None
        self.config_fingerprint: str | None = None
        self.toolsets: list[McpToolset] = []
        self._stale_toolsets: list[McpToolset] = []
        self._active_streams = 0
        self._init_lock = asyncio.Lock()
        self._sync_http_client = httpx.Client(verify=SSL_VERIFY)
        self._async_http_client = httpx.AsyncClient(verify=SSL_VERIFY)
        self._refresh_task: asyncio.Task[None] | None = None
        self._refresh_stop_event: asyncio.Event | None = None
        self._langfuse_initialized = False
        self.langfuse_enabled = False
        self.langfuse = None
        self._langfuse_prompt = None
        self._langfuse_callback_handler_cls = None
        self._langfuse_propagate_attributes = None
        self._last_prompt_source = 'local_default'
        self._runtime_config_listeners: list[
            Callable[[AgentRuntimeConfig], None]
        ] = []

    def _initialize_langfuse(self) -> None:
        if self._langfuse_initialized:
            return

        self._langfuse_initialized = True
        if not _langfuse_requested():
            logger.info(
                'Langfuse is disabled because credentials are not configured.'
            )
            return

        try:
            from langfuse import get_client, propagate_attributes
            from langfuse.langchain import CallbackHandler
        except Exception as exc:
            logger.exception(
                'Failed to import Langfuse. Continuing without tracing: %s',
                exc,
            )
            return

        try:
            client = get_client()
            if not client.auth_check():
                logger.warning(
                    'Langfuse credentials are configured, but authentication failed. '
                    'Continuing without tracing.'
                )
                return
            self.langfuse = client
            self._langfuse_callback_handler_cls = CallbackHandler
            self._langfuse_propagate_attributes = propagate_attributes
            self.langfuse_enabled = True
            logger.info('Langfuse is authenticated and ready.')
        except Exception as exc:
            logger.exception(
                'Failed to initialize Langfuse. Continuing without tracing: %s',
                exc,
            )

    def create_langfuse_trace_id(self, seed: str | None) -> str | None:
        if not seed:
            return None

        self._initialize_langfuse()
        if not self.langfuse_enabled or self.langfuse is None:
            return None

        try:
            return self.langfuse.create_trace_id(seed=seed)
        except Exception:
            logger.exception(
                'Failed to create a deterministic Langfuse trace id for seed %r.',
                seed,
            )
            return None

    def _create_langfuse_handler(
        self,
        *,
        trace_context: dict[str, str] | None = None,
    ):
        if (
            not self.langfuse_enabled
            or self._langfuse_callback_handler_cls is None
        ):
            return None

        try:
            return self._langfuse_callback_handler_cls(
                trace_context=trace_context
            )
        except Exception:
            logger.exception(
                'Failed to create a Langfuse callback handler for a request.'
            )
            return None

    def _stream_item(
        self,
        content: str,
        *,
        status_message: str | None = None,
        task_state: Literal[
            'working',
            'completed',
            'input_required',
            'failed',
        ] = 'working',
        metadata: dict[str, Any] | None = None,
        truncate_content: bool = True,
    ) -> AgentStreamItem:
        if truncate_content:
            message = _truncate_text(content, limit=MAX_STATUS_TEXT_LENGTH)
        else:
            message = content
        normalized_metadata = dict(metadata or {})
        item: AgentStreamItem = {
            'content': message,
            'task_state': task_state,
            'is_task_complete': task_state == 'completed',
            'require_user_input': task_state == 'input_required',
            'metadata': normalized_metadata,
        }
        if status_message is not None:
            normalized_status_message = str(status_message).strip()
            if normalized_status_message:
                item['status_message'] = normalized_status_message
        return item

    def _load_runtime_config(self) -> AgentRuntimeConfig:
        self._initialize_langfuse()
        self._langfuse_prompt = None
        if self.langfuse_enabled and self.langfuse is not None:
            agent_settings = get_agent_settings_name()
            try:
                prompt = self.langfuse.get_prompt(
                    agent_settings,
                    label='production',
                )
                self._langfuse_prompt = prompt
                self._last_prompt_source = 'langfuse'
                return AgentRuntimeConfig(
                    prompt=expand_env_vars(prompt.prompt),
                    config=expand_env_vars(prompt.config or {}),
                )
            except Exception:
                if self.runtime_config is not None:
                    logger.exception(
                        "Failed to load Langfuse prompt '%s'. Reusing the last applied configuration.",
                        agent_settings,
                    )
                    return self.runtime_config
                logger.exception(
                    "Failed to load Langfuse prompt '%s'. Falling back to local config.",
                    agent_settings,
                )

        with open(
            os.path.join(os.path.dirname(__file__), 'default_config.json'),
            encoding='utf-8',
        ) as config_file:
            agent_config = json.load(config_file)

        self._last_prompt_source = 'local_default'
        return AgentRuntimeConfig(
            prompt=expand_env_vars(agent_config['prompt']),
            config=expand_env_vars(agent_config.get('config') or {}),
        )

    def _build_agent_prompt(self, prompt_text: str) -> Any:
        langfuse_prompt = self._langfuse_prompt
        if (
            langfuse_prompt is None
            or not hasattr(langfuse_prompt, 'get_langchain_prompt')
        ):
            return prompt_text

        try:
            langchain_prompt = langfuse_prompt.get_langchain_prompt()
        except Exception:
            logger.exception(
                'Failed to convert the Langfuse prompt into a LangChain '
                'prompt template. Falling back to the plain system prompt.'
            )
            return prompt_text

        prompt_metadata = {'langfuse_prompt': langfuse_prompt}

        if isinstance(langchain_prompt, list):
            prompt_messages = _expand_langchain_prompt_messages(
                list(langchain_prompt)
            )
            if not any(
                isinstance(message, MessagesPlaceholder)
                and message.variable_name == 'messages'
                for message in prompt_messages
            ):
                prompt_messages.append(MessagesPlaceholder('messages'))
            return ChatPromptTemplate(
                messages=prompt_messages,
                metadata=prompt_metadata,
            )

        return ChatPromptTemplate(
            messages=[
                ('system', expand_env_vars(langchain_prompt)),
                MessagesPlaceholder('messages'),
            ],
            metadata=prompt_metadata,
        )

    def load_runtime_config_snapshot(self) -> AgentRuntimeConfig:
        return self._load_runtime_config()

    def register_runtime_config_listener(
        self,
        listener: Callable[[AgentRuntimeConfig], None],
    ) -> None:
        self._runtime_config_listeners.append(listener)

    def _notify_runtime_config_listeners(
        self,
        runtime_config: AgentRuntimeConfig,
    ) -> None:
        for listener in list(self._runtime_config_listeners):
            try:
                listener(runtime_config)
            except Exception:
                logger.exception(
                    'A runtime configuration listener failed while applying updated settings.'
                )

    async def _load_server_tools(
        self,
        server_config: McpServerConfig,
    ) -> tuple[McpToolset, list[McpTool], list[BaseTool]]:
        toolset = McpToolset(
            connection_params=server_config.build_connection_params(),
            tool_name_prefix=server_config.tool_name_prefix,
        )
        raw_tools = await toolset.get_tools()
        filtered_tools = self._filter_tools(raw_tools, server_config)
        wrapped_tools = [McpToolWrapper(tool) for tool in filtered_tools]
        return toolset, raw_tools, wrapped_tools

    async def initialize(self) -> list[AgentStreamItem]:
        async with self._init_lock:
            if self.graph is not None and self.config_fingerprint is None:
                return []

            runtime_config = self._load_runtime_config()
            config_fingerprint = json.dumps(
                runtime_config.model_dump(mode='json', exclude_none=True),
                sort_keys=True,
            )
            if (
                self.graph is not None
                and self.config_fingerprint == config_fingerprint
            ):
                return []

            events: list[AgentStreamItem] = []
            if self.graph is None:
                events.append(
                    self._stream_item(
                        'Initializing agent runtime...',
                        metadata={'phase': 'initializing'},
                    )
                )
            else:
                events.append(
                    self._stream_item(
                        'Detected updated settings. Applying hot reload...',
                        metadata={'phase': 'reloading'},
                    )
                )

            new_toolsets: list[McpToolset] = []
            new_tools: list[BaseTool] = []
            try:
                for server_config in resolve_mcp_servers(runtime_config):
                    server_name = server_config.resolved_name()
                    events.append(
                        self._stream_item(
                            f"Connecting to {server_name} tools...",
                            metadata={
                                'phase': 'initializing',
                                'tool_source': server_name,
                            },
                        )
                    )
                    try:
                        toolset, raw_tools, wrapped_tools = (
                            await self._load_server_tools(server_config)
                        )
                        if not wrapped_tools:
                            await toolset.close()
                            events.append(
                                self._stream_item(
                                    (
                                        f'{server_name} exposed no usable tools after '
                                        'applying filters.'
                                    ),
                                    metadata={
                                        'phase': 'initializing',
                                        'severity': 'warning',
                                        'tool_source': server_name,
                                        'raw_tool_count': len(raw_tools),
                                    },
                                )
                            )
                            continue

                        new_toolsets.append(toolset)
                        new_tools.extend(wrapped_tools)
                        events.append(
                            self._stream_item(
                                (
                                    f'{server_name} tools ready '
                                    f'({len(wrapped_tools)} new tools, {len(new_tools)} total).'
                                ),
                                metadata={
                                    'phase': 'initializing',
                                    'tool_source': server_name,
                                    'tool_count': len(wrapped_tools),
                                    'raw_tool_count': len(raw_tools),
                                    'total_tool_count': len(new_tools),
                                },
                            )
                        )
                    except Exception as exc:
                        logger.exception(
                            "Failed to load tools from MCP server '%s': %s",
                            server_name,
                            exc,
                        )
                        events.append(
                            self._stream_item(
                                (
                                    f'{server_name} tools are unavailable right now; '
                                    'continuing with the remaining runtime.'
                                ),
                                metadata={
                                    'phase': 'initializing',
                                    'severity': 'warning',
                                    'tool_source': server_name,
                                    'warning_type': type(exc).__name__,
                                },
                            )
                        )

                new_model = self._create_model(runtime_config)
                new_graph = create_react_agent(
                    new_model,
                    tools=new_tools,
                    checkpointer=memory,
                    prompt=self._build_agent_prompt(runtime_config.prompt),
                    response_format=(self.FORMAT_INSTRUCTION, ResponseFormat),
                )
            except Exception:
                await self._close_toolsets(new_toolsets)
                if self.graph is None:
                    raise
                logger.exception(
                    'Failed to refresh agent configuration. Keeping the previous graph.'
                )
                events.append(
                    self._stream_item(
                        (
                            'Updated settings could not be applied; continuing '
                            'with the previous runtime.'
                        ),
                        metadata={
                            'phase': 'reloading',
                            'severity': 'warning',
                        },
                    )
                )
                return events

            previous_toolsets = list(self.toolsets)
            self.runtime_config = runtime_config
            self.config_fingerprint = config_fingerprint
            self.model = new_model
            self.tools = new_tools
            self.graph = new_graph
            self.toolsets = new_toolsets
            self._log_duplicate_tool_names()
            self._notify_runtime_config_listeners(runtime_config)

            if previous_toolsets:
                self._stale_toolsets.extend(previous_toolsets)

            await self._maybe_close_stale_toolsets()
            events.append(
                self._stream_item(
                    (
                        'Agent runtime ready. '
                        f'Prompt source: {self._last_prompt_source}. '
                        f'Total tools available: {len(self.tools)}.'
                    ),
                    metadata={
                        'phase': 'initializing',
                        'prompt_source': self._last_prompt_source,
                        'tool_count': len(self.tools),
                    },
                )
            )
            return events

    def _filter_tools(
        self,
        server_tools: list[McpTool],
        server_config: McpServerConfig,
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
                ', '.join(sorted(skipped_tool_names)),
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
                'DEFAULT_HEADERS is not valid JSON. Ignoring the value.'
            )
            return {}

        if not isinstance(parsed_headers, dict):
            logger.warning(
                'DEFAULT_HEADERS must be a JSON object. Ignoring the value.'
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
                'Duplicate MCP tool names detected: %s. '
                'Consider setting tool_name_prefix in the Langfuse MCP config.',
                ', '.join(duplicates),
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
                logger.exception('Failed to close an MCP toolset cleanly')

    def get_refresh_interval_seconds(self) -> float:
        raw_value = os.getenv('AGENT_SETTINGS_REFRESH_INTERVAL_SECONDS', '30')
        try:
            interval_seconds = float(raw_value)
        except ValueError:
            logger.warning(
                'AGENT_SETTINGS_REFRESH_INTERVAL_SECONDS=%r is invalid. '
                'Falling back to 30 seconds.',
                raw_value,
            )
            return 30.0

        if interval_seconds < 0:
            logger.warning(
                'AGENT_SETTINGS_REFRESH_INTERVAL_SECONDS=%s is negative. '
                'Disabling automatic refresh.',
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
            logger.info('Automatic agent settings refresh is disabled.')
            return

        if self._refresh_task is not None and not self._refresh_task.done():
            return

        self._refresh_stop_event = asyncio.Event()
        self._refresh_task = asyncio.create_task(
            self._auto_refresh_loop(interval_seconds),
            name='analysis-agent-settings-refresh',
        )
        logger.info(
            'Automatic agent settings refresh is enabled every %s seconds.',
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
                logger.exception('Automatic agent settings refresh failed.')

    async def close(self) -> None:
        await self.stop_auto_refresh()
        await self._close_toolsets(list(self.toolsets))
        self.toolsets = []
        await self._close_toolsets(list(self._stale_toolsets))
        self._stale_toolsets = []
        if self.langfuse is not None:
            try:
                self.langfuse.flush()
            except Exception:
                logger.exception('Failed to flush Langfuse before shutdown.')
        await self._async_http_client.aclose()
        self._sync_http_client.close()
        self.graph = None
        self.model = None
        self.tools = []

    def _map_custom_event(
        self,
        payload: dict[str, Any],
    ) -> list[AgentStreamItem]:
        event = payload.get('event')
        tool_name = str(payload.get('tool_name', 'tool'))
        tool_args = payload.get('tool_args')
        args_preview = (
            _preview_json(tool_args, limit=MAX_TOOL_ARG_PREVIEW_LENGTH)
            if tool_args
            else ''
        )

        if event == 'tool_started':
            content = f'Running tool {tool_name}.'
            if args_preview:
                content = f'{content} Arguments: {args_preview}'
            return [
                self._stream_item(
                    content,
                    metadata={
                        'phase': 'tool_started',
                        'tool_name': tool_name,
                        'tool_args': tool_args or {},
                    },
                )
            ]

        if event == 'tool_finished':
            result_preview = str(payload.get('result_preview', '')).strip()
            content = f'Finished tool {tool_name}.'
            if result_preview:
                content = f'{content} Result preview: {result_preview}'
            return [
                self._stream_item(
                    content,
                    metadata={
                        'phase': 'tool_finished',
                        'tool_name': tool_name,
                        'tool_args': tool_args or {},
                    },
                )
            ]

        if event == 'tool_failed':
            error_message = str(payload.get('error_message', 'Unknown tool error'))
            return [
                self._stream_item(
                    f'Tool {tool_name} failed: {error_message}',
                    metadata={
                        'phase': 'tool_failed',
                        'tool_name': tool_name,
                        'tool_args': tool_args or {},
                        'error_type': payload.get('error_type'),
                    },
                )
            ]

        return []

    def _map_update_event(
        self,
        payload: dict[str, Any],
        *,
        seen_message_keys: set[str],
    ) -> list[AgentStreamItem]:
        updates: list[AgentStreamItem] = []

        for node_name, node_update in payload.items():
            if not isinstance(node_update, dict):
                continue

            messages = node_update.get('messages')
            if not isinstance(messages, list) or not messages:
                continue

            message = messages[-1]
            if not isinstance(message, BaseMessage):
                continue

            key = _message_key(message)
            if key in seen_message_keys:
                continue
            seen_message_keys.add(key)

            if isinstance(message, AIMessage):
                if message.tool_calls:
                    tool_names = ', '.join(
                        str(tool_call.get('name', 'tool'))
                        for tool_call in message.tool_calls[:3]
                    )
                    if len(message.tool_calls) > 3:
                        tool_names += ', ...'
                    updates.append(
                        self._stream_item(
                            f'Planning the next action: {tool_names}.',
                            metadata={
                                'phase': 'planning',
                                'node_name': node_name,
                                'tool_call_count': len(message.tool_calls),
                            },
                        )
                    )
                elif _extract_message_text(message):
                    updates.append(
                        self._stream_item(
                            'Drafting the final response...',
                            metadata={
                                'phase': 'finalizing',
                                'node_name': node_name,
                            },
                        )
                    )
                continue

            if isinstance(message, ToolMessage):
                phase = 'tool_result'
                content = 'Reviewing tool results...'
                if message.status == 'error':
                    phase = 'tool_result_error'
                    content = 'A tool returned an error. Re-evaluating the plan...'
                updates.append(
                    self._stream_item(
                        content,
                        metadata={
                            'phase': phase,
                            'node_name': node_name,
                            'tool_call_id': message.tool_call_id,
                        },
                    )
                )

        return updates

    def _map_graph_chunk(
        self,
        chunk: dict[str, Any],
        *,
        seen_message_keys: set[str],
    ) -> list[AgentStreamItem]:
        event_type = chunk.get('type')
        payload = chunk.get('data')

        if event_type == 'custom' and isinstance(payload, dict):
            return self._map_custom_event(payload)

        if event_type == 'updates' and isinstance(payload, dict):
            return self._map_update_event(
                payload,
                seen_message_keys=seen_message_keys,
            )

        return []

    def _request_trace(
        self,
        langfuse_request: LangfuseRequest | None,
    ) -> tuple[Any | None, Any | None]:
        self._initialize_langfuse()
        if (
            langfuse_request is None
            or not self.langfuse_enabled
            or self.langfuse is None
        ):
            return None, None

        trace_context = None
        if langfuse_request.trace_id:
            if _is_valid_langfuse_trace_id(langfuse_request.trace_id):
                trace_context = {'trace_id': langfuse_request.trace_id}
            else:
                logger.warning(
                    'Ignoring invalid explicit Langfuse trace id: %r',
                    langfuse_request.trace_id,
                )
        propagation_kwargs: dict[str, Any] = {}
        if langfuse_request.user_id:
            propagation_kwargs['user_id'] = langfuse_request.user_id
        if langfuse_request.session_id:
            propagation_kwargs['session_id'] = langfuse_request.session_id
        if langfuse_request.trace_metadata:
            propagation_kwargs['metadata'] = langfuse_request.trace_metadata
        if langfuse_request.tags:
            propagation_kwargs['tags'] = langfuse_request.tags
        if langfuse_request.trace_name:
            propagation_kwargs['trace_name'] = langfuse_request.trace_name

        try:
            if self._langfuse_propagate_attributes is not None:
                with self._langfuse_propagate_attributes(**propagation_kwargs):
                    root_span = self.langfuse.start_observation(
                        name=langfuse_request.trace_name,
                        as_type='span',
                        trace_context=trace_context,
                        input=langfuse_request.input_text,
                        metadata=langfuse_request.observation_metadata or None,
                    )
            else:
                root_span = self.langfuse.start_observation(
                    name=langfuse_request.trace_name,
                    as_type='span',
                    trace_context=trace_context,
                    input=langfuse_request.input_text,
                    metadata=langfuse_request.observation_metadata or None,
                )
        except Exception:
            logger.exception('Failed to create a Langfuse request span.')
            return None, None

        self._set_request_trace_io(
            root_span,
            input_text=langfuse_request.input_text,
        )
        handler = self._create_langfuse_handler(
            trace_context={
                'trace_id': root_span.trace_id,
                'parent_span_id': root_span.id,
            }
        )
        return root_span, handler

    def _set_request_trace_io(
        self,
        root_span: Any,
        *,
        input_text: str | None = None,
        output: str | None = None,
    ) -> None:
        if root_span is None or not hasattr(root_span, 'set_trace_io'):
            return

        update_payload: dict[str, Any] = {}
        if input_text is not None:
            update_payload['input'] = input_text
        if output is not None:
            update_payload['output'] = output
        if not update_payload:
            return

        try:
            root_span.set_trace_io(**update_payload)
        except Exception:
            logger.exception(
                'Failed to update trace-level Langfuse input/output.'
            )

    def _update_request_trace(
        self,
        root_span: Any,
        *,
        output: str | None = None,
        task_state: str | None = None,
        metadata: dict[str, Any] | None = None,
        level: str | None = None,
        status_message: str | None = None,
    ) -> None:
        update_payload: dict[str, Any] = {}
        if output is not None:
            update_payload['output'] = output
            self._set_request_trace_io(root_span, output=output)
        merged_metadata = dict(metadata or {})
        if task_state:
            merged_metadata.setdefault('task_state', task_state)
        if self._last_prompt_source:
            merged_metadata.setdefault('prompt_source', self._last_prompt_source)
        if merged_metadata:
            update_payload['metadata'] = merged_metadata
        if level is not None:
            update_payload['level'] = level
        if status_message is not None:
            update_payload['status_message'] = status_message

        if not update_payload:
            return

        try:
            root_span.update(**update_payload)
        except Exception:
            logger.exception('Failed to update the Langfuse request span.')

    def _end_request_trace(self, root_span: Any) -> None:
        if root_span is None:
            return

        try:
            root_span.end()
        except Exception:
            logger.exception('Failed to close the Langfuse request span.')

    def _build_graph_config(
        self,
        context_id: str,
        *,
        langfuse_request: LangfuseRequest | None = None,
        langfuse_handler: Any = None,
    ) -> dict[str, Any]:
        metadata: dict[str, Any] = {}
        if langfuse_request is not None:
            metadata.update(langfuse_request.langchain_metadata)
            metadata['langfuse_session_id'] = langfuse_request.session_id
            if langfuse_request.user_id:
                metadata['langfuse_user_id'] = langfuse_request.user_id
            if langfuse_request.tags:
                metadata['langfuse_tags'] = langfuse_request.tags

        config: dict[str, Any] = {
            'configurable': {
                'thread_id': context_id,
            },
            'callbacks': [langfuse_handler] if langfuse_handler else [],
            'metadata': metadata,
        }
        if langfuse_request is not None and langfuse_request.trace_name:
            config['run_name'] = langfuse_request.trace_name

        return config

    async def stream(
        self,
        query: str,
        context_id: str,
        *,
        langfuse_request: LangfuseRequest | None = None,
    ) -> AsyncIterable[AgentStreamItem]:
        self._active_streams += 1
        root_span = None
        try:
            request_trace = langfuse_request or LangfuseRequest(
                input_text=query,
                session_id=context_id,
            )
            root_span, langfuse_handler = self._request_trace(request_trace)

            try:
                for item in await self.initialize():
                    yield item

                if root_span is not None:
                    self._update_request_trace(
                        root_span,
                        metadata={'phase': 'initialized'},
                    )

                if self.graph is None:
                    raise RuntimeError('Agent graph was not initialized.')

                inputs = {'messages': [('user', query)]}
                config = self._build_graph_config(
                    context_id,
                    langfuse_request=request_trace,
                    langfuse_handler=langfuse_handler,
                )
                seen_message_keys: set[str] = set()

                async for chunk in self.graph.astream(
                    inputs,
                    config,
                    stream_mode=['updates', 'custom'],
                    version='v2',
                ):
                    for item in self._map_graph_chunk(
                        chunk,
                        seen_message_keys=seen_message_keys,
                    ):
                        yield item

                final_item = await self.get_agent_response(config)
                if root_span is not None:
                    self._update_request_trace(
                        root_span,
                        output=final_item.get('content'),
                        task_state=final_item.get('task_state'),
                        metadata=final_item.get('metadata'),
                    )
                yield final_item
            except Exception as exc:
                if root_span is not None:
                    self._update_request_trace(
                        root_span,
                        output=str(exc),
                        task_state='failed',
                        metadata={'phase': 'failed'},
                        level='ERROR',
                        status_message=str(exc),
                    )
                raise
        finally:
            self._end_request_trace(root_span)
            self._active_streams -= 1
            await self._maybe_close_stale_toolsets()

    async def get_agent_response(
        self,
        config: dict[str, Any],
    ) -> AgentStreamItem:
        if self.graph is None:
            raise RuntimeError('Agent graph was not initialized.')

        current_state = await self.graph.aget_state(config)
        last_ai_message = ''
        messages = current_state.values.get('messages', [])

        for message in reversed(messages):
            if getattr(message, 'type', '') == 'human':
                break
            if isinstance(message, AIMessage):
                last_ai_message = _extract_message_text(message)
                if last_ai_message:
                    break

        structured_response = current_state.values.get('structured_response')
        final_content = last_ai_message
        final_status_message: str | None = None
        final_state: Literal[
            'working',
            'completed',
            'input_required',
            'failed',
        ] = 'input_required'

        if structured_response and isinstance(structured_response, ResponseFormat):
            structured_message = structured_response.message.strip()

            if structured_response.status == 'completed':
                final_state = 'completed'
                final_content = last_ai_message or structured_message
            elif structured_response.status == 'error':
                final_state = 'failed'
                final_content = structured_message or last_ai_message
            else:
                final_state = 'input_required'
                final_content = structured_message or last_ai_message

            final_status_message = structured_message or final_content

            return self._stream_item(
                final_content or 'The task finished without a response message.',
                status_message=final_status_message or final_content,
                task_state=final_state,
                metadata={
                    'phase': 'final_response',
                    'response_status': structured_response.status,
                },
                truncate_content=False,
            )

        fallback_message = final_content or (
            'We could not finish the request cleanly. Please try again.'
        )
        return self._stream_item(
            fallback_message,
            status_message=fallback_message,
            task_state='input_required',
            metadata={
                'phase': 'final_response',
                'response_status': 'fallback',
            },
            truncate_content=False,
        )
