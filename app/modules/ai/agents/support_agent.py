from app.modules.ai.agents.base import BaseAgent
from app.modules.ai.providers.base import AIProvider
from app.modules.ai.prompts.system_prompts import AGENT_PROMPTS

class SupportAgent(BaseAgent):
    def __init__(self, provider: AIProvider):
        super().__init__(
            name="SupportAgent",
            role="Customer Support Lead",
            system_prompt=AGENT_PROMPTS["SupportAgent"],
            provider=provider,
            permissions=["support:tickets", "kb:read"]
        )
