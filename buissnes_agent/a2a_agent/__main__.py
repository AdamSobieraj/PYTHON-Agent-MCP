import asyncio
import contextlib
import logging
import os
import sys

from contextlib import asynccontextmanager
from datetime import datetime, timezone
from typing import Any

import click
import grpc
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, StreamingResponse
from dotenv import load_dotenv
from google.protobuf.json_format import MessageToDict

try:
    from . import patch_a2a_sdk  # noqa: F401
except ImportError:
    from buissnes_agent.a2a_agent import patch_a2a_sdk  # type: ignore  # noqa: F401

from a2a.compat.v0_3 import a2a_v0_3_pb2_grpc
from a2a.compat.v0_3.grpc_handler import CompatGrpcHandler
from a2a.server.request_handlers import DefaultRequestHandler, GrpcHandler
from a2a.server.request_handlers.response_helpers import agent_card_to_dict
from a2a.server.routes import create_jsonrpc_routes, create_rest_routes
from a2a.server.routes.common import DefaultServerCallContextBuilder
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentInterface,
    AgentProvider,
    AgentSkill,
    GetTaskRequest,
    ListTasksRequest,
    a2a_pb2_grpc,
)
from a2a.utils.constants import AGENT_CARD_WELL_KNOWN_PATH
from a2a.utils.proto_utils import parse_params

try:
    from .ag_ui import (
        AG_UI_MEDIA_TYPE,
        AG_UI_NDJSON_MEDIA_TYPE,
        EventEncoder,
        RunAgentInput,
        get_last_user_text,
    )
    from .agent import AnalysisAgent
    from .agent_executor import AnalysisAgentExecutor
    from .mcp_config import AgentRuntimeConfig
except ImportError:
    from buissnes_agent.a2a_agent.ag_ui import (  # type: ignore
        AG_UI_MEDIA_TYPE,
        AG_UI_NDJSON_MEDIA_TYPE,
        EventEncoder,
        RunAgentInput,
        get_last_user_text,
    )
    from buissnes_agent.a2a_agent.agent import AnalysisAgent  # type: ignore
    from buissnes_agent.a2a_agent.agent_executor import AnalysisAgentExecutor  # type: ignore
    from buissnes_agent.a2a_agent.mcp_config import (  # type: ignore
        AgentRuntimeConfig,
    )


load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


DEFAULT_AGENT_CARD_NAME = 'Deep Research Agent'
DEFAULT_AGENT_CARD_DESCRIPTION = (
    'Helps with deep research and system analysis.'
)
DEFAULT_AGENT_CARD_VERSION = '1.0.0'
DEFAULT_AGENT_CARD_PROVIDER_ORG = 'Business Agent'
DEFAULT_AGENT_CARD_OUTPUT_MODES = ['text', 'task-status']
DEFAULT_AGENT_CARD_SKILL = {
    'id': 'system_analysis',
    'name': 'System Analysis Tool',
    'description': 'Helps with system analysis and research tasks.',
    'tags': ['system-analysis', 'research'],
    'examples': ['What is system analysis?'],
}


class MissingConfigurationError(Exception):
    """Exception for missing required runtime configuration."""


def _resolve_public_host(bind_host: str) -> str:
    configured_host = os.getenv('A2A_AGENT_HOST')
    if configured_host:
        return configured_host

    if bind_host in {'0.0.0.0', '::'}:
        return '127.0.0.1'

    return bind_host


def _validate_ports(
    http_port: int,
    grpc_port: int,
    compat_grpc_port: int,
) -> None:
    ports = [port for port in (http_port, grpc_port, compat_grpc_port) if port]
    if any(port < 0 for port in ports):
        raise ValueError('Ports must be zero or positive integers.')
    if len(ports) != len(set(ports)):
        raise ValueError(
            'HTTP, gRPC, and compatibility gRPC ports must be distinct.'
        )


