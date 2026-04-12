import unittest

from contextlib import asynccontextmanager
from typing import Any
from unittest.mock import patch
from uuid import uuid4

import grpc
import httpx

from google.protobuf.json_format import MessageToDict

from a2a.types import (
    Message,
    Part,
    Role,
    SendMessageRequest,
    TaskState,
    a2a_pb2_grpc,
)
from buissnes_agent.a2a_agent.__main__ import (
    _build_agent_card,
    _build_app,
    _build_grpc_server,
    _build_request_handler,
)
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
            agent_card = _build_agent_card(
                public_host='testserver',
                http_port=10000,
                grpc_port=10001,
                compat_grpc_port=10002,
            )
            request_handler = _build_request_handler(agent_card)
            app = _build_app(agent_card, request_handler)
            await app.router.startup()
            transport = httpx.ASGITransport(app=app)
            async with httpx.AsyncClient(
                transport=transport,
                base_url='http://testserver',
            ) as client:
                yield client
            await app.router.shutdown()

    @asynccontextmanager
    async def _grpc_stub(self, stream_items: list[dict[str, Any]]):
        async def fake_stream(
            _self: AnalysisAgent,
            query: str,
            context_id: str,
        ):
            for item in stream_items:
                yield item

        with patch.object(AnalysisAgent, 'stream', new=fake_stream):
            agent_card = _build_agent_card(
                public_host='127.0.0.1',
                http_port=10000,
                grpc_port=10001,
                compat_grpc_port=10002,
            )
            request_handler = _build_request_handler(agent_card)
            grpc_server, port = _build_grpc_server(
                request_handler=request_handler,
                bind_host='127.0.0.1',
                port=0,
                compat=False,
            )
            await grpc_server.start()
            async with grpc.aio.insecure_channel(f'127.0.0.1:{port}') as channel:
                await channel.channel_ready()
                stub = a2a_pb2_grpc.A2AServiceStub(channel)
                yield stub
            await grpc_server.stop(0)

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

    def _send_message_request(self, text: str) -> SendMessageRequest:
        return SendMessageRequest(
            message=Message(
                role=Role.ROLE_USER,
                message_id=str(uuid4()),
                context_id=str(uuid4()),
                parts=[Part(text=text)],
            )
        )

    async def test_agent_card_lists_explicit_transport_endpoints(self) -> None:
        async with self._test_client([]) as client:
            response = await client.get('/.well-known/agent-card.json')

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['name'], 'Deep Research Agent')
        self.assertEqual(payload['defaultInputModes'], ['text'])
        self.assertEqual(payload['url'], 'http://testserver:10000/a2a/jsonrpc')
        self.assertEqual(payload['preferredTransport'], 'JSONRPC')
        self.assertEqual(payload['protocolVersion'], '0.3')
        self.assertIn('additionalInterfaces', payload)
        self.assertIn(
            {
                'url': 'http://testserver:10000/a2a/jsonrpc',
                'protocolBinding': 'JSONRPC',
                'protocolVersion': '1.0',
            },
            payload['supportedInterfaces'],
        )
        self.assertIn(
            {
                'url': 'http://testserver:10000/a2a/rest',
                'protocolBinding': 'HTTP+JSON',
                'protocolVersion': '1.0',
            },
            payload['supportedInterfaces'],
        )
        self.assertIn(
            {
                'url': 'testserver:10001',
                'protocolBinding': 'GRPC',
                'protocolVersion': '1.0',
            },
            payload['supportedInterfaces'],
        )

    async def test_swagger_docs_expose_rest_get_routes(self) -> None:
        async with self._test_client([]) as client:
            docs_response = await client.get('/docs')
            openapi_response = await client.get('/openapi.json')

        self.assertEqual(docs_response.status_code, 200)
        self.assertEqual(openapi_response.status_code, 200)
        payload = openapi_response.json()
        self.assertIn('/a2a/rest/tasks', payload['paths'])
        self.assertIn('/a2a/rest/tasks/{id}', payload['paths'])
        self.assertIn('get', payload['paths']['/a2a/rest/tasks'])
        self.assertIn('get', payload['paths']['/a2a/rest/tasks/{id}'])

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
                '/a2a/rest/message:send',
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
                '/a2a/jsonrpc',
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

    async def test_grpc_send_message_returns_completed_task(self) -> None:
        stream_items = [
            {
                'is_task_complete': True,
                'require_user_input': False,
                'content': 'Hello from gRPC.',
            }
        ]

        async with self._grpc_stub(stream_items) as stub:
            response = await stub.SendMessage(
                self._send_message_request('hello over grpc')
            )

        self.assertEqual(
            TaskState.Name(response.task.status.state),
            'TASK_STATE_COMPLETED',
        )
        self.assertEqual(
            response.task.artifacts[0].parts[0].text,
            'Hello from gRPC.',
        )


if __name__ == '__main__':
    unittest.main(verbosity=2)
