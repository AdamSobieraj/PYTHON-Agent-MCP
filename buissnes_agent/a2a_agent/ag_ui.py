import json
import time

from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


AG_UI_MEDIA_TYPE = 'text/event-stream'


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


class Message(AgUiBaseModel):
    id: str | None = None
    role: str
    content: Any = None
    name: str | None = None
    tool_calls: list[ToolCall] = Field(default_factory=list)
    tool_call_id: str | None = None
    error: str | None = None
    metadata: dict[str, Any] | None = None
    encrypted_value: str | None = None


class RunAgentInput(AgUiBaseModel):
    thread_id: str
    run_id: str
    parent_run_id: str | None = None
    state: Any = None
    messages: list[Message] = Field(default_factory=list)
    tools: list[dict[str, Any]] = Field(default_factory=list)
    context: list[dict[str, Any]] = Field(default_factory=list)
    forwarded_props: Any = None


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


class ActivitySnapshotEvent(BaseEvent):
    type: Literal['ACTIVITY_SNAPSHOT'] = 'ACTIVITY_SNAPSHOT'
    message_id: str
    activity_type: str
    content: dict[str, Any]
    replace: bool = False


class StateSnapshotEvent(BaseEvent):
    type: Literal['STATE_SNAPSHOT'] = 'STATE_SNAPSHOT'
    snapshot: dict[str, Any]


class CustomEvent(BaseEvent):
    type: Literal['CUSTOM'] = 'CUSTOM'
    name: str
    value: Any


def encode_sse_event(event: BaseEvent) -> str:
    payload = event.model_dump(by_alias=True, exclude_none=True)
    return (
        f'data: {json.dumps(payload, ensure_ascii=False, separators=(",", ":"))}\n\n'
    )


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
            source_value = source.get('value') or source.get('url')
            if isinstance(source_value, str) and source_value.strip():
                label = part_type or 'input'
                return f'[{label}: {source_value.strip()}]'

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
