import asyncio
import unittest

from types import SimpleNamespace
from unittest.mock import AsyncMock

from buissnes_agent.a2a_agent.agent import AnalysisAgent, ResponseFormat


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

    async def test_get_agent_response_preserves_full_final_content(self) -> None:
        agent = AnalysisAgent()
        repeated_detail = (
            "- To jest bardzo dluga odpowiedz testowa, ktora nie powinna zostac "
            "obcieta nawet wtedy, gdy przekracza limit status update'ow."
        )
        long_message = (
            "Tak, w przestrzeni SD znajduje sie strona o tytule \"Coal\".\n\n"
            "Szczegoly:\n"
            + "\n".join([repeated_detail] * 3)
        )
        agent.graph = SimpleNamespace(
            aget_state=AsyncMock(
                return_value=SimpleNamespace(
                    values={
                        'messages': [],
                        'structured_response': ResponseFormat(
                            status='completed',
                            message=long_message,
                        ),
                    }
                )
            )
        )

        try:
            response = await agent.get_agent_response({'configurable': {}})
        finally:
            await agent.close()

        self.assertEqual(response['task_state'], 'completed')
        self.assertEqual(response['content'], long_message)
        self.assertIn('\n\nSzczegoly:\n- ', response['content'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