def _build_supported_interfaces(
    public_host: str,
    http_port: int,
    grpc_port: int,
    compat_grpc_port: int,
) -> list[AgentInterface]:
    http_base_url = f'http://{public_host}:{http_port}'
    supported_interfaces = [
        AgentInterface(
            protocol_binding='JSONRPC',
            protocol_version='1.0',
            url=f'{http_base_url}/a2a/jsonrpc',
        ),
        AgentInterface(
            protocol_binding='HTTP+JSON',
            protocol_version='1.0',
            url=f'{http_base_url}/a2a/rest',
        ),
    ]

    if grpc_port:
        supported_interfaces.append(
            AgentInterface(
                protocol_binding='GRPC',
                protocol_version='1.0',
                url=f'{public_host}:{grpc_port}',
            )
        )

    supported_interfaces.extend(
        [
            AgentInterface(
                protocol_binding='JSONRPC',
                protocol_version='0.3',
                url=f'{http_base_url}/a2a/jsonrpc',
            ),
            AgentInterface(
                protocol_binding='HTTP+JSON',
                protocol_version='0.3',
                url=f'{http_base_url}/a2a/rest',
            ),
        ]
    )

    if compat_grpc_port:
        supported_interfaces.append(
            AgentInterface(
                protocol_binding='GRPC',
                protocol_version='0.3',
                url=f'{public_host}:{compat_grpc_port}',
            )
        )

    return supported_interfaces


def _build_agent_card(
    public_host: str,
    http_port: int,
    grpc_port: int,
    compat_grpc_port: int,
    runtime_config: AgentRuntimeConfig | None = None,
) -> AgentCard:
    agent_card_config = None
    if runtime_config is not None:
        agent_card_config = runtime_config.config.agent_card

    http_base_url = f'http://{public_host}:{http_port}'
    input_modes = list(
        (
            agent_card_config.default_input_modes
            if agent_card_config
            and agent_card_config.default_input_modes
            else AnalysisAgent.SUPPORTED_CONTENT_TYPES
        )
    )
    output_modes = list(
        (
            agent_card_config.default_output_modes
            if agent_card_config
            and agent_card_config.default_output_modes
            else DEFAULT_AGENT_CARD_OUTPUT_MODES
        )
    )

    capabilities_kwargs = {
        'streaming': True,
        'push_notifications': False,
    }
    if agent_card_config and agent_card_config.capabilities:
        if agent_card_config.capabilities.streaming is not None:
            capabilities_kwargs['streaming'] = (
                agent_card_config.capabilities.streaming
            )
        if agent_card_config.capabilities.push_notifications is not None:
            capabilities_kwargs['push_notifications'] = (
                agent_card_config.capabilities.push_notifications
            )
        if agent_card_config.capabilities.extended_agent_card is not None:
            capabilities_kwargs['extended_agent_card'] = (
                agent_card_config.capabilities.extended_agent_card
            )
    capabilities = AgentCapabilities(**capabilities_kwargs)

    if agent_card_config and agent_card_config.skills:
        skills = [
            AgentSkill(
                id=skill.id,
                name=skill.name,
                description=skill.description,
                tags=list(skill.tags),
                examples=list(skill.examples or []),
                input_modes=list(skill.input_modes or input_modes),
                output_modes=list(skill.output_modes or output_modes),
            )
            for skill in agent_card_config.skills
        ]
    else:
        skills = [
            AgentSkill(
                id=DEFAULT_AGENT_CARD_SKILL['id'],
                name=DEFAULT_AGENT_CARD_SKILL['name'],
                description=DEFAULT_AGENT_CARD_SKILL['description'],
                tags=list(DEFAULT_AGENT_CARD_SKILL['tags']),
                examples=list(DEFAULT_AGENT_CARD_SKILL['examples']),
                input_modes=input_modes,
                output_modes=output_modes,
            )
        ]

    provider_config = agent_card_config.provider if agent_card_config else None
    provider = AgentProvider(
        organization=(
            provider_config.organization
            if provider_config and provider_config.organization
            else DEFAULT_AGENT_CARD_PROVIDER_ORG
        ),
        url=(
            provider_config.url
            if provider_config and provider_config.url
            else http_base_url
        ),
    )

    agent_card_kwargs = {
        'name': (
            agent_card_config.name
            if agent_card_config and agent_card_config.name
            else DEFAULT_AGENT_CARD_NAME
        ),
        'description': (
            agent_card_config.description
            if agent_card_config and agent_card_config.description
            else DEFAULT_AGENT_CARD_DESCRIPTION
        ),
        'provider': provider,
        'version': (
            agent_card_config.version
            if agent_card_config and agent_card_config.version
            else DEFAULT_AGENT_CARD_VERSION
        ),
        'default_input_modes': input_modes,
        'default_output_modes': output_modes,
        'capabilities': capabilities,
        'skills': skills,
        'supported_interfaces': _build_supported_interfaces(
            public_host=public_host,
            http_port=http_port,
            grpc_port=grpc_port,
            compat_grpc_port=compat_grpc_port,
        ),
    }
    if (
        agent_card_config
        and agent_card_config.documentation_url
    ):
        agent_card_kwargs['documentation_url'] = (
            agent_card_config.documentation_url
        )
    if agent_card_config and agent_card_config.icon_url:
        agent_card_kwargs['icon_url'] = agent_card_config.icon_url

    return AgentCard(**agent_card_kwargs)


