import json
import os
import unittest

from contextlib import contextmanager
from contextlib import asynccontextmanager
from types import SimpleNamespace
from typing import Any
from unittest.mock import AsyncMock, patch
from uuid import uuid4

import grpc
import httpx
import openai

from google.protobuf.json_format import MessageToDict
from langchain_core.messages import AIMessage, ToolMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.utils.function_calling import convert_to_openai_function

from a2a.types import (
    Message,
    Part,
    Role,
    SendMessageRequest,
    TaskState,
    a2a_pb2_grpc,
)
from buissnes_agent.a2a_agent.__main__ import (
    _apply_runtime_config_to_agent_card,
    _build_agent_card,
    _build_app,
    _build_grpc_server,
    _build_request_handler,
)
from buissnes_agent.a2a_agent.ag_ui import (
    Message as AgUiMessage,
    RunAgentInput,
    RunFinishedEvent,
    RunStartedEvent,
    StateSnapshotEvent,
    TextMessageContentEvent,
    TextMessageEndEvent,
    TextMessageStartEvent,
)
from buissnes_agent.a2a_agent.agent import (
    AnalysisAgent,
    LangfuseRequest,
    ResponseFormat,
)
from buissnes_agent.a2a_agent.agent_executor import AnalysisAgentExecutor
from buissnes_agent.a2a_agent.mcp_config import AgentRuntimeConfig


