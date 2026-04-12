import logging

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
    from agent import AnalysisAgent  # type: ignore


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AnalysisAgentExecutor(AgentExecutor):
    """A2A executor for the business analysis agent."""

    def __init__(self) -> None:
        self.agent = AnalysisAgent()

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
            message=updater.new_agent_message(
                parts=[Part(text='Processing your request...')]
            )
        )

        query = context.get_user_input()

        try:
            async for item in self.agent.stream(query, context_id):
                content = item.get('content') or 'Processing your request...'

                if item.get('is_task_complete'):
                    await updater.add_artifact(
                        parts=[Part(text=content)],
                        name='analysis_result',
                        last_chunk=True,
                    )
                    await updater.complete()
                    return

                if item.get('require_user_input'):
                    await updater.requires_input(
                        message=updater.new_agent_message(
                            parts=[Part(text=content)]
                        )
                    )
                    return

                await updater.update_status(
                    TaskState.TASK_STATE_WORKING,
                    message=updater.new_agent_message(
                        parts=[Part(text=content)]
                    ),
                )
        except Exception:
            logger.exception('Agent execution failed for task %s', task_id)
            raise

    def _validate_request(self, context: RequestContext) -> str | None:
        if not context.message:
            return 'A user message is required.'

        if not context.get_user_input().strip():
            return 'A text input message is required.'

        return None

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
