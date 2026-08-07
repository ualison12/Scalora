from app.modules.ai.agents.base import BaseAgent
from app.modules.ai.providers.base import AIProvider
from app.modules.ai.prompts.system_prompts import AGENT_PROMPTS

class CEOAgent(BaseAgent):
    def __init__(self, provider: AIProvider):
        super().__init__(
            name="CEOAgent",
            role="Chief Executive Officer",
            system_prompt=AGENT_PROMPTS["CEOAgent"],
            provider=provider,
            permissions=["all"]
        )
