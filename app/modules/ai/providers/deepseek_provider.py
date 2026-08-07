import openai
from app.modules.ai.providers.openai_provider import OpenAIProvider

class DeepSeekProvider(OpenAIProvider):
    def __init__(self, api_key: str, model: str = "deepseek-chat", base_url: str = "https://api.deepseek.com"):
        self.client = openai.AsyncOpenAI(api_key=api_key, base_url=base_url)
        self.model = model
