from app.modules.ai.agents.base import BaseAgent
from app.modules.ai.providers.base import AIProvider
from app.modules.ai.prompts.system_prompts import AGENT_PROMPTS

class OperationsAgent(BaseAgent):
    def __init__(self, provider: AIProvider):
        super().__init__(
            name="OperationsAgent",
            role="Operations Manager",
            system_prompt=AGENT_PROMPTS["OperationsAgent"],
            provider=provider,
            permissions=["ops:workflows", "ops:logs"]
        )
