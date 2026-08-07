import asyncio
import aiohttp
from typing import Dict, Any, Callable, Awaitable
from app.modules.ai.providers.factory import ProviderFactory

ActionHandler = Callable[[Dict[str, Any], Dict[str, Any]], Awaitable[Dict[str, Any]]]

class ActionRegistry:
    def __init__(self):
        self._handlers: Dict[str, ActionHandler] = {}
        self._register_default_actions()

    def register(self, name: str, handler: ActionHandler):
        self._handlers[name] = handler

    def get(self, name: str) -> ActionHandler:
        if name not in self._handlers:
            raise ValueError(f"Acao/Handler '{name}' nao registrado na Engine de Automacao.")
        return self._handlers[name]

    def _register_default_actions(self):
        async def handle_delay(config: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
            seconds = config.get("seconds", 0)
            await asyncio.sleep(seconds)
            return {"status": "delayed", "waited_seconds": seconds}

        async def handle_webhook(config: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
            url = config.get("url")
            method = config.get("method", "POST").upper()
            headers = config.get("headers", {})
            payload = config.get("body", context)

            async with aiohttp.ClientSession() as session:
                async with session.request(method, url, json=payload, headers=headers) as response:
                    res_text = await response.text()
                    return {"status_code": response.status, "response": res_text}

        async def handle_ai_generate(config: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
            provider_name = config.get("provider", "openai")
            api_key = config.get("api_key")
            prompt_template = config.get("prompt", "{input}")
            
            prompt = prompt_template.format(**context)
            provider = ProviderFactory.create(provider_name, api_key=api_key)
            result = await provider.generate(prompt)
            return {"ai_output": result}

        async def handle_email(config: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
            to_email = config.get("to")
            return {"status": "sent", "recipient": to_email, "type": "email"}

        async def handle_whatsapp(config: Dict[str, Any], context: Dict[str, Any]) -> Dict[str, Any]:
            phone = config.get("phone")
            return {"status": "sent", "recipient": phone, "type": "whatsapp"}

        self.register("delay.wait", handle_delay)
        self.register("webhook.request", handle_webhook)
        self.register("ai.generate", handle_ai_generate)
        self.register("email.send", handle_email)
        self.register("whatsapp.send", handle_whatsapp)
