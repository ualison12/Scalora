from typing import Dict, Any

class PromptManager:
    def __init__(self):
        self._templates: Dict[str, str] = {}

    def register_template(self, name: str, template: str) -> None:
        self._templates[name] = template

    def render(self, name: str, **variables: Any) -> str:
        if name not in self._templates:
            raise KeyError(f"Template '{name}' não registrado.")
        return self._templates[name].format(**variables)
