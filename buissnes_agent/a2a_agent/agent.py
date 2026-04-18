import asyncio
import json
import logging
import os

from collections.abc import AsyncIterable
from typing import Any, Literal, TypedDict

import httpx
from google.adk.tools.mcp_tool.mcp_session_manager import (
    StreamableHTTPServerParams,
)
from google.adk.tools.mcp_tool.mcp_tool import McpTool
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from langchain_core.messages import AIMessage, BaseMessage, ToolMessage
from langchain_core.tools import BaseTool
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
from langgraph.config import get_stream_writer
from langgraph.prebuilt import create_react_agent
from pydantic import BaseModel, Field, create_model

try:
    from . import patch_pydantic  # noqa: F401
except ImportError:
    from buissnes_agent.a2a_agent import patch_pydantic  # type: ignore  # noqa: F401

logger = logging.getLogger(__name__)
memory = MemorySaver()

AGENT_SETTINGS = os.getenv('AGENT_SETTINGS', 'Analyst agent')
SSL_VERIFY = os.getenv('SSL_VERIFY', 'False').lower() in ('true', '1', 't')
INTERNAL_MCP_URL = os.getenv('INTERNAL_MCP_URL', 'http://localhost:8011/mcp')
ATLASSIAN_MCP_URL = os.getenv(
    'ATLASSIAN_MCP_URL', 'http://localhost:9002/mcp/'
)

MAX_STATUS_TEXT_LENGTH = 280
MAX_TOOL_ARG_PREVIEW_LENGTH = 220
MAX_TOOL_RESULT_PREVIEW_LENGTH = 200

class AgentStreamItem(TypedDict, total=False):
    content: str
    task_state: Literal['working', 'completed', 'input_required', 'failed']
    is_task_complete: bool
    require_user_input: bool
    metadata: dict[str, Any]


