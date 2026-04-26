import json
import time

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


AG_UI_MEDIA_TYPE = 'text/event-stream'
AG_UI_NDJSON_MEDIA_TYPE = 'application/x-ndjson'


def _to_camel(value: str) -> str:
    parts = value.split('_')
    return parts[0] + ''.join(part.capitalize() for part in parts[1:])


class AgUiBaseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=_to_camel,
        populate_by_name=True,
        extra='allow',
    )


class FunctionCall(AgUiBaseModel):
    name: str
    arguments: str = '{}'


class ToolCall(AgUiBaseModel):
    id: str | None = None
    type: Literal['function'] = 'function'
    function: FunctionCall


class Context(AgUiBaseModel):
    description: str
    value: Any


class Tool(AgUiBaseModel):
    name: str
    description: str | None = None
    parameters: Any = None


class Message(AgUiBaseModel):
    id: str | None = None
    role: str
    content: Any = None
    name: str | None = None
    tool_calls: list[ToolCall] = Field(default_factory=list)
    tool_call_id: str | None = None
    activity_type: str | None = None
    error: str | None = None
    metadata: dict[str, Any] | None = None
    encrypted_value: str | None = None


class RunAgentInput(AgUiBaseModel):
    thread_id: str
    run_id: str
    parent_run_id: str | None = None
    state: Any = Field(default_factory=dict)
    messages: list[Message] = Field(default_factory=list)
    tools: list[Tool] = Field(default_factory=list)
    context: list[Context] = Field(default_factory=list)
    forwarded_props: Any = Field(default_factory=dict)


class BaseEvent(AgUiBaseModel):
    type: str
    timestamp: int | None = None
    raw_event: Any = None

    @model_validator(mode='before')
    @classmethod
    def _apply_default_timestamp(cls, value: Any) -> Any:
        if not isinstance(value, dict):
            return value
        if value.get('timestamp') is not None:
            return value
        updated = dict(value)
        updated['timestamp'] = int(time.time() * 1000)
        return updated


class RunStartedEvent(BaseEvent):
    type: Literal['RUN_STARTED'] = 'RUN_STARTED'
    thread_id: str
    run_id: str
    parent_run_id: str | None = None
    input: RunAgentInput | None = None


class RunFinishedEvent(BaseEvent):
    type: Literal['RUN_FINISHED'] = 'RUN_FINISHED'
    thread_id: str
    run_id: str
    result: Any = None


class RunErrorEvent(BaseEvent):
    type: Literal['RUN_ERROR'] = 'RUN_ERROR'
    message: str
    code: str | None = None


class StepStartedEvent(BaseEvent):
    type: Literal['STEP_STARTED'] = 'STEP_STARTED'
    step_name: str


class StepFinishedEvent(BaseEvent):
    type: Literal['STEP_FINISHED'] = 'STEP_FINISHED'
    step_name: str


class TextMessageStartEvent(BaseEvent):
    type: Literal['TEXT_MESSAGE_START'] = 'TEXT_MESSAGE_START'
    message_id: str
    role: Literal['assistant'] = 'assistant'


class TextMessageContentEvent(BaseEvent):
    type: Literal['TEXT_MESSAGE_CONTENT'] = 'TEXT_MESSAGE_CONTENT'
    message_id: str
    delta: str

    @model_validator(mode='after')
    def _validate_delta(self) -> 'TextMessageContentEvent':
        if not self.delta:
            raise ValueError('Delta must not be empty.')
        return self


class TextMessageEndEvent(BaseEvent):
    type: Literal['TEXT_MESSAGE_END'] = 'TEXT_MESSAGE_END'
    message_id: str


class ToolCallStartEvent(BaseEvent):
    type: Literal['TOOL_CALL_START'] = 'TOOL_CALL_START'
    tool_call_id: str
    tool_call_name: str
    parent_message_id: str | None = None


class ToolCallArgsEvent(BaseEvent):
    type: Literal['TOOL_CALL_ARGS'] = 'TOOL_CALL_ARGS'
    tool_call_id: str
    delta: str


