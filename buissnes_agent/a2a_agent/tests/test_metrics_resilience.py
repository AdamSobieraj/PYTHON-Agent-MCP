import unittest

from unittest.mock import patch

from buissnes_agent.metrics.repository_factory import MetricsRepositoryFactory
from buissnes_agent.tools import rag_metrics


class MetricsResilienceTests(unittest.TestCase):
    def tearDown(self) -> None:
        MetricsRepositoryFactory.reset_singleton()
        rag_metrics.MetricsCollector._instance = None

    def test_metrics_collector_disables_itself_when_postgres_backend_is_unavailable(self) -> None:
        MetricsRepositoryFactory.reset_singleton()
        rag_metrics.MetricsCollector._instance = None

        with (
            patch.object(rag_metrics, "METRICS_ENABLED", True),
            patch.object(
                MetricsRepositoryFactory,
                "_load_postgres_repository_class",
                side_effect=ModuleNotFoundError("No module named 'psycopg2'"),
            ),
        ):
            collector = rag_metrics.MetricsCollector()

        self.assertFalse(collector.is_enabled())
        self.assertIsNone(collector.repository)
