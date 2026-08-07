from app.modules.ai.agents.base import BaseAgent
from app.modules.ai.providers.base import AIProvider
from app.modules.ai.prompts.system_prompts import AGENT_PROMPTS

class SalesAgent(BaseAgent):
    def __init__(self, provider: AIProvider):
        super().__init__(
            name="SalesAgent",
            role="Sales Specialist",
            system_prompt=AGENT_PROMPTS["SalesAgent"],
            provider=provider,
            permissions=["sales:read", "sales:write", "crm:access"]
        )
