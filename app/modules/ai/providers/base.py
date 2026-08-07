from abc import ABC, abstractmethod
from typing import AsyncGenerator, Dict, Any, List, Optional

class AIProvider(ABC):
    """Interface genérica para provedores de LLM."""

    @abstractmethod
    async def generate(
        self,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        **kwargs: Any
    ) -> str:
        pass

    @abstractmethod
    async def stream(
        self,
        prompt: str,
        system_instruction: Optional[str] = None,
        temperature: float = 0.7,
        **kwargs: Any
    ) -> AsyncGenerator[str, None]:
        pass