def _apply_runtime_config_to_agent_card(
    agent_card: AgentCard,
    runtime_config: AgentRuntimeConfig,
    *,
    public_host: str,
    http_port: int,
    grpc_port: int,
    compat_grpc_port: int,
) -> None:
    updated_agent_card = _build_agent_card(
        public_host=public_host,
        http_port=http_port,
        grpc_port=grpc_port,
        compat_grpc_port=compat_grpc_port,
        runtime_config=runtime_config,
    )
    agent_card.CopyFrom(updated_agent_card)


def _build_request_handler(
    agent_card: AgentCard,
    agent_executor: AnalysisAgentExecutor | None = None,
) -> DefaultRequestHandler:
    if agent_executor is None:
        agent_executor = AnalysisAgentExecutor()

    return DefaultRequestHandler(
        agent_executor=agent_executor,
        task_store=InMemoryTaskStore(),
        agent_card=agent_card,
    )


def _build_call_context(request: Request):
    context_builder = DefaultServerCallContextBuilder()
    context = context_builder.build(request)
    if 'tenant' in request.path_params:
        context.tenant = request.path_params['tenant']
    return context


def _add_documented_rest_get_routes(
    app: FastAPI,
    request_handler: DefaultRequestHandler,
    path_prefix: str,
) -> None:
    rest_tag = 'A2A REST'

    @app.get(
        f'{path_prefix}/tasks',
        tags=[rest_tag],
        summary='List A2A tasks',
        description='REST GET endpoint for listing tasks. Query parameters follow the A2A specification.',
    )
    async def rest_list_tasks(request: Request) -> JSONResponse:
        context = _build_call_context(request)
        params = ListTasksRequest()
        parse_params(request.query_params, params)
        result = await request_handler.on_list_tasks(params, context)
        return JSONResponse(
            content=MessageToDict(
                result,
                preserving_proto_field_name=False,
                always_print_fields_with_no_presence=True,
            )
        )

    @app.get(
        f'{path_prefix}/tasks/{{id}}',
        tags=[rest_tag],
        summary='Get A2A task',
        description='REST GET endpoint for fetching a task by id.',
    )
    async def rest_get_task(id: str, request: Request) -> JSONResponse:
        context = _build_call_context(request)
        params = GetTaskRequest(id=id)
        parse_params(request.query_params, params)
        task = await request_handler.on_get_task(params, context)
        if not task:
            raise HTTPException(status_code=404, detail='Task not found')
        return JSONResponse(
            content=MessageToDict(task, preserving_proto_field_name=False)
        )