class A2AAgentServerTests(unittest.IsolatedAsyncioTestCase):
    def _parse_sse_events(self, payload: str) -> list[dict[str, Any]]:
        events: list[dict[str, Any]] = []
        for block in payload.split('\n\n'):
            block = block.strip()
            if not block:
                continue
            if not block.startswith('data: '):
                continue
            events.append(json.loads(block[len('data: ') :]))
        return events

    @asynccontextmanager
    async def _test_client(
        self,
        stream_items: list[dict[str, Any]],
        *,
        stream_error: Exception | None = None,
    ):
        async def fake_stream(
            _self: AnalysisAgent,
            query: str,
            context_id: str,
            **_: Any,
        ):
            if stream_error is not None:
                raise stream_error
                yield  # pragma: no cover
            for item in stream_items:
                yield item

        with (
            patch.object(AnalysisAgent, 'stream', new=fake_stream),
            patch.object(
                AnalysisAgent,
                'create_langfuse_trace_id',
                return_value=None,
            ),
            patch.object(AnalysisAgentExecutor, 'startup', new=AsyncMock()),
            patch.object(AnalysisAgentExecutor, 'shutdown', new=AsyncMock()),
        ):
            agent_card = _build_agent_card(
                public_host='testserver',
                http_port=10000,
                grpc_port=10001,
                compat_grpc_port=10002,
            )
            agent_executor = AnalysisAgentExecutor()
            request_handler = _build_request_handler(
                agent_card,
                agent_executor,
            )
            app = _build_app(agent_card, request_handler, agent_executor)
            async with app.router.lifespan_context(app):
                transport = httpx.ASGITransport(app=app)
                async with httpx.AsyncClient(
                    transport=transport,
                    base_url='http://testserver',
                ) as client:
                    yield client

    @asynccontextmanager
    async def _grpc_stub(self, stream_items: list[dict[str, Any]]):
        async def fake_stream(
            _self: AnalysisAgent,
            query: str,
            context_id: str,
            **_: Any,
        ):
            for item in stream_items:
                yield item

        with (
            patch.object(AnalysisAgent, 'stream', new=fake_stream),
            patch.object(
                AnalysisAgent,
                'create_langfuse_trace_id',
                return_value=None,
            ),
        ):
            agent_card = _build_agent_card(
                public_host='127.0.0.1',
                http_port=10000,
                grpc_port=10001,
                compat_grpc_port=10002,
            )
            agent_executor = AnalysisAgentExecutor()
            request_handler = _build_request_handler(
                agent_card,
                agent_executor,
            )
            grpc_server, port = await _build_grpc_server(
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

    def test_build_agent_card_uses_runtime_config_overrides(self) -> None:
        runtime_config = AgentRuntimeConfig(
            prompt='test',
            config={
                'agent_card': {
                    'name': 'Audit-backed Analyst',
                    'description': 'Published from Langfuse prompt config.',
                    'version': '2.1.0',
                    'documentation_url': 'https://docs.example.com/agent',
                    'icon_url': 'https://docs.example.com/icon.png',
                    'provider': {
                        'organization': 'Risk Systems',
                        'url': 'https://agents.example.com',
                    },
                    'capabilities': {
                        'streaming': False,
                        'push_notifications': True,
                        'extended_agent_card': True,
                    },
                    'skills': [
                        {
                            'id': 'audit_analysis',
                            'name': 'Audit Analysis',
                            'description': 'Explains audit-backed settings.',
                            'tags': ['audit', 'analysis'],
                        }
                    ],
                }
            },
        )

        agent_card = _build_agent_card(
            public_host='testserver',
            http_port=10000,
            grpc_port=10001,
            compat_grpc_port=10002,
            runtime_config=runtime_config,
        )

        self.assertEqual(agent_card.name, 'Audit-backed Analyst')
        self.assertEqual(
            agent_card.description,
            'Published from Langfuse prompt config.',
        )
        self.assertEqual(agent_card.version, '2.1.0')
        self.assertEqual(
            agent_card.documentation_url,
            'https://docs.example.com/agent',
        )
        self.assertEqual(
            agent_card.icon_url,
            'https://docs.example.com/icon.png',
        )
        self.assertEqual(
            agent_card.provider.organization,
            'Risk Systems',
        )
        self.assertEqual(
            agent_card.provider.url,
            'https://agents.example.com',
        )
        self.assertFalse(agent_card.capabilities.streaming)
        self.assertTrue(agent_card.capabilities.push_notifications)
        self.assertTrue(agent_card.capabilities.extended_agent_card)
        self.assertEqual(agent_card.skills[0].id, 'audit_analysis')
        self.assertEqual(
            list(agent_card.skills[0].input_modes),
            ['text'],
        )
        self.assertEqual(
            list(agent_card.skills[0].output_modes),
            ['text', 'task-status'],
        )

    def test_apply_runtime_config_to_agent_card_updates_existing_card(self) -> None:
        agent_card = _build_agent_card(
            public_host='testserver',
            http_port=10000,
            grpc_port=10001,
            compat_grpc_port=10002,
        )
        runtime_config = AgentRuntimeConfig(
            prompt='test',
            config={
                'agentCard': {
                    'name': 'Prompt Config Agent',
                    'provider': {
                        'organization': 'Prompt Team',
                    },
                    'skills': [
                        {
                            'id': 'prompt_skill',
                            'name': 'Prompt Skill',
                            'description': 'Defined in prompt config.',
                            'tags': ['prompt'],
                            'inputModes': ['text'],
                            'outputModes': ['text', 'task-status'],
                        }
                    ],
                }
            },
        )

        _apply_runtime_config_to_agent_card(
            agent_card,
            runtime_config,
            public_host='testserver',
            http_port=10000,
            grpc_port=10001,
            compat_grpc_port=10002,
        )

        self.assertEqual(agent_card.name, 'Prompt Config Agent')
        self.assertEqual(
            agent_card.provider.organization,
            'Prompt Team',
        )
        self.assertEqual(agent_card.skills[0].id, 'prompt_skill')

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
            payload['task']['status']['message']['parts'][0]['text'],
            'Hello from the completed task.',
        )
        self.assertEqual(
            payload['task']['artifacts'][0]['parts'][0]['text'],
            'Hello from the completed task.',
        )

    async def test_ag_ui_endpoint_streams_sse_events(self) -> None:
        async def fake_stream_ag_ui(
            _self: AnalysisAgent,
            run_input: RunAgentInput,
        ):
            yield RunStartedEvent(
                thread_id=run_input.thread_id,
                run_id=run_input.run_id,
            )
            yield TextMessageStartEvent(message_id='assistant-1')
            yield TextMessageContentEvent(
                message_id='assistant-1',
                delta='Hello from AG-UI.',
            )
            yield TextMessageEndEvent(message_id='assistant-1')
            yield RunFinishedEvent(
                thread_id=run_input.thread_id,
                run_id=run_input.run_id,
                result={'taskState': 'completed'},
            )

        with (
            patch.object(AnalysisAgent, 'stream_ag_ui', new=fake_stream_ag_ui),
            patch.object(AnalysisAgentExecutor, 'startup', new=AsyncMock()),
            patch.object(AnalysisAgentExecutor, 'shutdown', new=AsyncMock()),
        ):
            agent_card = _build_agent_card(
                public_host='testserver',
                http_port=10000,
                grpc_port=10001,
                compat_grpc_port=10002,
            )
            agent_executor = AnalysisAgentExecutor()
            request_handler = _build_request_handler(
                agent_card,
                agent_executor,
            )
            app = _build_app(agent_card, request_handler, agent_executor)

            async with app.router.lifespan_context(app):
                transport = httpx.ASGITransport(app=app)
                async with httpx.AsyncClient(
                    transport=transport,
                    base_url='http://testserver',
                ) as client:
                    response = await client.post(
                        '/ag-ui',
                        json={
                            'threadId': 'thread-1',
                            'runId': 'run-1',
                            'messages': [
                                {
                                    'id': 'user-1',
                                    'role': 'user',
                                    'content': 'hello',
                                }
                            ],
                        },
                    )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            response.headers['content-type'].startswith('text/event-stream')
        )
        events = self._parse_sse_events(response.text)
        self.assertEqual(
            [event['type'] for event in events],
            [
                'RUN_STARTED',
                'TEXT_MESSAGE_START',
                'TEXT_MESSAGE_CONTENT',
                'TEXT_MESSAGE_END',
                'RUN_FINISHED',
            ],
        )
        self.assertEqual(events[0]['threadId'], 'thread-1')
        self.assertEqual(events[2]['delta'], 'Hello from AG-UI.')

    async def test_ag_ui_root_endpoint_streams_sse_events(self) -> None:
        async def fake_stream_ag_ui(
            _self: AnalysisAgent,
            run_input: RunAgentInput,
        ):
            yield RunStartedEvent(
                thread_id=run_input.thread_id,
                run_id=run_input.run_id,
            )
            yield TextMessageStartEvent(message_id='assistant-1')
            yield TextMessageContentEvent(
                message_id='assistant-1',
                delta='Hello from root AG-UI.',
            )
            yield TextMessageEndEvent(message_id='assistant-1')
            yield RunFinishedEvent(
                thread_id=run_input.thread_id,
                run_id=run_input.run_id,
                result={'taskState': 'completed'},
            )

        with (
            patch.object(AnalysisAgent, 'stream_ag_ui', new=fake_stream_ag_ui),
            patch.object(AnalysisAgentExecutor, 'startup', new=AsyncMock()),
            patch.object(AnalysisAgentExecutor, 'shutdown', new=AsyncMock()),
        ):
            agent_card = _build_agent_card(
                public_host='testserver',
                http_port=10000,
                grpc_port=10001,
                compat_grpc_port=10002,
            )
            agent_executor = AnalysisAgentExecutor()
            request_handler = _build_request_handler(
                agent_card,
                agent_executor,
            )
            app = _build_app(agent_card, request_handler, agent_executor)

            async with app.router.lifespan_context(app):
                transport = httpx.ASGITransport(app=app)
                async with httpx.AsyncClient(
                    transport=transport,
                    base_url='http://testserver',
                ) as client:
                    response = await client.post(
                        '/',
                        json={
                            'threadId': 'thread-1',
                            'runId': 'run-1',
                            'messages': [
                                {
                                    'id': 'user-1',
                                    'role': 'user',
                                    'content': 'hello',
                                }
                            ],
                        },
                    )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            response.headers['content-type'].startswith('text/event-stream')
        )
        events = self._parse_sse_events(response.text)
        self.assertEqual(events[0]['type'], 'RUN_STARTED')
        self.assertEqual(events[2]['delta'], 'Hello from root AG-UI.')

    async def test_catalog_endpoint_returns_runtime_snapshot(self) -> None:
        with (
            patch.object(AnalysisAgentExecutor, 'startup', new=AsyncMock()),
            patch.object(AnalysisAgentExecutor, 'shutdown', new=AsyncMock()),
        ):
            agent_card = _build_agent_card(
                public_host='testserver',
                http_port=10000,
                grpc_port=10001,
                compat_grpc_port=10002,
            )
            agent_executor = AnalysisAgentExecutor()
            agent_executor.agent.tools = [
                SimpleNamespace(name='search_docs', description='Find docs')
            ]
            request_handler = _build_request_handler(
                agent_card,
                agent_executor,
            )
            app = _build_app(agent_card, request_handler, agent_executor)

            async with app.router.lifespan_context(app):
                transport = httpx.ASGITransport(app=app)
                async with httpx.AsyncClient(
                    transport=transport,
                    base_url='http://testserver',
                ) as client:
                    response = await client.get('/catalog')

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['configPath'], 'default_config.json')
        self.assertEqual(payload['a2aAgents'][0]['name'], 'Deep Research Agent')
        self.assertEqual(payload['mcpTools'][0]['toolName'], 'search_docs')
        self.assertEqual(payload['warnings'], [])

    async def test_ag_ui_info_endpoint_describes_content_negotiation(self) -> None:
        with (
            patch.object(AnalysisAgentExecutor, 'startup', new=AsyncMock()),
            patch.object(AnalysisAgentExecutor, 'shutdown', new=AsyncMock()),
        ):
            agent_card = _build_agent_card(
                public_host='testserver',
                http_port=10000,
                grpc_port=10001,
                compat_grpc_port=10002,
            )
            agent_executor = AnalysisAgentExecutor()
            request_handler = _build_request_handler(
                agent_card,
                agent_executor,
            )
            app = _build_app(agent_card, request_handler, agent_executor)

            async with app.router.lifespan_context(app):
                transport = httpx.ASGITransport(app=app)
                async with httpx.AsyncClient(
                    transport=transport,
                    base_url='http://testserver',
                ) as client:
                    response = await client.get('/ag-ui')

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['content_type'], 'text/event-stream')
        self.assertEqual(
            payload['supported_content_types'],
            ['text/event-stream', 'application/x-ndjson'],
        )
        self.assertEqual(
            payload['content_negotiation']['request_header'],
            'Accept',
        )

    async def test_ag_ui_endpoint_respects_ndjson_accept_header(self) -> None:
        async def fake_stream_ag_ui(
            _self: AnalysisAgent,
            run_input: RunAgentInput,
        ):
            yield RunStartedEvent(
                thread_id=run_input.thread_id,
                run_id=run_input.run_id,
            )
            yield StateSnapshotEvent(snapshot={'mode': 'ndjson'})
            yield RunFinishedEvent(
                thread_id=run_input.thread_id,
                run_id=run_input.run_id,
            )

        with (
            patch.object(AnalysisAgent, 'stream_ag_ui', new=fake_stream_ag_ui),
            patch.object(AnalysisAgentExecutor, 'startup', new=AsyncMock()),
            patch.object(AnalysisAgentExecutor, 'shutdown', new=AsyncMock()),
        ):
            agent_card = _build_agent_card(
                public_host='testserver',
                http_port=10000,
                grpc_port=10001,
                compat_grpc_port=10002,
            )
            agent_executor = AnalysisAgentExecutor()
            request_handler = _build_request_handler(
                agent_card,
                agent_executor,
            )
            app = _build_app(agent_card, request_handler, agent_executor)

            async with app.router.lifespan_context(app):
                transport = httpx.ASGITransport(app=app)
                async with httpx.AsyncClient(
                    transport=transport,
                    base_url='http://testserver',
                ) as client:
                    response = await client.post(
                        '/ag-ui',
                        headers={'accept': 'application/json'},
                        json={
                            'threadId': 'thread-1',
                            'runId': 'run-1',
                            'messages': [
                                {
                                    'id': 'user-1',
                                    'role': 'user',
                                    'content': 'hello',
                                }
                            ],
                        },
                    )

        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            response.headers['content-type'].startswith(
                'application/x-ndjson'
            )
        )
        self.assertFalse(response.text.startswith('data: '))
        first_line = response.text.splitlines()[0]
        self.assertEqual(json.loads(first_line)['type'], 'RUN_STARTED')

    async def test_ag_ui_endpoint_rejects_missing_messages(self) -> None:
        with (
            patch.object(AnalysisAgentExecutor, 'startup', new=AsyncMock()),
            patch.object(AnalysisAgentExecutor, 'shutdown', new=AsyncMock()),
        ):
            agent_card = _build_agent_card(
                public_host='testserver',
                http_port=10000,
                grpc_port=10001,
                compat_grpc_port=10002,
            )
            agent_executor = AnalysisAgentExecutor()
            request_handler = _build_request_handler(
                agent_card,
                agent_executor,
            )
            app = _build_app(agent_card, request_handler, agent_executor)

            async with app.router.lifespan_context(app):
                transport = httpx.ASGITransport(app=app)
                async with httpx.AsyncClient(
                    transport=transport,
                    base_url='http://testserver',
                ) as client:
                    response = await client.post(
                        '/ag-ui',
                        json={
                            'threadId': 'thread-1',
                            'runId': 'run-1',
                            'messages': [],
                        },
                    )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()['detail'],
            'AG-UI requests require at least one message.',
        )

    async def test_ag_ui_endpoint_rejects_missing_user_text(self) -> None:
        with (
            patch.object(AnalysisAgentExecutor, 'startup', new=AsyncMock()),
            patch.object(AnalysisAgentExecutor, 'shutdown', new=AsyncMock()),
        ):
            agent_card = _build_agent_card(
                public_host='testserver',
                http_port=10000,
                grpc_port=10001,
                compat_grpc_port=10002,
            )
            agent_executor = AnalysisAgentExecutor()
            request_handler = _build_request_handler(
                agent_card,
                agent_executor,
            )
            app = _build_app(agent_card, request_handler, agent_executor)

            async with app.router.lifespan_context(app):
                transport = httpx.ASGITransport(app=app)
                async with httpx.AsyncClient(
                    transport=transport,
                    base_url='http://testserver',
                ) as client:
                    response = await client.post(
                        '/ag-ui',
                        json={
                            'threadId': 'thread-1',
                            'runId': 'run-1',
                            'messages': [
                                {
                                    'id': 'assistant-1',
                                    'role': 'assistant',
                                    'content': 'hello',
                                }
                            ],
                        },
                    )

        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.json()['detail'],
            'AG-UI requests require a user text message.',
        )

    async def test_rest_send_message_returns_failed_task_with_context_error(
        self,
    ) -> None:
        request = httpx.Request(
            'POST',
            'http://testserver/v1/chat/completions',
        )
        response = httpx.Response(
            400,
            request=request,
            json={
                'error': {
                    'message': (
                        "This model's maximum context length is 16384 tokens. "
                        'However, your request has 23425 input tokens. '
                        'Please reduce the length of the input messages. None'
                    ),
                    'type': 'BadRequestError',
                    'param': None,
                    'code': 400,
                }
            },
        )
        stream_error = openai.BadRequestError(
            'Error code: 400',
            response=response,
            body=response.json(),
        )

        async with self._test_client([], stream_error=stream_error) as client:
            response = await client.post(
                '/a2a/rest/message:send',
                json=self._send_message_payload('say hello'),
                headers={'A2A-Version': '1.0'},
            )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['task']['status']['state'], 'TASK_STATE_FAILED')
        message = payload['task']['status']['message']['parts'][0]['text']
        self.assertIn('23425 input tokens', message)
        self.assertIn('16384', message)
        self.assertIn('fresh context', message)

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
            response.task.status.message.parts[0].text,
            'Hello from gRPC.',
        )
        self.assertEqual(
            response.task.artifacts[0].parts[0].text,
            'Hello from gRPC.',
        )

    async def test_rest_completed_task_can_publish_distinct_status_summary(
        self,
    ) -> None:
        stream_items = [
            {
                'task_state': 'completed',
                'content': 'Detailed answer artifact.',
                'status_message': 'Short completion summary.',
            }
        ]

        async with self._test_client(stream_items) as client:
            response = await client.post(
                '/a2a/rest/message:send',
                json=self._send_message_payload('summarize the result'),
                headers={'A2A-Version': '1.0'},
            )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(
            payload['task']['status']['message']['parts'][0]['text'],
            'Short completion summary.',
        )
        self.assertEqual(
            payload['task']['artifacts'][0]['parts'][0]['text'],
            'Detailed answer artifact.',
        )

    async def test_app_lifecycle_starts_and_stops_agent_refresh(self) -> None:
        startup_mock = AsyncMock()
        shutdown_mock = AsyncMock()

        with (
            patch.object(AnalysisAgentExecutor, 'startup', startup_mock),
            patch.object(AnalysisAgentExecutor, 'shutdown', shutdown_mock),
        ):
            agent_card = _build_agent_card(
                public_host='testserver',
                http_port=10000,
                grpc_port=10001,
                compat_grpc_port=10002,
            )
            agent_executor = AnalysisAgentExecutor()
            request_handler = _build_request_handler(
                agent_card,
                agent_executor,
            )
            app = _build_app(agent_card, request_handler, agent_executor)

            async with app.router.lifespan_context(app):
                pass

        startup_mock.assert_awaited_once()
        shutdown_mock.assert_awaited_once()

    async def test_analysis_agent_stream_emits_status_updates(self) -> None:
        class FakeGraph:
            async def astream(
                self,
                inputs: dict[str, Any],
                config: dict[str, Any],
                stream_mode: list[str],
                version: str,
            ):
                self.inputs = inputs
                self.config = config
                self.stream_mode = stream_mode
                self.version = version

                yield {
                    'type': 'custom',
                    'data': {
                        'event': 'tool_started',
                        'tool_name': 'search_docs',
                        'tool_args': {'query': 'context limit'},
                    },
                }
                yield {
                    'type': 'updates',
                    'data': {
                        'tools': {
                            'messages': [
                                ToolMessage(
                                    content='Found matching documents',
                                    tool_call_id='call-1',
                                )
                            ]
                        }
                    },
                }
                yield {
                    'type': 'updates',
                    'data': {
                        'agent': {
                            'messages': [AIMessage(content='Final answer draft')]
                        }
                    },
                }

            async def aget_state(self, config: dict[str, Any]):
                return SimpleNamespace(
                    values={
                        'messages': [AIMessage(content='Final answer draft')],
                        'structured_response': ResponseFormat(
                            status='completed',
                            message='Final answer draft',
                        ),
                    }
                )

        agent = AnalysisAgent()
        agent.graph = FakeGraph()
        agent._langfuse_initialized = True
        agent.langfuse_enabled = False

        items = []
        async for item in agent.stream('How big is the context?', 'ctx-1'):
            items.append(item)

        self.assertIn('Running tool search_docs.', items[0]['content'])
        self.assertEqual(items[1]['content'], 'Reviewing tool results...')
        self.assertEqual(items[2]['content'], 'Drafting the final response...')
        self.assertEqual(items[-1]['task_state'], 'completed')
        self.assertEqual(items[-1]['content'], 'Final answer draft')
        self.assertEqual(items[-1]['status_message'], 'Final answer draft')
        self.assertEqual(agent.graph.stream_mode, ['updates', 'custom'])
        self.assertEqual(agent.graph.version, 'v2')

    async def test_analysis_agent_stream_ag_ui_emits_protocol_events(
        self,
    ) -> None:
        class FakeGraph:
            async def astream(
                self,
                inputs: dict[str, Any],
                config: dict[str, Any],
                stream_mode: list[str],
                version: str,
            ):
                self.inputs = inputs
                self.config = config
                self.stream_mode = stream_mode
                self.version = version

                yield {
                    'type': 'messages',
                    'data': (
                        AIMessage(content='Looking up the answer. '),
                        {'langgraph_node': 'agent'},
                    ),
                }
                yield {
                    'type': 'updates',
                    'data': {
                        'agent': {
                            'messages': [
                                AIMessage(
                                    content='',
                                    tool_calls=[
                                        {
                                            'name': 'search_docs',
                                            'args': {'query': 'context limit'},
                                            'id': 'call-1',
                                        }
                                    ],
                                )
                            ]
                        }
                    },
                }
                yield {
                    'type': 'updates',
                    'data': {
                        'tools': {
                            'messages': [
                                ToolMessage(
                                    content='Found supporting material.',
                                    tool_call_id='call-1',
                                    id='tool-msg-1',
                                )
                            ]
                        }
                    },
                }
                yield {
                    'type': 'messages',
                    'data': (
                        AIMessage(content='Final answer ready.'),
                        {'langgraph_node': 'agent'},
                    ),
                }
                yield {
                    'type': 'messages',
                    'data': (
                        AIMessage(
                            content='{"status":"completed","message":"ignore me"}'
                        ),
                        {'langgraph_node': 'generate_structured_response'},
                    ),
                }

            async def aget_state(self, config: dict[str, Any]):
                return SimpleNamespace(
                    values={
                        'messages': [
                            AIMessage(
                                content='Looking up the answer. Final answer ready.'
                            )
                        ],
                        'structured_response': ResponseFormat(
                            status='completed',
                            message='Looking up the answer. Final answer ready.',
                        ),
                    }
                )

        agent = AnalysisAgent()
        agent.graph = FakeGraph()
        agent._langfuse_initialized = True
        agent.langfuse_enabled = False

        run_input = RunAgentInput(
            thread_id='thread-1',
            run_id='run-1',
            messages=[
                AgUiMessage(
                    id='user-1',
                    role='user',
                    content=[
                        {'type': 'text', 'text': 'What is the context limit?'}
                    ],
                )
            ],
        )

        events = []
        async for event in agent.stream_ag_ui(run_input):
            events.append(event.model_dump(by_alias=True, exclude_none=True))

        self.assertEqual(events[0]['type'], 'RUN_STARTED')
        self.assertEqual(events[1]['type'], 'STATE_SNAPSHOT')
        self.assertEqual(events[1]['snapshot'], {})
        self.assertEqual(events[2]['type'], 'STEP_STARTED')
        self.assertIn(
            'ACTIVITY_SNAPSHOT',
            [event['type'] for event in events],
        )
        self.assertIn('TEXT_MESSAGE_START', [event['type'] for event in events])
        self.assertIn('TOOL_CALL_START', [event['type'] for event in events])
        self.assertIn('TOOL_CALL_RESULT', [event['type'] for event in events])
        self.assertEqual(events[-1]['type'], 'RUN_FINISHED')
        self.assertEqual(
            events[-1]['result']['taskState'],
            'completed',
        )
        activity_messages = [
            event['content']['message']
            for event in events
            if event['type'] == 'ACTIVITY_SNAPSHOT'
        ]
        self.assertIn(
            'Planning the next action: search_docs.',
            activity_messages,
        )
        self.assertIn(
            'Reviewing tool results...',
            activity_messages,
        )
        self.assertTrue(
            all(
                event.get('replace') is True
                for event in events
                if event['type'] == 'ACTIVITY_SNAPSHOT'
            )
        )
        text_deltas = [
            event['delta']
            for event in events
            if event['type'] == 'TEXT_MESSAGE_CONTENT'
        ]
        self.assertEqual(
            text_deltas,
            ['Looking up the answer. ', 'Final answer ready.'],
        )
        self.assertEqual(agent.graph.stream_mode, ['messages', 'updates', 'custom'])
        self.assertEqual(agent.graph.version, 'v2')
        self.assertEqual(len(agent.graph.inputs['messages']), 1)
        self.assertEqual(agent.graph.inputs['messages'][0].type, 'human')

    async def test_analysis_agent_stream_ag_ui_parents_tool_calls_before_text(
        self,
    ) -> None:
        class FakeGraph:
            async def astream(
                self,
                inputs: dict[str, Any],
                config: dict[str, Any],
                stream_mode: list[str],
                version: str,
            ):
                yield {
                    'type': 'updates',
                    'data': {
                        'agent': {
                            'messages': [
                                AIMessage(
                                    content='',
                                    tool_calls=[
                                        {
                                            'name': 'calculator',
                                            'args': {'expression': '2+2'},
                                            'id': 'call-42',
                                        }
                                    ],
                                )
                            ]
                        }
                    },
                }
                yield {
                    'type': 'updates',
                    'data': {
                        'tools': {
                            'messages': [
                                ToolMessage(
                                    content='4',
                                    tool_call_id='call-42',
                                    id='tool-msg-42',
                                )
                            ]
                        }
                    },
                }
                yield {
                    'type': 'messages',
                    'data': (
                        AIMessage(content='The answer is 4.'),
                        {'langgraph_node': 'agent'},
                    ),
                }

            async def aget_state(self, config: dict[str, Any]):
                return SimpleNamespace(
                    values={
                        'messages': [AIMessage(content='The answer is 4.')],
                        'structured_response': ResponseFormat(
                            status='completed',
                            message='The answer is 4.',
                        ),
                    }
                )

        agent = AnalysisAgent()
        agent.graph = FakeGraph()
        agent._langfuse_initialized = True
        agent.langfuse_enabled = False

        run_input = RunAgentInput(
            thread_id='thread-42',
            run_id='run-42',
            state={'filters': {'scope': 'all'}},
            messages=[
                AgUiMessage(id='user-1', role='user', content='2+2=?')
            ],
        )

        events = []
        async for event in agent.stream_ag_ui(run_input):
            events.append(event.model_dump(by_alias=True, exclude_none=True))

        state_snapshot = next(
            event for event in events if event['type'] == 'STATE_SNAPSHOT'
        )
        tool_start = next(
            event for event in events if event['type'] == 'TOOL_CALL_START'
        )
        text_start = next(
            event for event in events if event['type'] == 'TEXT_MESSAGE_START'
        )
        text_start_index = next(
            index
            for index, event in enumerate(events)
            if event['type'] == 'TEXT_MESSAGE_START'
        )
        tool_start_index = next(
            index
            for index, event in enumerate(events)
            if event['type'] == 'TOOL_CALL_START'
        )
        text_deltas = [
            event['delta']
            for event in events
            if event['type'] == 'TEXT_MESSAGE_CONTENT'
        ]

        self.assertEqual(
            state_snapshot['snapshot'],
            {'filters': {'scope': 'all'}},
        )
        self.assertEqual(tool_start['parentMessageId'], text_start['messageId'])
        self.assertLess(text_start_index, tool_start_index)
        self.assertEqual(text_deltas, ['The answer is 4.'])

    async def test_analysis_agent_stream_ag_ui_emits_run_error_event(self) -> None:
        class FailingGraph:
            async def astream(
                self,
                inputs: dict[str, Any],
                config: dict[str, Any],
                stream_mode: list[str],
                version: str,
            ):
                raise RuntimeError('AG-UI graph failure')
                yield  # pragma: no cover

        agent = AnalysisAgent()
        agent.graph = FailingGraph()
        agent._langfuse_initialized = True
        agent.langfuse_enabled = False

        run_input = RunAgentInput(
            thread_id='thread-1',
            run_id='run-1',
            messages=[AgUiMessage(id='user-1', role='user', content='hello')],
        )

        events = []
        async for event in agent.stream_ag_ui(run_input):
            events.append(event.model_dump(by_alias=True, exclude_none=True))

        self.assertEqual(events[0]['type'], 'RUN_STARTED')
        self.assertEqual(events[-1]['type'], 'RUN_ERROR')
        self.assertEqual(events[-1]['message'], 'AG-UI graph failure')

    async def test_analysis_agent_stream_ag_ui_falls_back_to_full_final_output(
        self,
    ) -> None:
        class DivergingGraph:
            async def astream(
                self,
                inputs: dict[str, Any],
                config: dict[str, Any],
                stream_mode: list[str],
                version: str,
            ):
                yield {
                    'type': 'messages',
                    'data': (
                        AIMessage(content='Draft answer'),
                        {'langgraph_node': 'agent'},
                    ),
                }

            async def aget_state(self, config: dict[str, Any]):
                return SimpleNamespace(
                    values={
                        'messages': [AIMessage(content='Final polished answer.')],
                        'structured_response': {
                            'status': 'completed',
                            'message': 'Final polished answer.',
                        },
                    }
                )

        agent = AnalysisAgent()
        agent.graph = DivergingGraph()
        agent._langfuse_initialized = True
        agent.langfuse_enabled = False

        run_input = RunAgentInput(
            thread_id='thread-1',
            run_id='run-1',
            messages=[AgUiMessage(id='user-1', role='user', content='hello')],
        )

        events = []
        async for event in agent.stream_ag_ui(run_input):
            events.append(event.model_dump(by_alias=True, exclude_none=True))

        text_deltas = [
            event['delta']
            for event in events
            if event['type'] == 'TEXT_MESSAGE_CONTENT'
        ]

        self.assertEqual(
            text_deltas,
            ['Draft answer', 'Final polished answer.'],
        )

    async def test_get_agent_response_separates_artifact_from_status_message(
        self,
    ) -> None:
        agent = AnalysisAgent()
        agent.graph = SimpleNamespace(
            aget_state=AsyncMock(
                return_value=SimpleNamespace(
                    values={
                        'messages': [
                            AIMessage(
                                content='Detailed final answer with supporting context.'
                            )
                        ],
                        'structured_response': ResponseFormat(
                            status='completed',
                            message='Short completion summary.',
                        ),
                    }
                )
            )
        )
        agent._langfuse_initialized = True
        agent.langfuse_enabled = False

        response = await agent.get_agent_response({'configurable': {}})

        self.assertEqual(response['task_state'], 'completed')
        self.assertEqual(
            response['content'],
            'Detailed final answer with supporting context.',
        )
        self.assertEqual(
            response['status_message'],
            'Short completion summary.',
        )

    async def test_get_agent_response_accepts_dict_structured_response(
        self,
    ) -> None:
        agent = AnalysisAgent()
        agent.graph = SimpleNamespace(
            aget_state=AsyncMock(
                return_value=SimpleNamespace(
                    values={
                        'messages': [AIMessage(content='The answer is 4.')],
                        'structured_response': {
                            'status': 'completed',
                            'message': 'The answer is 4.',
                        },
                    }
                )
            )
        )
        agent._langfuse_initialized = True
        agent.langfuse_enabled = False

        response = await agent.get_agent_response({'configurable': {}})

        self.assertEqual(response['task_state'], 'completed')
        self.assertEqual(response['content'], 'The answer is 4.')
        self.assertEqual(response['status_message'], 'The answer is 4.')

    def test_response_format_schema_is_openai_function_compatible(self) -> None:
        function_schema = convert_to_openai_function(
            AnalysisAgent.RESPONSE_FORMAT_SCHEMA
        )

        self.assertEqual(function_schema['name'], 'ResponseFormat')
        self.assertIn('parameters', function_schema)

    def test_build_langfuse_request_uses_a2a_identifiers(self) -> None:
        with patch.dict(os.environ, {'AGENT_SETTINGS': 'Analyst agent'}):
            executor = AnalysisAgentExecutor()
            executor.agent.create_langfuse_trace_id = (
                lambda seed: '0123456789abcdef0123456789abcdef'
            )

            context = SimpleNamespace(
                metadata={
                    'langfuse_tags': ['priority'],
                    'langfuse_trace_name': 'Custom request trace',
                },
                message=SimpleNamespace(
                    message_id='msg-1',
                    metadata={
                        'customer_id': 'cust-7',
                        'langfuse_user_id': 'metadata-user',
                    },
                ),
                call_context=SimpleNamespace(
                    user=SimpleNamespace(
                        is_authenticated=True,
                        user_name='auth-user',
                    )
                ),
                tenant='tenant-a',
            )

            request = executor._build_langfuse_request(
                context,
                'Inspect this account',
                task_id='task-1',
                context_id='ctx-1',
            )

        self.assertEqual(
            request.trace_id,
            '0123456789abcdef0123456789abcdef',
        )
        self.assertEqual(request.session_id, 'ctx-1')
        self.assertEqual(request.user_id, 'auth-user')
        self.assertEqual(request.trace_name, 'Custom request trace')
        self.assertIn('priority', request.tags)
        self.assertEqual(request.trace_metadata['a2a_task_id'], 'task-1')
        self.assertEqual(
            request.observation_metadata['message_metadata']['customer_id'],
            'cust-7',
        )
        self.assertEqual(
            request.langchain_metadata['a2a_message_id'],
            'msg-1',
        )
        self.assertEqual(
            request.trace_metadata['agent_settings'],
            'Analyst agent',
        )

    def test_build_langfuse_request_reads_agent_settings_from_runtime_env(self) -> None:
        executor = AnalysisAgentExecutor()
        executor.agent.create_langfuse_trace_id = lambda seed: None

        context = SimpleNamespace(
            metadata={},
            message=SimpleNamespace(message_id='msg-1', metadata={}),
            call_context=SimpleNamespace(user=None),
            tenant='tenant-a',
        )

        with patch.dict(os.environ, {'AGENT_SETTINGS': 'Analyst Workstation'}):
            request = executor._build_langfuse_request(
                context,
                'Inspect this account',
                task_id='task-1',
                context_id='ctx-1',
            )

        self.assertEqual(
            request.trace_metadata['agent_settings'],
            'Analyst Workstation',
        )

    def test_build_langfuse_request_prefers_explicit_session_id(self) -> None:
        executor = AnalysisAgentExecutor()
        executor.agent.create_langfuse_trace_id = lambda seed: None

        context = SimpleNamespace(
            metadata={'langfuse_session_id': 'session-42'},
            message=SimpleNamespace(message_id='msg-1', metadata={}),
            call_context=SimpleNamespace(user=None),
            tenant='tenant-a',
        )

        request = executor._build_langfuse_request(
            context,
            'Inspect this account',
            task_id='task-1',
            context_id='ctx-1',
        )

        self.assertEqual(request.session_id, 'session-42')

    def test_request_trace_ignores_invalid_explicit_trace_id(self) -> None:
        class FakeSpan:
            def __init__(self, **start_kwargs: Any) -> None:
                self.start_kwargs = start_kwargs
                self.trace_id = 'fedcba9876543210fedcba9876543210'
                self.id = '0123456789abcdef'

            def update(self, **kwargs: Any) -> None:
                return None

            def set_trace_io(self, **kwargs: Any) -> None:
                return None

            def end(self) -> None:
                return None

        class FakeLangfuseClient:
            def __init__(self) -> None:
                self.spans: list[FakeSpan] = []

            def start_observation(self, **kwargs: Any) -> FakeSpan:
                span = FakeSpan(**kwargs)
                self.spans.append(span)
                return span

        @contextmanager
        def fake_propagate_attributes(**kwargs: Any):
            yield

        agent = AnalysisAgent()
        agent._langfuse_initialized = True
        agent.langfuse_enabled = True
        agent.langfuse = FakeLangfuseClient()
        agent._langfuse_propagate_attributes = fake_propagate_attributes

        root_span, handler = agent._request_trace(
            LangfuseRequest(
                input_text='hello',
                session_id='ctx-1',
                trace_id='not-a-valid-trace-id',
            )
        )

        self.assertIsNotNone(root_span)
        self.assertIsNone(handler)
        self.assertIsNone(agent.langfuse.spans[0].start_kwargs['trace_context'])

    def test_build_agent_prompt_uses_langfuse_prompt_metadata(self) -> None:
        agent = AnalysisAgent()
        langfuse_prompt = SimpleNamespace(
            name='Analyst agent',
            version=11,
            get_langchain_prompt=lambda: 'Use careful banking language.',
        )
        agent._langfuse_prompt = langfuse_prompt

        prompt = agent._build_agent_prompt('Fallback prompt')

        self.assertIsInstance(prompt, ChatPromptTemplate)
        self.assertEqual(prompt.metadata['langfuse_prompt'], langfuse_prompt)
        rendered_prompt = prompt.invoke({'messages': [('user', 'hello')]})
        self.assertEqual(
            rendered_prompt.messages[0].content,
            'Use careful banking language.',
        )
        self.assertEqual(rendered_prompt.messages[1].content, 'hello')

    def test_build_graph_config_sets_trace_attrs_without_prompt_object(self) -> None:
        agent = AnalysisAgent()
        config = agent._build_graph_config(
            'ctx-1',
            langfuse_request=LangfuseRequest(
                input_text='hello',
                session_id='ctx-1',
                trace_name='Custom trace',
                user_id='user-1',
                tags=['a2a', 'priority'],
                langchain_metadata={'a2a_task_id': 'task-1'},
            ),
        )

        self.assertEqual(config['run_name'], 'Custom trace')
        self.assertEqual(config['metadata']['langfuse_session_id'], 'ctx-1')
        self.assertEqual(config['metadata']['langfuse_user_id'], 'user-1')
        self.assertEqual(config['metadata']['a2a_task_id'], 'task-1')
        self.assertNotIn('langfuse_prompt', config['metadata'])

    def test_load_runtime_config_reads_agent_settings_from_runtime_env(self) -> None:
        class FakeLangfuseClient:
            def __init__(self) -> None:
                self.prompt_calls: list[tuple[str, str]] = []

            def get_prompt(self, name: str, *, label: str):
                self.prompt_calls.append((name, label))
                return SimpleNamespace(
                    prompt='Use careful banking language.',
                    config={
                        'agent_card': {
                            'name': 'System research Agent',
                        }
                    },
                )

        agent = AnalysisAgent()
        agent._langfuse_initialized = True
        agent.langfuse_enabled = True
        agent.langfuse = FakeLangfuseClient()

        with patch.dict(os.environ, {'AGENT_SETTINGS': 'Analyst Workstation'}):
            runtime_config = agent._load_runtime_config()

        self.assertEqual(
            agent.langfuse.prompt_calls,
            [('Analyst Workstation', 'production')],
        )
        self.assertEqual(
            runtime_config.config.agent_card.name,
            'System research Agent',
        )

    async def test_analysis_agent_stream_updates_langfuse_request_span(self) -> None:
        class FakeHandler:
            def __init__(
                self,
                *,
                trace_context: dict[str, str] | None = None,
            ) -> None:
                self.trace_context = trace_context

        class FakeSpan:
            def __init__(self, **start_kwargs: Any) -> None:
                self.start_kwargs = start_kwargs
                trace_context = dict(start_kwargs.get('trace_context') or {})
                self.trace_id = trace_context.get(
                    'trace_id',
                    'fedcba9876543210fedcba9876543210',
                )
                self.id = '0123456789abcdef'
                self.updates: list[dict[str, Any]] = []
                self.trace_io_updates: list[dict[str, Any]] = []
                self.end_calls = 0

            def update(self, **kwargs: Any) -> None:
                self.updates.append(kwargs)

            def set_trace_io(self, **kwargs: Any) -> None:
                self.trace_io_updates.append(kwargs)

            def end(self) -> None:
                self.end_calls += 1

        class FakeLangfuseClient:
            def __init__(self) -> None:
                self.spans: list[FakeSpan] = []

            def start_observation(self, **kwargs: Any) -> FakeSpan:
                span = FakeSpan(**kwargs)
                self.spans.append(span)
                return span

        propagation_calls: list[dict[str, Any]] = []

        @contextmanager
        def fake_propagate_attributes(**kwargs: Any):
            propagation_calls.append(kwargs)
            yield

        class FakeGraph:
            async def astream(
                self,
                inputs: dict[str, Any],
                config: dict[str, Any],
                stream_mode: list[str],
                version: str,
            ):
                self.inputs = inputs
                self.config = config
                self.stream_mode = stream_mode
                self.version = version
                yield {
                    'type': 'updates',
                    'data': {
                        'agent': {
                            'messages': [AIMessage(content='Final answer draft')]
                        }
                    },
                }

            async def aget_state(self, config: dict[str, Any]):
                return SimpleNamespace(
                    values={
                        'messages': [AIMessage(content='Final answer draft')],
                        'structured_response': ResponseFormat(
                            status='completed',
                            message='Final answer draft',
                        ),
                    }
                )

        agent = AnalysisAgent()
        agent.graph = FakeGraph()
        agent._langfuse_initialized = True
        agent.langfuse_enabled = True
        agent.langfuse = FakeLangfuseClient()
        agent._langfuse_callback_handler_cls = FakeHandler
        agent._langfuse_propagate_attributes = fake_propagate_attributes
        agent._langfuse_prompt = SimpleNamespace(name='Analyst agent', version=11)

        request = LangfuseRequest(
            input_text='How big is the context?',
            session_id='ctx-1',
            trace_id='0123456789abcdef0123456789abcdef',
            user_id='user-123',
            tags=['a2a', 'langgraph', 'priority'],
            trace_metadata={'a2a_task_id': 'task-1'},
            observation_metadata={'a2a_task_id': 'task-1'},
            langchain_metadata={'a2a_task_id': 'task-1'},
        )

        items = []
        async for item in agent.stream(
            'How big is the context?',
            'ctx-1',
            langfuse_request=request,
        ):
            items.append(item)

        self.assertEqual(items[-1]['content'], 'Final answer draft')
        self.assertEqual(len(agent.langfuse.spans), 1)
        root_span = agent.langfuse.spans[0]
        self.assertEqual(root_span.start_kwargs['input'], 'How big is the context?')
        self.assertEqual(
            root_span.start_kwargs['trace_context'],
            {'trace_id': '0123456789abcdef0123456789abcdef'},
        )
        self.assertEqual(propagation_calls[0]['session_id'], 'ctx-1')
        self.assertEqual(propagation_calls[0]['user_id'], 'user-123')
        self.assertIn('priority', propagation_calls[0]['tags'])
        self.assertEqual(
            agent.graph.config['metadata']['langfuse_session_id'],
            'ctx-1',
        )
        self.assertEqual(
            agent.graph.config['metadata']['langfuse_user_id'],
            'user-123',
        )
        self.assertEqual(
            agent.graph.config['metadata']['a2a_task_id'],
            'task-1',
        )
        self.assertEqual(agent.graph.config['run_name'], 'Deep Research Agent request')
        handler = agent.graph.config['callbacks'][0]
        self.assertIsInstance(handler, FakeHandler)
        self.assertEqual(
            handler.trace_context,
            {
                'trace_id': '0123456789abcdef0123456789abcdef',
                'parent_span_id': '0123456789abcdef',
            },
        )
        self.assertEqual(
            root_span.trace_io_updates[0]['input'],
            'How big is the context?',
        )
        self.assertEqual(
            root_span.trace_io_updates[-1]['output'],
            'Final answer draft',
        )
        self.assertEqual(root_span.updates[-1]['output'], 'Final answer draft')
        self.assertEqual(
            root_span.updates[-1]['metadata']['task_state'],
            'completed',
        )
        self.assertEqual(root_span.end_calls, 1)


if __name__ == '__main__':
    unittest.main(verbosity=2)
