import logging
import os
import sys

import click
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv

try:
    from . import patch_a2a_sdk  # noqa: F401
except ImportError:
    import patch_a2a_sdk  # type: ignore  # noqa: F401

from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.routes import (
    create_agent_card_routes,
    create_jsonrpc_routes,
    create_rest_routes,
)
from a2a.server.tasks import (
    InMemoryTaskStore,
)
from a2a.types import (
    AgentCapabilities,
    AgentCard,
    AgentInterface,
    AgentProvider,
    AgentSkill,
)

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


def _build_agent_card(public_host: str, port: int) -> AgentCard:
    base_url = f'http://{public_host}:{port}'
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
            url=base_url,
        ),
        version='1.0.0',
        default_input_modes=input_modes,
        default_output_modes=output_modes,
        capabilities=capabilities,
        skills=[skill],
        supported_interfaces=[
            AgentInterface(
                protocol_binding='JSONRPC',
                protocol_version='1.0',
                url=f'{base_url}/',
            ),
            AgentInterface(
                protocol_binding='JSONRPC',
                protocol_version='0.3',
                url=f'{base_url}/',
            ),
            AgentInterface(
                protocol_binding='HTTP+JSON',
                protocol_version='1.0',
                url=base_url,
            ),
            AgentInterface(
                protocol_binding='HTTP+JSON',
                protocol_version='0.3',
                url=base_url,
            ),
        ],
    )


def _build_app(agent_card: AgentCard) -> FastAPI:
    request_handler = DefaultRequestHandler(
        agent_executor=AnalysisAgentExecutor(),
        task_store=InMemoryTaskStore(),
        agent_card=agent_card,
    )

    app = FastAPI()
    app.routes.extend(create_agent_card_routes(agent_card=agent_card))
    app.routes.extend(
        create_jsonrpc_routes(
            request_handler=request_handler,
            rpc_url='/',
            enable_v0_3_compat=True,
        )
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


@click.command()
@click.option('--host', 'host', default='localhost')
@click.option('--port', 'port', default=10000)
def main(host: str, port: int) -> None:
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

        public_host = _resolve_public_host(host)
        agent_card = _build_agent_card(public_host, port)
        app = _build_app(agent_card)

        logger.info(
            'Starting Deep Research Agent on http://%s:%s', host, port
        )
        logger.info(
            'Agent card available at http://%s:%s/.well-known/agent-card.json',
            public_host,
            port,
        )

        uvicorn.run(app, host=host, port=port)
    except MissingConfigurationError as exc:
        logger.error('Error: %s', exc)
        sys.exit(1)
    except Exception:
        logger.exception('An error occurred during server startup')
        sys.exit(1)


if __name__ == '__main__':
    main()