def _build_app(
    agent_card: AgentCard,
    request_handler: DefaultRequestHandler,
    agent_executor: AnalysisAgentExecutor,
) -> FastAPI:
    @asynccontextmanager
    async def lifespan(_app: FastAPI):
        await agent_executor.startup()
        try:
            yield
        finally:
            await agent_executor.shutdown()

    app = FastAPI(
        title=agent_card.name,
        description=agent_card.description,
        version=agent_card.version,
        lifespan=lifespan,
    )

    @app.get(
        '/',
        include_in_schema=False,
    )
    async def root() -> dict[str, str]:
        return {
            'name': agent_card.name,
            'postPath': '/',
            'catalog': '/catalog',
            'agent_card': AGENT_CARD_WELL_KNOWN_PATH,
            'jsonrpc': '/a2a/jsonrpc',
            'rest': '/a2a/rest',
            'ag_ui': '/ag-ui',
            'docs': '/docs',
        }

    async def _stream_ag_ui_response(
        input_data: RunAgentInput,
        request: Request,
    ) -> StreamingResponse:
        if not input_data.messages:
            raise HTTPException(
                status_code=400,
                detail='AG-UI requests require at least one message.',
            )

        if not get_last_user_text(input_data.messages):
            raise HTTPException(
                status_code=400,
                detail='AG-UI requests require a user text message.',
            )

        encoder = EventEncoder(accept=request.headers.get('accept'))

        async def event_generator():
            async for event in agent_executor.agent.stream_ag_ui(input_data):
                yield encoder.encode(event)

        return StreamingResponse(
            event_generator(),
            media_type=encoder.get_content_type(),
            headers={
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'X-Accel-Buffering': 'no',
            },
        )

    @app.get(
        AGENT_CARD_WELL_KNOWN_PATH,
        tags=['A2A Discovery'],
        summary='Get agent card',
        description='Returns the published agent card for discovery.',
    )
    async def get_agent_card() -> JSONResponse:
        return JSONResponse(agent_card_to_dict(agent_card))

    @app.get(
        '/catalog',
        tags=['AG-UI'],
        summary='Get a lightweight runtime catalog',
        description='Returns a simple catalog snapshot compatible with the local AG-UI playground.',
    )
    async def get_catalog() -> dict[str, Any]:
        return {
            'loadedAt': datetime.now(timezone.utc).isoformat(),
            'configPath': 'default_config.json',
            'a2aAgents': [
                {
                    'name': agent_card.name,
                    'displayName': agent_card.name,
                    'description': agent_card.description,
                    'endpointUrl': '/a2a/jsonrpc',
                    'protocolBinding': 'JSONRPC',
                    'skills': [skill.name for skill in agent_card.skills],
                }
            ],
            'mcpTools': [
                {
                    'serverName': 'agent-runtime',
                    'toolName': tool.name,
                    'description': tool.description or '',
                }
                for tool in agent_executor.agent.tools
            ],
            'warnings': [],
        }

    @app.get('/catalog/', include_in_schema=False)
    async def get_catalog_alias() -> dict[str, Any]:
        return await get_catalog()

    @app.get(
        '/ag-ui',
        tags=['AG-UI'],
        summary='Describe the AG-UI endpoint',
        description='Returns transport details for the AG-UI-compatible UI streaming endpoint.',
    )
    async def ag_ui_info() -> dict[str, Any]:
        return {
            'name': agent_card.name,
            'description': agent_card.description,
            'endpoint': '/ag-ui',
            'method': 'POST',
            'content_type': AG_UI_MEDIA_TYPE,
            'supported_content_types': [
                AG_UI_MEDIA_TYPE,
                AG_UI_NDJSON_MEDIA_TYPE,
            ],
            'content_negotiation': {
                'request_header': 'Accept',
                'default': AG_UI_MEDIA_TYPE,
                'selection': (
                    'Returns application/x-ndjson when the Accept header '
                    'requests JSON without text/event-stream; otherwise '
                    'streams text/event-stream.'
                ),
            },
            'threading': 'stateless-per-run',
        }

    @app.get('/agui', include_in_schema=False)
    async def ag_ui_info_alias() -> dict[str, Any]:
        return await ag_ui_info()

    @app.post(
        '/ag-ui',
        tags=['AG-UI'],
        summary='Run the agent over AG-UI',
        description='Accepts AG-UI RunAgentInput payloads and streams AG-UI events with accept-aware encoding.',
    )
    async def run_ag_ui(
        input_data: RunAgentInput,
        request: Request,
    ) -> StreamingResponse:
        return await _stream_ag_ui_response(input_data, request)

    @app.post('/agui', include_in_schema=False)
    async def run_ag_ui_alias(
        input_data: RunAgentInput,
        request: Request,
    ) -> StreamingResponse:
        return await _stream_ag_ui_response(input_data, request)

    @app.post('/', include_in_schema=False)
    async def run_ag_ui_root(
        input_data: RunAgentInput,
        request: Request,
    ) -> StreamingResponse:
        return await _stream_ag_ui_response(input_data, request)

    _add_documented_rest_get_routes(
        app=app,
        request_handler=request_handler,
        path_prefix='/a2a/rest',
    )

    app.routes.extend(
        create_jsonrpc_routes(
            request_handler=request_handler,
            rpc_url='/a2a/jsonrpc',
            enable_v0_3_compat=True,
        )
    )
    app.routes.extend(
        create_rest_routes(
            request_handler=request_handler,
            path_prefix='/a2a/rest',
            enable_v0_3_compat=True,
        )
    )

    return app


