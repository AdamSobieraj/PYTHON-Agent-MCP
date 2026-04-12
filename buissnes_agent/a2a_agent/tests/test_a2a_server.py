import unittest

from contextlib import asynccontextmanager
from typing import Any
from unittest.mock import patch
from uuid import uuid4

import httpx

from google.protobuf.json_format import MessageToDict

from a2a.types import Message, Part, Role, SendMessageRequest
from buissnes_agent.a2a_agent.__main__ import _build_agent_card, _build_app
from buissnes_agent.a2a_agent.agent import AnalysisAgent


class A2AAgentServerTests(unittest.IsolatedAsyncioTestCase):
    @asynccontextmanager
    async def _test_client(self, stream_items: list[dict[str, Any]]):
        async def fake_stream(
            _self: AnalysisAgent,
            query: str,
            context_id: str,
        ):
            for item in stream_items:
                yield item

        with patch.object(AnalysisAgent, 'stream', new=fake_stream):
            app = _build_app(_build_agent_card('testserver', 10000))
            await app.router.startup()
            transport = httpx.ASGITransport(app=app)
            async with httpx.AsyncClient(
                transport=transport,
                base_url='http://testserver',
            ) as client:
                yield client
            await app.router.shutdown()

    def _send_message_payload(self, text: str) -> dict[str, Any]:
        request = SendMessageRequest(
            message=Message(
                role=Role.ROLE_USER,
                message_id=str(uuid4()),
                context_id=str(uuid4()),
                parts=[Part(text=text)],
            )
        )
        return MessageToDict(request)

    async def test_agent_card_exposes_a2a_1_0_interfaces(self) -> None:
        async with self._test_client([]) as client:
            response = await client.get('/.well-known/agent-card.json')

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['name'], 'Deep Research Agent')
        self.assertEqual(payload['defaultInputModes'], ['text'])
        self.assertIn(
            {
                'url': 'http://testserver:10000/',
                'protocolBinding': 'JSONRPC',
                'protocolVersion': '1.0',
            },
            payload['supportedInterfaces'],
        )
        self.assertIn(
            {
                'url': 'http://testserver:10000',
                'protocolBinding': 'HTTP+JSON',
                'protocolVersion': '1.0',
            },
            payload['supportedInterfaces'],
        )

    async def test_rest_send_message_returns_completed_task(self) -> None:
        stream_items = [
            {
                'is_task_complete': False,
                'require_user_input': False,
                'content': 'Processing your request...',
            },
            {
                'is_task_complete': True,
                'require_user_input': False,
                'content': 'Hello from the completed task.',
            },
        ]

        async with self._test_client(stream_items) as client:
            response = await client.post(
                '/message:send',
                json=self._send_message_payload('say hello'),
                headers={'A2A-Version': '1.0'},
            )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(
            payload['task']['status']['state'],
            'TASK_STATE_COMPLETED',
        )
        self.assertEqual(
            payload['task']['artifacts'][0]['parts'][0]['text'],
            'Hello from the completed task.',
        )

    async def test_jsonrpc_send_message_returns_input_required_task(self) -> None:
        stream_items = [
            {
                'is_task_complete': False,
                'require_user_input': True,
                'content': 'Please provide the missing document number.',
            }
        ]

        async with self._test_client(stream_items) as client:
            response = await client.post(
                '/',
                json={
                    'jsonrpc': '2.0',
                    'id': 'test-request',
                    'method': 'SendMessage',
                    'params': self._send_message_payload(
                        'continue with missing input'
                    ),
                },
                headers={'A2A-Version': '1.0'},
            )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        task = payload['result']['task']
        self.assertEqual(task['status']['state'], 'TASK_STATE_INPUT_REQUIRED')
        self.assertEqual(
            task['status']['message']['parts'][0]['text'],
            'Please provide the missing document number.',
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
