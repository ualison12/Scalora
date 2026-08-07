from typing import List, Dict, Any, Optional
from app.modules.ai.providers.base import AIProvider
from app.modules.ai.memory.conversation import ConversationMemory
from app.modules.ai.tools.base import Tool

class BaseAgent:
    """Classe base genérica para todos os agentes do Scalora."""

    def __init__(
        self,
        name: str,
        role: str,
        system_prompt: str,
        provider: AIProvider,
        permissions: List[str],
        tools: Optional[List[Tool]] = None,
        max_history: int = 20
    ):
        self.name = name
        self.role = role
        self.system_prompt = system_prompt
        self.provider = provider
        self.permissions = permissions
        self.tools = {tool.name: tool for tool in (tools or [])}
        self.memory = ConversationMemory(max_history=max_history)

    def check_permission(self, permission: str) -> bool:
        return "all" in self.permissions or permission in self.permissions

    async def execute_tool(self, tool_name: str, **kwargs) -> Any:
        if tool_name not in self.tools:
            raise ValueError(f"Ferramenta '{tool_name}' não disponível para o agente {self.name}.")
        return await self.tools[tool_name].run(**kwargs)

    async def run(self, user_input: str) -> str:
        self.memory.add_message("user", user_input)
        
        # Constrói o histórico formatado
        history = self.memory.get_history()
        prompt_with_context = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in history])
        
        response = await self.provider.generate(
            prompt=prompt_with_context,
            system_instruction=self.system_prompt
        )
        
        self.memory.add_message("assistant", response)
        return response
