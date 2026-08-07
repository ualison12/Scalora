from app.modules.ai.agents.base import BaseAgent
from app.modules.ai.providers.base import AIProvider
from app.modules.ai.prompts.system_prompts import AGENT_PROMPTS

class FinanceAgent(BaseAgent):
    def __init__(self, provider: AIProvider):
        super().__init__(
            name="FinanceAgent",
            role="Financial Manager",
            system_prompt=AGENT_PROMPTS["FinanceAgent"],
            provider=provider,
            permissions=["finance:read", "finance:write", "reports:generate"]
        )
