import json
import unittest

from collections.abc import AsyncGenerator
from unittest.mock import patch

import httpx

from a2a.types import (
    Artifact,
    Message,
    Part,
    Role,
    StreamResponse,
    TaskState,
    TaskStatus,
    TaskStatusUpdateEvent,
)
from buissnes_agent.ag_ui_adapter.service import A2ATarget, create_app


class FakeClient:
    def __init__(self, responses: list[StreamResponse]) -> None:
        self.responses = responses
        self.requests = []
        self.closed = False

    async def send_message(
        self,
        request,
    ) -> AsyncGenerator[StreamResponse, None]:
        self.requests.append(request)
        for response in self.responses:
            yield response

    async def close(self) -> None:
        self.closed = True


def _status_response(
    *,
    task_id: str,
    context_id: str,
    state: TaskState,
    text: str | None = None,
) -> StreamResponse:
    message = None
    if text is not None:
        message = Message(
            role=Role.ROLE_AGENT,
            message_id='status-msg',
            task_id=task_id,
            context_id=context_id,
            parts=[Part(text=text)],
        )
    return StreamResponse(
        status_update=TaskStatusUpdateEvent(
            task_id=task_id,
            context_id=context_id,
            status=TaskStatus(
                state=state,
                message=message,
            ),
        )
    )


def _artifact_response(
    *,
    task_id: str,
    context_id: str,
    artifact_id: str,
    text: str,
    append: bool,
    last_chunk: bool,
) -> StreamResponse:
    return StreamResponse(
        artifact_update={
            'task_id': task_id,
            'context_id': context_id,
            'artifact': Artifact(
                artifact_id=artifact_id,
                parts=[Part(text=text)],
            ),
            'append': append,
            'last_chunk': last_chunk,
        }
    )


def _parse_sse_events(body: str) -> list[dict[str, object]]:
    events = []
    for line in body.splitlines():
        if not line.startswith('data: '):
            continue
        events.append(json.loads(line[6:]))
    return events