async def _build_grpc_server(
    request_handler: DefaultRequestHandler,
    bind_host: str,
    port: int,
    *,
    compat: bool = False,
) -> tuple[grpc.aio.Server, int]:
    server = grpc.aio.server()
    try:
        bound_port = server.add_insecure_port(f'{bind_host}:{port}')
        if bound_port == 0:
            raise RuntimeError(
                f'Unable to bind {"compatibility " if compat else ""}gRPC server to {bind_host}:{port}.'
            )

        if compat:
            compat_servicer = CompatGrpcHandler(request_handler)
            a2a_v0_3_pb2_grpc.add_A2AServiceServicer_to_server(
                compat_servicer,
                server,
            )
        else:
            servicer = GrpcHandler(request_handler)
            a2a_pb2_grpc.add_A2AServiceServicer_to_server(servicer, server)

        return server, bound_port
    except Exception:
        with contextlib.suppress(Exception):
            await server.stop(0)
        raise


async def serve(
    host: str,
    http_port: int,
    grpc_port: int,
    compat_grpc_port: int,
) -> None:
    _validate_ports(http_port, grpc_port, compat_grpc_port)

    public_host = _resolve_public_host(host)
    agent_executor = AnalysisAgentExecutor()
    runtime_config = agent_executor.agent.load_runtime_config_snapshot()
    agent_card = _build_agent_card(
        public_host=public_host,
        http_port=http_port,
        grpc_port=grpc_port,
        compat_grpc_port=compat_grpc_port,
        runtime_config=runtime_config,
    )
    agent_executor.agent.register_runtime_config_listener(
        lambda updated_runtime_config: _apply_runtime_config_to_agent_card(
            agent_card,
            updated_runtime_config,
            public_host=public_host,
            http_port=http_port,
            grpc_port=grpc_port,
            compat_grpc_port=compat_grpc_port,
        )
    )
    request_handler = _build_request_handler(agent_card, agent_executor)
    app = _build_app(agent_card, request_handler, agent_executor)

    grpc_server = None
    compat_grpc_server = None

    try:
        if grpc_port:
            grpc_server, grpc_port = await _build_grpc_server(
                request_handler=request_handler,
                bind_host=host,
                port=grpc_port,
                compat=False,
            )
            await grpc_server.start()

        if compat_grpc_port:
            compat_grpc_server, compat_grpc_port = await _build_grpc_server(
                request_handler=request_handler,
                bind_host=host,
                port=compat_grpc_port,
                compat=True,
            )
            await compat_grpc_server.start()

        logger.info('Starting %s', agent_card.name)
        logger.info(' - Agent card: http://%s:%s%s', public_host, http_port, AGENT_CARD_WELL_KNOWN_PATH)
        logger.info(' - JSON-RPC:   http://%s:%s/a2a/jsonrpc', public_host, http_port)
        logger.info(' - REST:       http://%s:%s/a2a/rest', public_host, http_port)
        logger.info(' - Swagger UI: http://%s:%s/docs', public_host, http_port)
        if grpc_port:
            logger.info(' - gRPC 1.0:   %s:%s', public_host, grpc_port)
        if compat_grpc_port:
            logger.info(' - gRPC 0.3:   %s:%s', public_host, compat_grpc_port)

        uvicorn_server = uvicorn.Server(
            uvicorn.Config(app, host=host, port=http_port)
        )
        await uvicorn_server.serve()
    finally:
        if grpc_server is not None:
            await grpc_server.stop(0)
        if compat_grpc_server is not None:
            await compat_grpc_server.stop(0)


@click.command()
@click.option('--host', 'host', default='localhost', show_default=True)
@click.option('--port', 'http_port', default=10000, show_default=True)
@click.option('--grpc-port', 'grpc_port', default=10001, show_default=True)
@click.option(
    '--compat-grpc-port',
    'compat_grpc_port',
    default=10002,
    show_default=True,
)
def main(
    host: str,
    http_port: int,
    grpc_port: int,
    compat_grpc_port: int,
) -> None:
    """Starts the Deep Research Agent server."""
    try:
        if not os.getenv('CHAT_BASE_URL'):
            raise MissingConfigurationError(
                'CHAT_BASE_URL environment variable not set.'
            )
        if not os.getenv('CHAT_MODEL'):
            raise MissingConfigurationError(
                'CHAT_MODEL environment variable not set.'
            )

        asyncio.run(
            serve(
                host=host,
                http_port=http_port,
                grpc_port=grpc_port,
                compat_grpc_port=compat_grpc_port,
            )
        )
    except MissingConfigurationError as exc:
        logger.error('Error: %s', exc)
        sys.exit(1)
    except Exception:
        logger.exception('An error occurred during server startup')
        sys.exit(1)


if __name__ == '__main__':
    main()