class ToolCallEndEvent(BaseEvent):
    type: Literal['TOOL_CALL_END'] = 'TOOL_CALL_END'
    tool_call_id: str


class ToolCallResultEvent(BaseEvent):
    type: Literal['TOOL_CALL_RESULT'] = 'TOOL_CALL_RESULT'
    message_id: str
    tool_call_id: str
    content: str
    role: Literal['tool'] | None = 'tool'


class StateSnapshotEvent(BaseEvent):
    type: Literal['STATE_SNAPSHOT'] = 'STATE_SNAPSHOT'
    snapshot: Any


class StateDeltaEvent(BaseEvent):
    type: Literal['STATE_DELTA'] = 'STATE_DELTA'
    delta: list[Any]


class MessagesSnapshotEvent(BaseEvent):
    type: Literal['MESSAGES_SNAPSHOT'] = 'MESSAGES_SNAPSHOT'
    messages: list[Message]


class ActivitySnapshotEvent(BaseEvent):
    type: Literal['ACTIVITY_SNAPSHOT'] = 'ACTIVITY_SNAPSHOT'
    message_id: str
    activity_type: str
    content: Any
    replace: bool = True


class ActivityDeltaEvent(BaseEvent):
    type: Literal['ACTIVITY_DELTA'] = 'ACTIVITY_DELTA'
    message_id: str
    activity_type: str
    patch: list[Any]


class RawEvent(BaseEvent):
    type: Literal['RAW'] = 'RAW'
    event: Any
    source: str | None = None


class CustomEvent(BaseEvent):
    type: Literal['CUSTOM'] = 'CUSTOM'
    name: str
    value: Any


class EventEncoder:
    def __init__(self, accept: str | None = None) -> None:
        accept_value = (accept or '').lower()
        self._use_sse = (
            not accept_value
            or AG_UI_MEDIA_TYPE in accept_value
            or '*/*' in accept_value
        )

    def encode(self, event: BaseEvent) -> str:
        payload = event.model_dump(by_alias=True, exclude_none=True)
        body = json.dumps(
            payload,
            ensure_ascii=False,
            separators=(',', ':'),
        )
        if self._use_sse:
            return f'data: {body}\n\n'
        return f'{body}\n'

    def get_content_type(self) -> str:
        if self._use_sse:
            return AG_UI_MEDIA_TYPE
        return AG_UI_NDJSON_MEDIA_TYPE


def encode_sse_event(event: BaseEvent) -> str:
    return EventEncoder().encode(event)


def flatten_text_content(content: Any) -> str:
    if content is None:
        return ''

    if isinstance(content, str):
        return content.strip()

    if hasattr(content, 'model_dump'):
        return flatten_text_content(content.model_dump(exclude_none=True))

    if isinstance(content, dict):
        part_type = str(content.get('type') or '').strip().lower()
        if part_type == 'text':
            text = content.get('text')
            return text.strip() if isinstance(text, str) else ''

        source = content.get('source')
        if hasattr(source, 'model_dump'):
            source = source.model_dump(exclude_none=True)
        if isinstance(source, dict):
            source_type = str(source.get('type') or '').strip().lower()
            source_value = source.get('value') or source.get('url')
            label = part_type or 'input'
            if (
                source_type == 'url'
                and isinstance(source_value, str)
                and source_value.strip()
            ):
                return f'[{label}: {source_value.strip()}]'
            if source_type == 'data':
                return f'[{label}: inline content]'

        text = content.get('text')
        if isinstance(text, str):
            return text.strip()

        return ''

    if isinstance(content, list):
        parts = [flatten_text_content(item) for item in content]
        return '\n'.join(part for part in parts if part).strip()

    return str(content).strip()


def parse_tool_call_arguments(arguments: str | dict[str, Any] | None) -> dict[str, Any]:
    if arguments is None:
        return {}
    if isinstance(arguments, dict):
        return arguments

    text = arguments.strip()
    if not text:
        return {}

    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return {'raw': text}

    return parsed if isinstance(parsed, dict) else {'value': parsed}
