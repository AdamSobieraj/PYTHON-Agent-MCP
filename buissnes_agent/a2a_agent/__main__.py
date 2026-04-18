import asyncio
import logging
import os
import sys

from contextlib import asynccontextmanager

import click
import grpc
import uvicorn
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from google.protobuf.json_format import MessageToDict

try:
    from . import patch_a2a_sdk  # noqa: F401
except ImportError:
    import patch_a2a_sdk  # type: ignore  # noqa: F401

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
    from .agent import AnalysisAgent
    from .agent_executor import AnalysisAgentExecutor
except ImportError:
    from agent import AnalysisAgent  # type: ignore
    from agent_executor import AnalysisAgentExecutor  # type: ignore


load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
) -> AgentCard:
    http_base_url = f'http://{public_host}:{http_port}'
    input_modes = AnalysisAgent.SUPPORTED_CONTENT_TYPES
    output_modes = ['text', 'task-status']

    capabilities = AgentCapabilities(streaming=True, push_notifications=False)
    skill = AgentSkill(
        id='system_analysis',
        name='System Analysis Tool',
        description='Helps with system analysis and research tasks.',
        tags=['system-analysis', 'research'],
        examples=['What is system analysis?'],
        input_modes=input_modes,
        output_modes=output_modes,
    )

    return AgentCard(
        name='Deep Research Agent',
        description='Helps with deep research and system analysis.',
        provider=AgentProvider(
            organization='Business Agent',
            url=http_base_url,
        ),
        version='1.0.0',
        default_input_modes=input_modes,
        default_output_modes=output_modes,
        capabilities=capabilities,
        skills=[skill],
        supported_interfaces=_build_supported_interfaces(
            public_host=public_host,
            http_port=http_port,
            grpc_port=grpc_port,
            compat_grpc_port=compat_grpc_port,
        ),
    )


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
        title='Deep Research Agent',
        description='A2A server exposing JSON-RPC, HTTP+JSON REST, and gRPC transports.',
        version='1.0.0',
        lifespan=lifespan,
    )

    @app.get(
        '/',
        include_in_schema=False,
    )
    async def root() -> dict[str, str]:
        return {
            'name': agent_card.name,
            'agent_card': AGENT_CARD_WELL_KNOWN_PATH,
            'jsonrpc': '/a2a/jsonrpc',
            'rest': '/a2a/rest',
            'docs': '/docs',
        }

    @app.get(
        AGENT_CARD_WELL_KNOWN_PATH,
        tags=['A2A Discovery'],
        summary='Get agent card',
        description='Returns the published agent card for discovery.',
    )
    async def get_agent_card() -> JSONResponse:
        return JSONResponse(agent_card_to_dict(agent_card))

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


def _build_grpc_server(
    request_handler: DefaultRequestHandler,
    bind_host: str,
    port: int,
    *,
    compat: bool = False,
) -> tuple[grpc.aio.Server, int]:
    server = grpc.aio.server()
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


async def serve(
    host: str,
    http_port: int,
    grpc_port: int,
    compat_grpc_port: int,
) -> None:
    _validate_ports(http_port, grpc_port, compat_grpc_port)

    public_host = _resolve_public_host(host)
    agent_card = _build_agent_card(
        public_host=public_host,
        http_port=http_port,
        grpc_port=grpc_port,
        compat_grpc_port=compat_grpc_port,
    )
    agent_executor = AnalysisAgentExecutor()
    request_handler = _build_request_handler(agent_card, agent_executor)
    app = _build_app(agent_card, request_handler, agent_executor)

    grpc_server = None
    compat_grpc_server = None

    if grpc_port:
        grpc_server, grpc_port = _build_grpc_server(
            request_handler=request_handler,
            bind_host=host,
            port=grpc_port,
            compat=False,
        )
        await grpc_server.start()

    if compat_grpc_port:
        compat_grpc_server, compat_grpc_port = _build_grpc_server(
            request_handler=request_handler,
            bind_host=host,
            port=compat_grpc_port,
            compat=True,
        )
        await compat_grpc_server.start()

    logger.info('Starting Deep Research Agent')
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

    try:
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
