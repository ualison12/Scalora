from typing import List, Dict, Any

class ConversationMemory:
    def __init__(self, max_history: int = 20):
        self.max_history = max_history
        self._history: List[Dict[str, str]] = []

    def add_message(self, role: str, content: str) -> None:
        self._history.append({"role": role, "content": content})
        if len(self._history) > self.max_history:
            self._history.pop(0)

    def get_history(self) -> List[Dict[str, str]]:
        return list(self._history)

    def clear(self) -> None:
        self._history.clear()
