from typing import AsyncGenerator, Optional, Any
import anthropic
from app.modules.ai.providers.base import AIProvider

class AnthropicClaudeProvider(AIProvider):
    def __init__(self, api_key: str, model: str = "claude-3-5-sonnet-20241022"):
        self.client = anthropic.AsyncAnthropic(api_key=api_key)
        self.model = model

    async def generate(self, prompt: str, system_instruction: Optional[str] = None, temperature: float = 0.7, **kwargs: Any) -> str:
        kwargs_clean = {"system": system_instruction} if system_instruction else {}
        response = await self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}],
            **kwargs_clean
        )
        return response.content[0].text

    async def stream(self, prompt: str, system_instruction: Optional[str] = None, temperature: float = 0.7, **kwargs: Any) -> AsyncGenerator[str, None]:
        kwargs_clean = {"system": system_instruction} if system_instruction else {}
        async with self.client.messages.stream(
            model=self.model,
            max_tokens=4096,
            temperature=temperature,
            messages=[{"role": "user", "content": prompt}],
            **kwargs_clean
        ) as stream:
            async for text in stream.text_stream:
                yield text
