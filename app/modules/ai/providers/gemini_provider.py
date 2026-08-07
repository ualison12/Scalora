from typing import AsyncGenerator, Optional, Any
import google.generativeai as genai
from app.modules.ai.providers.base import AIProvider

class GeminiProvider(AIProvider):
    def __init__(self, api_key: str, model: str = "gemini-1.5-pro"):
        genai.configure(api_key=api_key)
        self.model_name = model

    async def generate(self, prompt: str, system_instruction: Optional[str] = None, temperature: float = 0.7, **kwargs: Any) -> str:
        model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=system_instruction
        )
        response = await model.generate_content_async(
            prompt,
            generation_config=genai.types.GenerationConfig(temperature=temperature)
        )
        return response.text

    async def stream(self, prompt: str, system_instruction: Optional[str] = None, temperature: float = 0.7, **kwargs: Any) -> AsyncGenerator[str, None]:
        model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=system_instruction
        )
        response = await model.generate_content_async(
            prompt,
            generation_config=genai.types.GenerationConfig(temperature=temperature),
            stream=True
        )
        async for chunk in response:
            yield chunk.text
