from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


def _to_camel(value: str) -> str:
    parts = value.split('_')
    return parts[0] + ''.join(part.capitalize() for part in parts[1:])


class AgUiModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=_to_camel,
        populate_by_name=True,
        extra='allow',
    )


class AgUiMessage(AgUiModel):
    id: str
    role: str
    content: Any = None
    name: str | None = None
    tool_calls: list[dict[str, Any]] | None = None
    tool_call_id: str | None = None
    activity_type: str | None = None
    error: str | None = None
    encrypted_value: str | None = None


class AgUiTool(AgUiModel):
    name: str
    description: str | None = None
    parameters: Any = None


class AgUiContext(AgUiModel):
    description: str
    value: Any


class RunAgentInput(AgUiModel):
    thread_id: str
    run_id: str
    parent_run_id: str | None = None
    state: Any = Field(default_factory=dict)
    messages: list[AgUiMessage] = Field(default_factory=list)
    tools: list[AgUiTool] = Field(default_factory=list)
    context: list[AgUiContext] = Field(default_factory=list)
    forwarded_props: Any = Field(default_factory=dict)
