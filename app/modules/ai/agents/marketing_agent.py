from app.modules.ai.agents.base import BaseAgent
from app.modules.ai.providers.base import AIProvider
from app.modules.ai.prompts.system_prompts import AGENT_PROMPTS

class MarketingAgent(BaseAgent):
    def __init__(self, provider: AIProvider):
        super().__init__(
            name="MarketingAgent",
            role="Marketing Specialist",
            system_prompt=AGENT_PROMPTS["MarketingAgent"],
            provider=provider,
            permissions=["marketing:read", "marketing:write", "campaigns:manage"]
        )
