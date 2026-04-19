import logging
import re
from typing import Any, Literal

import httpx
import openai

from a2a.server.agent_execution import AgentExecutor, RequestContext
from a2a.server.events import EventQueue
from a2a.server.tasks import TaskUpdater
from a2a.types import (
    InvalidParamsError,
    Part,
    TaskState,
    UnsupportedOperationError,
)

try:
    from .agent import AnalysisAgent
except ImportError:
    from buissnes_agent.a2a_agent.agent import AnalysisAgent  # type: ignore


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CONTEXT_WINDOW_PATTERN = re.compile(
    r"maximum context length is\s+(?P<max_tokens>\d+)\s+tokens.*?request has\s+"
    r"(?P<input_tokens>\d+)\s+input tokens",
    re.IGNORECASE | re.DOTALL,
)

TaskStateName = Literal['working', 'completed', 'input_required', 'failed']


class AnalysisAgentExecutor(AgentExecutor):
    """A2A executor for the business analysis agent."""

    def __init__(self) -> None:
        self.agent = AnalysisAgent()

    async def startup(self) -> None:
        await self.agent.start_auto_refresh()

    async def shutdown(self) -> None:
        await self.agent.close()

    async def execute(
        self,
        context: RequestContext,
        event_queue: EventQueue,
    ) -> None:
        error_message = self._validate_request(context)
        if error_message:
            raise InvalidParamsError(message=error_message)

        task_id = context.task_id
        context_id = context.context_id
        if not task_id or not context_id:
            raise InvalidParamsError(
                message='Both task_id and context_id are required.'
            )

        updater = TaskUpdater(
            event_queue=event_queue,
            task_id=task_id,
            context_id=context_id,
        )

        await updater.start_work(
            message=self._new_agent_message(
                updater,
                'Processing your request...',
                metadata={
                    'phase': 'submitted',
                    'task_state': 'working',
                },
            )
        )

        query = context.get_user_input()
        last_status_signature: tuple[str, str] | None = None

        try:
            async for item in self.agent.stream(query, context_id):
                task_state = self._resolve_task_state(item)
                content = self._resolve_content(item, task_state=task_state)
                metadata = self._resolve_metadata(
                    item,
                    task_state=task_state,
                    task_id=task_id,
                    context_id=context_id,
                )

                signature = (task_state, content)
                if task_state == 'working' and signature == last_status_signature:
                    continue
                last_status_signature = signature

                if task_state == 'completed':
                    await updater.add_artifact(
                        parts=[Part(text=content)],
                        name='analysis_result',
                        metadata=metadata,
                        last_chunk=True,
                    )
                    await updater.complete()
                    return

                if task_state == 'input_required':
                    await updater.requires_input(
                        message=self._new_agent_message(
                            updater,
                            content,
                            metadata=metadata,
                        )
                    )
                    return

                if task_state == 'failed':
                    await updater.failed(
                        message=self._new_agent_message(
                            updater,
                            content,
                            metadata=metadata,
                        )
                    )
                    return

                await updater.update_status(
                    TaskState.TASK_STATE_WORKING,
                    message=self._new_agent_message(
                        updater,
                        content,
                        metadata=metadata,
                    ),
                )
        except Exception as exc:
            failure_content, failure_metadata = self._describe_exception(
                exc,
                context_id=context_id,
            )
            logger.error(
                'Agent execution failed for task %s (context %s): %s',
                task_id,
                context_id,
                failure_content,
                exc_info=True,
            )
            await updater.failed(
                message=self._new_agent_message(
                    updater,
                    failure_content,
                    metadata=failure_metadata,
                )
            )

    def _validate_request(self, context: RequestContext) -> str | None:
        if not context.message:
            return 'A user message is required.'

        if not context.get_user_input().strip():
            return 'A text input message is required.'

        return None

    def _new_agent_message(
        self,
        updater: TaskUpdater,
        content: str,
        *,
        metadata: dict[str, Any] | None = None,
    ):
        return updater.new_agent_message(
            parts=[Part(text=content)],
            metadata=self._json_safe(metadata or {}),
        )

    def _resolve_task_state(self, item: dict[str, Any]) -> TaskStateName:
        task_state = item.get('task_state')
        if task_state in {'working', 'completed', 'input_required', 'failed'}:
            return task_state

        if item.get('is_task_complete'):
            return 'completed'
        if item.get('require_user_input'):
            return 'input_required'
        if item.get('is_error'):
            return 'failed'
        return 'working'

    def _resolve_content(
        self,
        item: dict[str, Any],
        *,
        task_state: TaskStateName,
    ) -> str:
        content = str(item.get('content') or '').strip()
        if content:
            return content

        if task_state == 'completed':
            return 'The request completed successfully.'
        if task_state == 'input_required':
            return 'More information is required to continue.'
        if task_state == 'failed':
            return 'The request failed before a response could be produced.'
        return 'Processing your request...'

    def _resolve_metadata(
        self,
        item: dict[str, Any],
        *,
        task_state: TaskStateName,
        task_id: str,
        context_id: str,
    ) -> dict[str, Any]:
        metadata = dict(item.get('metadata') or {})
        metadata.setdefault('task_state', task_state)
        metadata.setdefault('task_id', task_id)
        metadata.setdefault('context_id', context_id)
        return self._json_safe(metadata)

    def _json_safe(self, value: Any) -> Any:
        if value is None or isinstance(value, (str, int, float, bool)):
            return value
        if isinstance(value, dict):
            return {
                str(key): self._json_safe(item)
                for key, item in value.items()
            }
        if isinstance(value, (list, tuple)):
            return [self._json_safe(item) for item in value]
        return str(value)

    def _extract_openai_error_message(
        self,
        error: openai.BadRequestError,
    ) -> str:
        body = getattr(error, 'body', None)
        if isinstance(body, dict):
            nested_error = body.get('error')
            if isinstance(nested_error, dict):
                nested_message = nested_error.get('message')
                if isinstance(nested_message, str) and nested_message.strip():
                    return nested_message.strip()

            body_message = body.get('message')
            if isinstance(body_message, str) and body_message.strip():
                return body_message.strip()

        return str(error).strip()

    def _describe_exception(
        self,
        error: Exception,
        *,
        context_id: str,
    ) -> tuple[str, dict[str, Any]]:
        metadata: dict[str, Any] = {
            'phase': 'failed',
            'task_state': 'failed',
            'context_id': context_id,
            'error_type': type(error).__name__,
        }

        provider_message = str(error).strip()

        if isinstance(error, openai.BadRequestError):
            provider_message = self._extract_openai_error_message(error)
            metadata['provider'] = 'openai'
            if getattr(error, 'request_id', None):
                metadata['provider_request_id'] = error.request_id

            match = CONTEXT_WINDOW_PATTERN.search(provider_message)
            if match:
                max_tokens = int(match.group('max_tokens'))
                input_tokens = int(match.group('input_tokens'))
                metadata.update(
                    {
                        'error_code': 'context_length_exceeded',
                        'max_input_tokens': max_tokens,
                        'input_tokens': input_tokens,
                        'provider_message': provider_message,
                    }
                )
                return (
                    'The conversation context is too large for the configured model. '
                    f'This request used {input_tokens} input tokens, but the model only supports '
                    f'{max_tokens}. Start a fresh context or trim earlier conversation history, '
                    'then try again.',
                    metadata,
                )

            metadata.update(
                {
                    'error_code': 'bad_request',
                    'provider_message': provider_message,
                }
            )
            return (
                f'The language model rejected the request: {provider_message}',
                metadata,
            )

        if isinstance(error, httpx.TimeoutException):
            metadata['error_code'] = 'upstream_timeout'
            return (
                'A required upstream service timed out while processing this request. '
                'Please try again.',
                metadata,
            )

        if isinstance(error, httpx.HTTPError):
            metadata['error_code'] = 'upstream_http_error'
            metadata['provider_message'] = provider_message
            return (
                f'A required upstream service returned an HTTP error: {provider_message}',
                metadata,
            )

        match = CONTEXT_WINDOW_PATTERN.search(provider_message)
        if match:
            max_tokens = int(match.group('max_tokens'))
            input_tokens = int(match.group('input_tokens'))
            metadata.update(
                {
                    'error_code': 'context_length_exceeded',
                    'max_input_tokens': max_tokens,
                    'input_tokens': input_tokens,
                    'provider_message': provider_message,
                }
            )
            return (
                'The conversation context is too large for the configured model. '
                f'This request used {input_tokens} input tokens, but the model only supports '
                f'{max_tokens}. Start a fresh context or trim earlier conversation history, '
                'then try again.',
                metadata,
            )

        metadata['error_code'] = 'agent_execution_failed'
        metadata['provider_message'] = provider_message
        return (
            f'The agent failed while processing the task: {provider_message}',
            metadata,
        )

    async def cancel(
        self,
        context: RequestContext,
        event_queue: EventQueue,
    ) -> None:
        task_id = context.task_id
        context_id = context.context_id
        if not task_id or not context_id:
            raise UnsupportedOperationError(
                message='Cannot cancel a task without task_id and context_id.'
            )

        updater = TaskUpdater(
            event_queue=event_queue,
            task_id=task_id,
            context_id=context_id,
        )
        await updater.cancel(
            message=updater.new_agent_message(
                parts=[Part(text='Task cancelled by request.')]
            )
        )
