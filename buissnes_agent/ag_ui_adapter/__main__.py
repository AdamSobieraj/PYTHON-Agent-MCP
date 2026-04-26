import logging
import os
import sys

import click
import uvicorn

from .service import A2ATarget, create_app, default_target_from_env


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.command()
@click.option('--host', default='127.0.0.1', show_default=True)
@click.option('--port', default=10100, show_default=True)
@click.option('--a2a-url', default=None)
@click.option('--a2a-transport', default=None)
def main(
    host: str,
    port: int,
    a2a_url: str | None,
    a2a_transport: str | None,
) -> None:
    """Starts the standalone AG-UI to A2A adapter."""
    try:
        default_target = default_target_from_env()
        if a2a_url:
            default_target = A2ATarget(
                url=a2a_url,
                transport=a2a_transport or (
                    default_target.transport if default_target else None
                ),
            )
        elif default_target is None:
            default_target = A2ATarget(
                url='http://127.0.0.1:10004',
                transport=a2a_transport,
            )

        app = create_app(default_target=default_target)

        logger.info('Starting AG-UI A2A adapter')
        logger.info(' - AG-UI endpoint: http://%s:%s/', host, port)
        logger.info(' - Health check:    http://%s:%s/healthz', host, port)
        if default_target:
            logger.info(
                ' - Default A2A:     %s (%s)',
                default_target.url,
                default_target.transport or 'server preference',
            )

        uvicorn.run(app, host=host, port=port)
    except Exception:
        logger.exception('Failed to start the AG-UI A2A adapter')
        sys.exit(1)


if __name__ == '__main__':
    main()