class ResponseFormat(BaseModel):
    """Respond to the user in this format."""

    status: Literal['input_required', 'completed', 'error'] = 'input_required'
    message: str


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
        clean_kwargs = {key: value for key, value in kwargs.items() if value is not None}
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
    """Analysis Agent - a specialized assistant for system analysis tasks."""

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
        self._initialization_lock = asyncio.Lock()
        self._langfuse_initialized = False
        self.langfuse_enabled = False
        self.langfuse = None
        self.langfuse_handler = None

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
            from langfuse import get_client
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
            self.langfuse_handler = CallbackHandler()
            self.langfuse_enabled = True
            logger.info('Langfuse is authenticated and ready.')
        except Exception as exc:
            logger.exception(
                'Failed to initialize Langfuse. Continuing without tracing: %s',
                exc,
            )

    def _stream_item(
        self,
        content: str,
        *,
        task_state: Literal[
            'working',
            'completed',
            'input_required',
            'failed',
        ] = 'working',
        metadata: dict[str, Any] | None = None,
    ) -> AgentStreamItem:
        message = _truncate_text(content, limit=MAX_STATUS_TEXT_LENGTH)
        normalized_metadata = dict(metadata or {})
        return {
            'content': message,
            'task_state': task_state,
            'is_task_complete': task_state == 'completed',
            'require_user_input': task_state == 'input_required',
            'metadata': normalized_metadata,
        }

    async def _load_toolset(
        self,
        *,
        name: str,
        url: str,
    ) -> list[BaseTool]:
        logger.info('Connecting to %s MCP at %s', name, url)
        connection_params = StreamableHTTPServerParams(url=url)
        raw_tools = await MCPToolset(
            connection_params=connection_params
        ).get_tools()
        logger.info('Loaded %s tools from %s MCP', len(raw_tools), name)
        return [McpToolWrapper(tool) for tool in raw_tools]

    async def initialize(self) -> AsyncIterable[AgentStreamItem]:
        if self.graph is not None:
            return

        async with self._initialization_lock:
            if self.graph is not None:
                return

            self.tools = []
            yield self._stream_item(
                'Initializing agent runtime...',
                metadata={'phase': 'initializing'},
            )

            yield self._stream_item(
                'Connecting to the Knowledge Base tools...',
                metadata={'phase': 'initializing', 'tool_source': 'knowledge_base'},
            )
            try:
                self.tools.extend(
                    await self._load_toolset(
                        name='Knowledge Base',
                        url=INTERNAL_MCP_URL,
                    )
                )
                yield self._stream_item(
                    f'Knowledge Base tools ready ({len(self.tools)} total tools loaded so far).',
                    metadata={
                        'phase': 'initializing',
                        'tool_source': 'knowledge_base',
                        'tool_count': len(self.tools),
                    },
                )
            except Exception as exc:
                logger.exception(
                    'Failed to load tools from Knowledge Base MCP: %s',
                    exc,
                )
                yield self._stream_item(
                    'Knowledge Base tools are unavailable right now; continuing with the remaining runtime.',
                    metadata={
                        'phase': 'initializing',
                        'severity': 'warning',
                        'tool_source': 'knowledge_base',
                        'warning_type': type(exc).__name__,
                    },
                )

            yield self._stream_item(
                'Connecting to the Atlassian tools...',
                metadata={'phase': 'initializing', 'tool_source': 'atlassian'},
            )
            try:
                atlassian_tools = await self._load_toolset(
                    name='Atlassian',
                    url=ATLASSIAN_MCP_URL,
                )
                self.tools.extend(atlassian_tools)
                yield self._stream_item(
                    f'Atlassian tools ready ({len(atlassian_tools)} new tools, {len(self.tools)} total).',
                    metadata={
                        'phase': 'initializing',
                        'tool_source': 'atlassian',
                        'tool_count': len(atlassian_tools),
                        'total_tool_count': len(self.tools),
                    },
                )
            except Exception as exc:
                logger.exception(
                    'Failed to load tools from Atlassian MCP: %s',
                    exc,
                )
                yield self._stream_item(
                    'Atlassian tools are unavailable right now; continuing with the remaining runtime.',
                    metadata={
                        'phase': 'initializing',
                        'severity': 'warning',
                        'tool_source': 'atlassian',
                        'warning_type': type(exc).__name__,
                    },
                )

            yield self._stream_item(
                'Loading agent prompt configuration...',
                metadata={'phase': 'initializing'},
            )
            self._initialize_langfuse()
            agent_config: dict[str, Any]
            if self.langfuse_enabled and self.langfuse is not None:
                try:
                    prompt = self.langfuse.get_prompt(
                        AGENT_SETTINGS,
                        label='latest',
                    )
                    agent_config = {
                        'prompt': prompt.prompt,
                        'config': {
                            'temperature': prompt.config.get('temperature', 0),
                        },
                    }
                    prompt_source = 'langfuse'
                except Exception as exc:
                    logger.exception(
                        'Failed to fetch Langfuse prompt. Falling back to local config: %s',
                        exc,
                    )
                    self.langfuse_enabled = False
                    self.langfuse_handler = None
                    with open(
                        os.path.join(
                            os.path.dirname(__file__),
                            'default_config.json',
                        )
                    ) as config_file:
                        agent_config = json.load(config_file)
                    prompt_source = 'local_default'
            else:
                with open(
                    os.path.join(
                        os.path.dirname(__file__),
                        'default_config.json',
                    )
                ) as config_file:
                    agent_config = json.load(config_file)
                prompt_source = 'local_default'

            sync_client = httpx.Client(verify=SSL_VERIFY)
            async_client = httpx.AsyncClient(verify=SSL_VERIFY)

            self.model = ChatOpenAI(
                model=os.getenv('CHAT_MODEL'),
                openai_api_key=os.getenv('CHAT_API_KEY', 'EMPTY'),
                openai_api_base=os.getenv('CHAT_BASE_URL'),
                temperature=float(agent_config['config']['temperature']),
                tiktoken_model_name=None,
                default_headers=json.loads(os.getenv('DEFAULT_HEADERS')),
                http_client=sync_client,
                http_async_client=async_client,
            )
            self.graph = create_react_agent(
                self.model,
                tools=self.tools,
                checkpointer=memory,
                prompt=agent_config['prompt'],
                response_format=(self.FORMAT_INSTRUCTION, ResponseFormat),
            )

            yield self._stream_item(
                f'Agent runtime ready. Prompt source: {prompt_source}. Total tools available: {len(self.tools)}.',
                metadata={
                    'phase': 'initializing',
                    'prompt_source': prompt_source,
                    'tool_count': len(self.tools),
                },
            )

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

    def _build_graph_config(self, context_id: str) -> dict[str, Any]:
        return {
            'configurable': {
                'thread_id': context_id,
            },
            'callbacks': [self.langfuse_handler] if self.langfuse_handler else [],
            'metadata': {
                'langfuse_session_id': context_id,
            },
        }

    async def stream(
        self,
        query: str,
        context_id: str,
    ) -> AsyncIterable[AgentStreamItem]:
        async for item in self.initialize():
            yield item

        if self.graph is None:
            raise RuntimeError('Agent graph was not initialized.')

        inputs = {'messages': [('user', query)]}
        config = self._build_graph_config(context_id)
        seen_message_keys: set[str] = set()

        yield self._stream_item(
            'Reviewing the request and conversation context...',
            metadata={'phase': 'planning', 'context_id': context_id},
        )
        yield self._stream_item(
            'Sending the request to the language model...',
            metadata={'phase': 'model_call', 'context_id': context_id},
        )

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

        yield await self.get_agent_response(config)

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
        final_state: Literal[
            'working',
            'completed',
            'input_required',
            'failed',
        ] = 'input_required'

        if structured_response and isinstance(structured_response, ResponseFormat):
            final_content = structured_response.message.strip() or last_ai_message
            if (
                last_ai_message
                and last_ai_message != structured_response.message
            ):
                if structured_response.message in last_ai_message:
                    final_content = last_ai_message
                elif last_ai_message in structured_response.message:
                    final_content = structured_response.message
                else:
                    final_content = (
                        f'{last_ai_message}\n\n{structured_response.message}'
                    )

            if structured_response.status == 'completed':
                final_state = 'completed'
            elif structured_response.status == 'error':
                final_state = 'failed'
            else:
                final_state = 'input_required'

            return self._stream_item(
                final_content or 'The task finished without a response message.',
                task_state=final_state,
                metadata={
                    'phase': 'final_response',
                    'response_status': structured_response.status,
                },
            )

        fallback_message = final_content or (
            'We could not finish the request cleanly. Please try again.'
        )
        return self._stream_item(
            fallback_message,
            task_state='input_required',
            metadata={
                'phase': 'final_response',
                'response_status': 'fallback',
            },
        )
