from __future__ import annotations

import copy
import json
import logging
import os
import uuid

from collections.abc import AsyncGenerator, Awaitable, Callable
from dataclasses import dataclass, field
from typing import Any

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse
from google.protobuf.json_format import MessageToDict

from a2a.client import ClientConfig, create_client
from a2a.types import (
    Message,
    Part,
    Role,
    SendMessageConfiguration,
    SendMessageRequest,
    StreamResponse,
    TaskState,
)

from .models import AgUiContext, AgUiMessage, RunAgentInput


logger = logging.getLogger(__name__)

TransportFactory = Callable[
    ['A2ATarget'],
    Awaitable[Any],
]

STATE_KEY = 'a2a'
PAUSED_STATES = {'input-required', 'auth-required'}
TERMINAL_STATES = {
    'completed',
    'failed',
    'rejected',
    'canceled',
}


@dataclass(slots=True)
class A2ATarget:
    url: str
    transport: str | None = None


@dataclass(slots=True)
class ThreadSession:
    thread_id: str
    a2a_url: str | None = None
    transport: str | None = None
    context_id: str | None = None
    current_task_id: str | None = None
    last_task_state: str | None = None
    last_user_message_id: str | None = None
    initialized: bool = False
    synced_message_ids: set[str] = field(default_factory=set)


class ThreadSessionStore:
    def __init__(self) -> None:
        self._sessions: dict[str, ThreadSession] = {}

    def get(self, thread_id: str) -> ThreadSession | None:
        return self._sessions.get(thread_id)

    def get_or_create(self, thread_id: str) -> ThreadSession:
        session = self._sessions.get(thread_id)
        if session is None:
            session = ThreadSession(thread_id=thread_id)
            self._sessions[thread_id] = session
        return session


class EventEncoder:
    def __init__(self, accept: str | None) -> None:
        accept_value = (accept or '').lower()
        self._use_sse = (
            not accept_value
            or 'text/event-stream' in accept_value
            or '*/*' in accept_value
        )

    def encode(self, payload: dict[str, Any]) -> bytes:
        body = json.dumps(
            payload,
            ensure_ascii=True,
            separators=(',', ':'),
        )
        if self._use_sse:
            return f'data: {body}\n\n'.encode('utf-8')
        return f'{body}\n'.encode('utf-8')

    def get_content_type(self) -> str:
        if self._use_sse:
            return 'text/event-stream'
        return 'application/x-ndjson'


def _event(event_type: str, **payload: Any) -> dict[str, Any]:
    data = {'type': event_type}
    for key, value in payload.items():
        if value is None:
            continue
        data[key] = value
    return data


def _run_started_event(input_data: RunAgentInput) -> dict[str, Any]:
    return _event(
        'RUN_STARTED',
        threadId=input_data.thread_id,
        runId=input_data.run_id,
    )


