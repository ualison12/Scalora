from typing import Dict, Type
from app.modules.ai.providers.base import AIProvider
from app.modules.ai.providers.openai_provider import OpenAIProvider
from app.modules.ai.providers.claude_provider import AnthropicClaudeProvider
from app.modules.ai.providers.gemini_provider import GeminiProvider
from app.modules.ai.providers.deepseek_provider import DeepSeekProvider

class ProviderFactory:
    _providers: Dict[str, Type[AIProvider]] = {
        "openai": OpenAIProvider,
        "claude": AnthropicClaudeProvider,
        "gemini": GeminiProvider,
        "deepseek": DeepSeekProvider,
    }

    @classmethod
    def create(cls, provider_name: str, api_key: str, model: str = None, **kwargs) -> AIProvider:
        provider_cls = cls._providers.get(provider_name.lower())
        if not provider_cls:
            raise ValueError(f"Provedor '{provider_name}' não suportado. Opções: {list(cls._providers.keys())}")
        
        init_kwargs = {"api_key": api_key, **kwargs}
        if model:
            init_kwargs["model"] = model
            
        return provider_cls(**init_kwargs)