class AgUiAdapterTests(unittest.IsolatedAsyncioTestCase):
    async def test_endpoint_streams_artifact_updates_as_text_messages(self) -> None:
        fake_client = FakeClient(
            [
                _status_response(
                    task_id='task-1',
                    context_id='thread-1',
                    state=TaskState.TASK_STATE_WORKING,
                    text='Processing your request...',
                ),
                _artifact_response(
                    task_id='task-1',
                    context_id='thread-1',
                    artifact_id='artifact-1',
                    text='Hello ',
                    append=False,
                    last_chunk=False,
                ),
                _artifact_response(
                    task_id='task-1',
                    context_id='thread-1',
                    artifact_id='artifact-1',
                    text='world',
                    append=True,
                    last_chunk=True,
                ),
                _status_response(
                    task_id='task-1',
                    context_id='thread-1',
                    state=TaskState.TASK_STATE_COMPLETED,
                    text='Done.',
                ),
            ]
        )

        async def fake_factory(_target):
            return fake_client

        app = create_app(
            default_target=A2ATarget(url='http://agent'),
            client_factory=fake_factory,
        )
        transport = httpx.ASGITransport(app=app)

        async with httpx.AsyncClient(
            transport=transport,
            base_url='http://testserver',
        ) as client:
            response = await client.post(
                '/',
                headers={'accept': 'text/event-stream'},
                json={
                    'threadId': 'thread-1',
                    'runId': 'run-1',
                    'state': {},
                    'messages': [
                        {
                            'id': 'user-1',
                            'role': 'user',
                            'content': 'Say hello',
                        }
                    ],
                    'tools': [],
                    'context': [],
                    'forwardedProps': {},
                },
            )

        self.assertEqual(response.status_code, 200)
        events = _parse_sse_events(response.text)
        event_types = [event['type'] for event in events]
        self.assertIn('RUN_STARTED', event_types)
        self.assertIn('ACTIVITY_SNAPSHOT', event_types)
        self.assertIn('TEXT_MESSAGE_START', event_types)
        self.assertIn('TEXT_MESSAGE_CONTENT', event_types)
        self.assertIn('TEXT_MESSAGE_END', event_types)
        self.assertEqual(event_types[-1], 'RUN_FINISHED')

        text_chunks = [
            event['delta']
            for event in events
            if event['type'] == 'TEXT_MESSAGE_CONTENT'
        ]
        self.assertEqual(''.join(text_chunks), 'Hello world')
        self.assertIsNone(
            events[-2]['snapshot']['a2a']['taskId'],
        )
        self.assertTrue(fake_client.closed)

    async def test_input_required_response_keeps_task_in_adapter_state(self) -> None:
        fake_client = FakeClient(
            [
                _status_response(
                    task_id='task-9',
                    context_id='thread-9',
                    state=TaskState.TASK_STATE_INPUT_REQUIRED,
                    text='Please provide the account number.',
                )
            ]
        )

        async def fake_factory(_target):
            return fake_client

        app = create_app(
            default_target=A2ATarget(url='http://agent'),
            client_factory=fake_factory,
        )
        transport = httpx.ASGITransport(app=app)

        async with httpx.AsyncClient(
            transport=transport,
            base_url='http://testserver',
        ) as client:
            response = await client.post(
                '/',
                headers={'accept': 'text/event-stream'},
                json={
                    'threadId': 'thread-9',
                    'runId': 'run-9',
                    'state': {},
                    'messages': [
                        {
                            'id': 'user-9',
                            'role': 'user',
                            'content': 'Continue',
                        }
                    ],
                    'tools': [],
                    'context': [],
                    'forwardedProps': {},
                },
            )

        events = _parse_sse_events(response.text)
        final_state = [
            event for event in events if event['type'] == 'STATE_SNAPSHOT'
        ][-1]
        self.assertEqual(final_state['snapshot']['a2a']['taskId'], 'task-9')
        self.assertEqual(
            final_state['snapshot']['a2a']['taskState'],
            'input-required',
        )
        assistant_chunks = [
            event['delta']
            for event in events
            if event['type'] == 'TEXT_MESSAGE_CONTENT'
        ]
        self.assertEqual(
            ''.join(assistant_chunks),
            'Please provide the account number.',
        )
        self.assertEqual(events[-1]['type'], 'RUN_FINISHED')
        self.assertEqual(events[-1]['result']['taskState'], 'input-required')

    async def test_follow_up_request_reuses_paused_a2a_task(self) -> None:
        first_client = FakeClient(
            [
                _status_response(
                    task_id='task-77',
                    context_id='thread-77',
                    state=TaskState.TASK_STATE_INPUT_REQUIRED,
                    text='Need one more field.',
                )
            ]
        )
        second_client = FakeClient(
            [
                _status_response(
                    task_id='task-77',
                    context_id='thread-77',
                    state=TaskState.TASK_STATE_COMPLETED,
                    text='All done.',
                )
            ]
        )
        clients = [first_client, second_client]

        async def fake_factory(_target):
            return clients.pop(0)

        app = create_app(
            default_target=A2ATarget(url='http://agent'),
            client_factory=fake_factory,
        )
        transport = httpx.ASGITransport(app=app)

        async with httpx.AsyncClient(
            transport=transport,
            base_url='http://testserver',
        ) as client:
            await client.post(
                '/',
                headers={'accept': 'text/event-stream'},
                json={
                    'threadId': 'thread-77',
                    'runId': 'run-1',
                    'state': {},
                    'messages': [
                        {
                            'id': 'user-1',
                            'role': 'user',
                            'content': 'Start',
                        }
                    ],
                    'tools': [],
                    'context': [],
                    'forwardedProps': {},
                },
            )
            await client.post(
                '/',
                headers={'accept': 'text/event-stream'},
                json={
                    'threadId': 'thread-77',
                    'runId': 'run-2',
                    'state': {},
                    'messages': [
                        {
                            'id': 'user-1',
                            'role': 'user',
                            'content': 'Start',
                        },
                        {
                            'id': 'user-2',
                            'role': 'user',
                            'content': 'Here is the missing field',
                        },
                    ],
                    'tools': [],
                    'context': [],
                    'forwardedProps': {},
                },
            )

        self.assertEqual(len(first_client.requests), 1)
        self.assertEqual(len(second_client.requests), 1)
        self.assertEqual(
            second_client.requests[0].message.task_id,
            'task-77',
        )
        self.assertEqual(
            second_client.requests[0].message.context_id,
            'thread-77',
        )

    async def test_first_request_bootstraps_history_into_a2a_message(self) -> None:
        fake_client = FakeClient(
            [
                _status_response(
                    task_id='task-hist',
                    context_id='thread-hist',
                    state=TaskState.TASK_STATE_COMPLETED,
                    text='Done.',
                )
            ]
        )

        async def fake_factory(_target):
            return fake_client

        app = create_app(
            default_target=A2ATarget(url='http://agent'),
            client_factory=fake_factory,
        )
        transport = httpx.ASGITransport(app=app)

        async with httpx.AsyncClient(
            transport=transport,
            base_url='http://testserver',
        ) as client:
            await client.post(
                '/',
                headers={'accept': 'text/event-stream'},
                json={
                    'threadId': 'thread-hist',
                    'runId': 'run-hist',
                    'state': {},
                    'messages': [
                        {
                            'id': 'system-1',
                            'role': 'system',
                            'content': 'Use concise answers.',
                        },
                        {
                            'id': 'user-1',
                            'role': 'user',
                            'content': 'Summarize the previous meeting.',
                        },
                        {
                            'id': 'assistant-1',
                            'role': 'assistant',
                            'content': 'I can do that.',
                        },
                        {
                            'id': 'user-2',
                            'role': 'user',
                            'content': 'Also highlight action items.',
                        },
                    ],
                    'tools': [],
                    'context': [
                        {
                            'description': 'Tenant',
                            'value': 'retail-banking',
                        }
                    ],
                    'forwardedProps': {},
                },
            )

        outbound_text = '\n'.join(
            part.text for part in fake_client.requests[0].message.parts
        )
        self.assertIn('Additional AG-UI context', outbound_text)
        self.assertIn('[system]', outbound_text)
        self.assertIn('[assistant]', outbound_text)
        self.assertIn('Also highlight action items.', outbound_text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