def _run_finished_event(
    input_data: RunAgentInput,
    *,
    result: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return _event(
        'RUN_FINISHED',
        threadId=input_data.thread_id,
        runId=input_data.run_id,
        result=result,
    )


def _run_error_event(message: str, *, code: str | None = None) -> dict[str, Any]:
    return _event(
        'RUN_ERROR',
        message=message,
        code=code,
    )


def _text_start_event(message_id: str) -> dict[str, Any]:
    return _event(
        'TEXT_MESSAGE_START',
        messageId=message_id,
        role='assistant',
    )


def _text_content_event(message_id: str, delta: str) -> dict[str, Any]:
    return _event(
        'TEXT_MESSAGE_CONTENT',
        messageId=message_id,
        delta=delta,
    )


def _text_end_event(message_id: str) -> dict[str, Any]:
    return _event(
        'TEXT_MESSAGE_END',
        messageId=message_id,
    )


def _activity_snapshot_event(
    message_id: str,
    content: dict[str, Any],
) -> dict[str, Any]:
    return _event(
        'ACTIVITY_SNAPSHOT',
        messageId=message_id,
        activityType='A2A_TASK',
        content=content,
        replace=True,
    )


def _state_snapshot_event(snapshot: dict[str, Any]) -> dict[str, Any]:
    return _event(
        'STATE_SNAPSHOT',
        snapshot=snapshot,
    )


def _safe_dict(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        return dict(value)
    return {}


def _normalize_transport(value: str | None) -> str | None:
    if not value:
        return None

    normalized = value.strip().lower()
    if normalized in {'jsonrpc', 'json-rpc'}:
        return 'JSONRPC'
    if normalized in {'http+json', 'rest', 'http_json'}:
        return 'HTTP+JSON'
    if normalized == 'grpc':
        return 'GRPC'
    return value.strip()


def _normalize_task_state(value: int) -> str:
    name = TaskState.Name(value)
    if name.startswith('TASK_STATE_'):
        name = name[len('TASK_STATE_') :]
    return name.lower().replace('_', '-')


def _message_text_from_parts(parts: list[Part]) -> str:
    chunks: list[str] = []
    for part in parts:
        if part.HasField('text') and part.text:
            chunks.append(part.text)
            continue
        if part.url:
            descriptor = part.media_type or 'link'
            chunks.append(f'[{descriptor} attachment: {part.url}]')
            continue
        if part.raw:
            descriptor = part.media_type or 'binary'
            filename = f' filename={part.filename}' if part.filename else ''
            chunks.append(f'[{descriptor} attachment{filename}]')
            continue
        if part.HasField('data'):
            chunks.append('[structured data attachment]')
    return '\n'.join(chunk for chunk in chunks if chunk)


def _message_text(message: Message | None) -> str:
    if message is None:
        return ''
    return _message_text_from_parts(list(message.parts))


def _content_to_text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return json.dumps(content, ensure_ascii=True, default=str)

    rendered: list[str] = []
    for item in content:
        if isinstance(item, str):
            rendered.append(item)
            continue
        if not isinstance(item, dict):
            rendered.append(str(item))
            continue
        item_type = str(item.get('type', '')).lower()
        if item_type == 'text':
            text = item.get('text')
            if isinstance(text, str):
                rendered.append(text)
            continue

        source = item.get('source') or {}
        source_type = str(source.get('type', '')).lower()
        source_value = source.get('value')
        mime_type = source.get('mimeType') or source.get('mime_type')
        filename = item.get('filename')
        descriptor = item_type or 'binary'

        details: list[str] = [descriptor]
        if mime_type:
            details.append(f'mime={mime_type}')
        if filename:
            details.append(f'filename={filename}')
        if source_type == 'url' and source_value:
            details.append(f'url={source_value}')
        elif source_type == 'data':
            details.append('inline-data')
        rendered.append('[' + ' '.join(details) + ']')

    return '\n'.join(part for part in rendered if part).strip()


def _render_tool_calls(tool_calls: list[dict[str, Any]] | None) -> str:
    if not tool_calls:
        return ''

    rendered: list[str] = []
    for tool_call in tool_calls:
        if not isinstance(tool_call, dict):
            rendered.append(str(tool_call))
            continue
        tool_id = tool_call.get('id')
        function = tool_call.get('function') or {}
        name = function.get('name') or tool_call.get('name') or 'tool'
        arguments = function.get('arguments') or tool_call.get('arguments') or ''
        prefix = f'{name}'
        if tool_id:
            prefix = f'{prefix} ({tool_id})'
        if arguments:
            prefix = f'{prefix}: {arguments}'
        rendered.append(prefix)
    return '\n'.join(rendered)


def _render_message_for_context(message: AgUiMessage) -> str:
    role = message.role.lower()

    if role == 'user':
        content = _content_to_text(message.content)
    elif role == 'assistant':
        content = (message.content or '').strip()
        tool_calls = _render_tool_calls(message.tool_calls)
        if tool_calls:
            content = '\n'.join(
                part for part in (content, f'Tool calls:\n{tool_calls}') if part
            )
    elif role == 'tool':
        content = str(message.content or '').strip()
        if message.tool_call_id:
            content = (
                f'Tool result for {message.tool_call_id}:\n{content}'
                if content
                else f'Tool result for {message.tool_call_id}.'
            )
        if message.error:
            content = (
                f'{content}\nError: {message.error}'
                if content
                else f'Error: {message.error}'
            )
    elif role == 'activity':
        payload = json.dumps(
            message.content,
            ensure_ascii=True,
            default=str,
        )
        activity_type = message.activity_type or 'activity'
        content = f'{activity_type}: {payload}'
    else:
        content = str(message.content or '').strip()

    if not content:
        return ''
    return f'[{role}]\n{content}'


def _context_preamble(context_items: list[AgUiContext]) -> str:
    if not context_items:
        return ''

    lines = ['Additional AG-UI context:']
    for item in context_items:
        value = item.value
        if not isinstance(value, str):
            value = json.dumps(value, ensure_ascii=True, default=str)
        lines.append(f'- {item.description}: {value}')
    return '\n'.join(lines)


def _messages_to_parts(
    input_data: RunAgentInput,
    session: ThreadSession,
) -> tuple[list[Part], list[str], str | None]:
    if not input_data.messages:
        raise ValueError('AG-UI request must contain at least one message.')

    new_messages = [
        message
        for message in input_data.messages
        if message.id not in session.synced_message_ids
    ]
    state_session = _safe_dict(_safe_dict(input_data.state).get(STATE_KEY))

    if new_messages:
        selected_messages = new_messages
    elif session.initialized or state_session.get('initialized'):
        last_user = next(
            (
                message
                for message in reversed(input_data.messages)
                if message.role.lower() == 'user'
            ),
            None,
        )
        if last_user is None:
            raise ValueError('AG-UI request does not contain a user message.')
        selected_messages = [last_user]
    else:
        selected_messages = input_data.messages

    last_user = next(
        (
            message
            for message in reversed(selected_messages)
            if message.role.lower() == 'user'
        ),
        None,
    )

    preamble_chunks: list[str] = []
    context_text = _context_preamble(input_data.context)
    if context_text:
        preamble_chunks.append(context_text)

    transcript_chunks: list[str] = []
    for message in selected_messages:
        if last_user is not None and message.id == last_user.id:
            continue
        rendered = _render_message_for_context(message)
        if rendered:
            transcript_chunks.append(rendered)

    if transcript_chunks:
        preamble_chunks.append(
            'Conversation transcript to preserve context:\n\n'
            + '\n\n'.join(transcript_chunks)
        )

    parts: list[Part] = []
    if preamble_chunks:
        parts.append(Part(text='\n\n'.join(preamble_chunks)))

    if last_user is not None:
        user_text = _content_to_text(last_user.content).strip()
        if user_text:
            parts.append(Part(text=user_text))
    elif transcript_chunks:
        parts.append(Part(text='Continue using the context above.'))

    if not parts:
        raise ValueError('No serializable AG-UI content was available for A2A.')

    synced_ids = [message.id for message in selected_messages]
    return parts, synced_ids, last_user.id if last_user is not None else None


def _resolve_target(
    input_data: RunAgentInput,
    session: ThreadSession,
    request: Request | None,
    default_target: A2ATarget | None,
) -> tuple[A2ATarget, str, str | None]:
    sources: list[dict[str, Any]] = []
    forwarded = _safe_dict(input_data.forwarded_props)
    state = _safe_dict(input_data.state)
    if forwarded:
        sources.append(forwarded)
        nested = _safe_dict(forwarded.get(STATE_KEY))
        if nested:
            sources.append(nested)
    if state:
        sources.append(state)
        nested = _safe_dict(state.get(STATE_KEY))
        if nested:
            sources.append(nested)

    if request is not None:
        header_url = request.headers.get('x-a2a-url')
        header_transport = request.headers.get('x-a2a-transport')
        if header_url or header_transport:
            sources.insert(
                0,
                {
                    'url': header_url,
                    'transport': header_transport,
                },
            )

    resolved_url = None
    resolved_transport = None
    resolved_context_id = None
    resolved_task_id = None

    for source in sources:
        resolved_url = resolved_url or source.get('url') or source.get('a2a_url')
        resolved_transport = (
            resolved_transport
            or source.get('transport')
            or source.get('a2a_transport')
        )
        resolved_context_id = (
            resolved_context_id
            or source.get('contextId')
            or source.get('context_id')
        )
        resolved_task_id = (
            resolved_task_id
            or source.get('taskId')
            or source.get('task_id')
        )

    resolved_url = (
        resolved_url
        or session.a2a_url
        or (default_target.url if default_target is not None else None)
    )
    if not resolved_url:
        raise ValueError(
            'No A2A target URL was configured. '
            'Provide A2A_AGENT_URL or forwardedProps.a2a.url.'
        )

    resolved_transport = _normalize_transport(
        resolved_transport
        or session.transport
        or (default_target.transport if default_target is not None else None)
    )
    resolved_context_id = resolved_context_id or session.context_id or input_data.thread_id
    resolved_task_id = resolved_task_id or session.current_task_id

    return (
        A2ATarget(url=str(resolved_url), transport=resolved_transport),
        str(resolved_context_id),
        str(resolved_task_id) if resolved_task_id else None,
    )


async def _build_client(target: A2ATarget) -> Any:
    config = ClientConfig()
    if target.transport:
        config.supported_protocol_bindings = [target.transport]
    return await create_client(target.url, client_config=config)


class AgUiA2AAdapterService:
    def __init__(
        self,
        *,
        default_target: A2ATarget | None = None,
        session_store: ThreadSessionStore | None = None,
        client_factory: TransportFactory | None = None,
    ) -> None:
        self.default_target = default_target
        self.session_store = session_store or ThreadSessionStore()
        self.client_factory = client_factory or _build_client

    def _state_snapshot(
        self,
        input_data: RunAgentInput,
        session: ThreadSession,
    ) -> dict[str, Any]:
        base_state = copy.deepcopy(input_data.state)
        if isinstance(base_state, dict):
            snapshot = base_state
        else:
            snapshot = {'clientState': base_state}

        snapshot[STATE_KEY] = {
            'initialized': session.initialized,
            'url': session.a2a_url,
            'transport': session.transport,
            'contextId': session.context_id,
            'taskId': session.current_task_id,
            'taskState': session.last_task_state,
            'lastUserMessageId': session.last_user_message_id,
        }
        return snapshot

    def _activity_payload(
        self,
        *,
        task_id: str,
        context_id: str,
        task_state: str,
        message: str | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        payload = {
            'taskId': task_id,
            'contextId': context_id,
            'taskState': task_state,
        }
        if message:
            payload['message'] = message
        if metadata:
            payload['metadata'] = metadata
        return payload

    async def stream_events(
        self,
        input_data: RunAgentInput,
        *,
        request: Request | None = None,
    ) -> AsyncGenerator[dict[str, Any], None]:
        session = self.session_store.get_or_create(input_data.thread_id)
        activity_message_id = f'a2a-task-{input_data.thread_id}'
        open_text_messages: set[str] = set()
        emitted_assistant_content = False
        last_status_text = ''
        last_task_state: str | None = None

        target, context_id, task_id = _resolve_target(
            input_data,
            session,
            request,
            self.default_target,
        )
        parts, synced_ids, last_user_message_id = _messages_to_parts(
            input_data,
            session,
        )

        session.a2a_url = target.url
        session.transport = target.transport
        session.context_id = context_id
        session.current_task_id = task_id
        session.last_user_message_id = last_user_message_id

        yield _run_started_event(input_data)
        yield _state_snapshot_event(self._state_snapshot(input_data, session))

        client = None
        try:
            client = await self.client_factory(target)

            request_metadata = {
                'ag_ui_thread_id': input_data.thread_id,
                'ag_ui_run_id': input_data.run_id,
                'ag_ui_parent_run_id': input_data.parent_run_id,
                'ag_ui_target_url': target.url,
                'ag_ui_target_transport': target.transport,
                'ag_ui_message_count': len(input_data.messages),
            }
            message = Message(
                role=Role.ROLE_USER,
                message_id=last_user_message_id or str(uuid.uuid4()),
                context_id=context_id,
                task_id=task_id,
                parts=parts,
            )
            send_request = SendMessageRequest(
                message=message,
                configuration=SendMessageConfiguration(
                    accepted_output_modes=['text', 'task-status']
                ),
                metadata=request_metadata,
            )

            async for stream_response in client.send_message(send_request):
                for event in self._map_stream_response(
                    stream_response=stream_response,
                    session=session,
                    input_data=input_data,
                    activity_message_id=activity_message_id,
                    open_text_messages=open_text_messages,
                ):
                    if event['type'] == 'TEXT_MESSAGE_CONTENT':
                        emitted_assistant_content = True
                    if event['type'] == 'ACTIVITY_SNAPSHOT':
                        last_task_state = (
                            event.get('content', {}).get('taskState')
                            or last_task_state
                        )
                        last_status_text = (
                            event.get('content', {}).get('message', '')
                            or last_status_text
                        )
                    yield event

            for message_id in list(open_text_messages):
                yield _text_end_event(message_id)
                open_text_messages.discard(message_id)

            if (
                last_status_text
                and (
                    not emitted_assistant_content
                    or last_task_state in PAUSED_STATES
                    or last_task_state in TERMINAL_STATES - {'completed'}
                )
            ):
                status_message_id = str(uuid.uuid4())
                yield _text_start_event(status_message_id)
                yield _text_content_event(status_message_id, last_status_text)
                yield _text_end_event(status_message_id)

            session.initialized = True
            session.synced_message_ids.update(synced_ids)

            if last_task_state in PAUSED_STATES:
                session.last_task_state = last_task_state
            elif last_task_state in TERMINAL_STATES:
                session.current_task_id = None
                session.last_task_state = last_task_state
            else:
                session.last_task_state = last_task_state

            yield _state_snapshot_event(self._state_snapshot(input_data, session))

            if last_task_state in {'failed', 'rejected', 'canceled'}:
                yield _run_error_event(
                    last_status_text or 'The A2A task failed.',
                    code=last_task_state,
                )
                return

            yield _run_finished_event(
                input_data,
                result={
                    'taskState': session.last_task_state,
                    'contextId': session.context_id,
                    'taskId': session.current_task_id,
                    'target': {
                        'url': session.a2a_url,
                        'transport': session.transport,
                    },
                },
            )
        except Exception as exc:
            logger.exception('AG-UI adapter failed to process request')
            yield _run_error_event(str(exc), code='adapter_error')
        finally:
            if client is not None:
                await client.close()

    def _map_stream_response(
        self,
        *,
        stream_response: StreamResponse,
        session: ThreadSession,
        input_data: RunAgentInput,
        activity_message_id: str,
        open_text_messages: set[str],
    ) -> list[dict[str, Any]]:
        events: list[dict[str, Any]] = []

        if stream_response.HasField('task'):
            task = stream_response.task
            task_state = _normalize_task_state(task.status.state)
            task_message = (
                _message_text(task.status.message)
                if task.status.HasField('message')
                else ''
            )
            session.current_task_id = task.id or session.current_task_id
            session.context_id = task.context_id or session.context_id
            session.last_task_state = task_state
            events.append(
                _activity_snapshot_event(
                    activity_message_id,
                    self._activity_payload(
                        task_id=session.current_task_id or '',
                        context_id=session.context_id or input_data.thread_id,
                        task_state=task_state,
                        message=task_message or None,
                    ),
                )
            )
            for artifact in task.artifacts:
                events.extend(
                    self._artifact_events(
                        artifact_id=artifact.artifact_id,
                        parts=list(artifact.parts),
                        append=True,
                        last_chunk=True,
                        open_text_messages=open_text_messages,
                    )
                )

        if stream_response.HasField('message'):
            direct_message = stream_response.message
            message_id = direct_message.message_id or str(uuid.uuid4())
            segments = _message_segments(list(direct_message.parts))
            if segments:
                events.append(_text_start_event(message_id))
                open_text_messages.add(message_id)
                for segment in segments:
                    events.append(_text_content_event(message_id, segment))
                events.append(_text_end_event(message_id))
                open_text_messages.discard(message_id)

        if stream_response.HasField('status_update'):
            status_update = stream_response.status_update
            task_state = _normalize_task_state(status_update.status.state)
            status_message = (
                _message_text(status_update.status.message)
                if status_update.status.HasField('message')
                else ''
            )
            session.current_task_id = (
                status_update.task_id or session.current_task_id
            )
            session.context_id = status_update.context_id or session.context_id
            session.last_task_state = task_state
            metadata = (
                MessageToDict(status_update.metadata)
                if status_update.metadata and status_update.metadata.fields
                else None
            )
            events.append(
                _activity_snapshot_event(
                    activity_message_id,
                    self._activity_payload(
                        task_id=session.current_task_id or '',
                        context_id=session.context_id or input_data.thread_id,
                        task_state=task_state,
                        message=status_message or None,
                        metadata=metadata,
                    ),
                )
            )
            if task_state in TERMINAL_STATES:
                session.current_task_id = None

        if stream_response.HasField('artifact_update'):
            artifact_update = stream_response.artifact_update
            session.current_task_id = (
                artifact_update.task_id or session.current_task_id
            )
            session.context_id = artifact_update.context_id or session.context_id
            events.extend(
                self._artifact_events(
                    artifact_id=artifact_update.artifact.artifact_id,
                    parts=list(artifact_update.artifact.parts),
                    append=artifact_update.append,
                    last_chunk=artifact_update.last_chunk,
                    open_text_messages=open_text_messages,
                )
            )

        return events

    def _artifact_events(
        self,
        *,
        artifact_id: str,
        parts: list[Part],
        append: bool,
        last_chunk: bool,
        open_text_messages: set[str],
    ) -> list[dict[str, Any]]:
        message_id = artifact_id or str(uuid.uuid4())
        events: list[dict[str, Any]] = []
        segments = _message_segments(parts)
        if not segments:
            return events

        if message_id not in open_text_messages or not append:
            if message_id in open_text_messages:
                events.append(_text_end_event(message_id))
            events.append(_text_start_event(message_id))
            open_text_messages.add(message_id)

        for segment in segments:
            events.append(_text_content_event(message_id, segment))

        if last_chunk:
            events.append(_text_end_event(message_id))
            open_text_messages.discard(message_id)

        return events


def _message_segments(parts: list[Part]) -> list[str]:
    text = _message_text_from_parts(parts)
    if not text:
        return []
    return [segment for segment in text.splitlines(True) if segment] or [text]


def create_app(
    *,
    default_target: A2ATarget | None = None,
    session_store: ThreadSessionStore | None = None,
    client_factory: TransportFactory | None = None,
) -> FastAPI:
    service = AgUiA2AAdapterService(
        default_target=default_target,
        session_store=session_store,
        client_factory=client_factory,
    )

    app = FastAPI(
        title='AG-UI A2A Adapter',
        description='Independent adapter that fronts A2A agents with an AG-UI endpoint.',
        version='0.1.0',
    )

    @app.get('/', include_in_schema=False)
    async def root() -> JSONResponse:
        return JSONResponse(
            {
                'name': 'AG-UI A2A Adapter',
                'postPath': '/',
                'healthz': '/healthz',
                'defaultTarget': {
                    'url': default_target.url if default_target else None,
                    'transport': (
                        default_target.transport if default_target else None
                    ),
                },
                'forwardedProps': {
                    STATE_KEY: {
                        'url': 'http://127.0.0.1:10004',
                        'transport': 'JSONRPC',
                    }
                },
            }
        )

    @app.get('/healthz', tags=['health'])
    async def healthz() -> JSONResponse:
        return JSONResponse({'ok': True})

    @app.post('/', tags=['ag-ui'])
    async def agentic_chat_endpoint(
        input_data: RunAgentInput,
        request: Request,
    ) -> StreamingResponse:
        encoder = EventEncoder(request.headers.get('accept'))

        async def event_generator() -> AsyncGenerator[bytes, None]:
            async for event in service.stream_events(input_data, request=request):
                yield encoder.encode(event)

        return StreamingResponse(
            event_generator(),
            media_type=encoder.get_content_type(),
        )

    return app


def default_target_from_env() -> A2ATarget | None:
    url = os.getenv('A2A_AGENT_URL')
    if not url:
        return None
    return A2ATarget(
        url=url,
        transport=_normalize_transport(os.getenv('A2A_AGENT_TRANSPORT')),
    )
