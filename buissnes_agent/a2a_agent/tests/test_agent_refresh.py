import asyncio
import unittest

from unittest.mock import AsyncMock

from buissnes_agent.a2a_agent.agent import AnalysisAgent


class AnalysisAgentRefreshTests(unittest.IsolatedAsyncioTestCase):
    async def test_start_auto_refresh_initializes_and_polls(self) -> None:
        agent = AnalysisAgent()
        agent.initialize = AsyncMock()

        try:
            await agent.start_auto_refresh(interval_seconds=0.01)
            await asyncio.sleep(0.03)
            self.assertGreaterEqual(agent.initialize.await_count, 2)
        finally:
            await agent.close()

    async def test_start_auto_refresh_can_be_disabled(self) -> None:
        agent = AnalysisAgent()
        agent.initialize = AsyncMock()

        try:
            await agent.start_auto_refresh(interval_seconds=0)
            self.assertEqual(agent.initialize.await_count, 1)
            self.assertIsNone(agent._refresh_task)
        finally:
            await agent.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
