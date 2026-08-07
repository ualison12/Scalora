from typing import Callable, Any, Dict

class Tool:
    """Encapsula funções executáveis por agentes."""
    def __init__(self, name: str, description: str, func: Callable):
        self.name = name
        self.description = description
        self.func = func

    async def run(self, **kwargs) -> Any:
        return await self.func(**kwargs) if callable(self.func) else self.func
