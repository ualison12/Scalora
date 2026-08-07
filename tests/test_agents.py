import pytest
from unittest.mock import AsyncMock
from app.modules.ai.providers.base import AIProvider
from app.modules.ai.agents.ceo_agent import CEOAgent
from app.modules.ai.agents.sales_agent import SalesAgent

@pytest.fixture
def mock_provider():
    provider = AsyncMock(spec=AIProvider)
    provider.generate.return_value = "Resposta simulada da IA"
    return provider

@pytest.mark.asyncio
async def test_ceo_agent_permissions_and_run(mock_provider):
    agent = CEOAgent(provider=mock_provider)
    assert agent.check_permission("any_permission") is True
    
    response = await agent.run("Qual a nossa estratégia?")
    assert response == "Resposta simulada da IA"
    assert len(agent.memory.get_history()) == 2

def test_sales_agent_permissions(mock_provider):
    agent = SalesAgent(provider=mock_provider)
    assert agent.check_permission("sales:read") is True
    assert agent.check_permission("finance:write") is False
