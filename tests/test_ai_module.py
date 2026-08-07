import pytest
from app.modules.ai.providers.factory import ProviderFactory
from app.modules.ai.prompts.manager import PromptManager
from app.modules.ai.memory.conversation import ConversationMemory

def test_prompt_manager():
    pm = PromptManager()
    pm.register_template("test", "Hello {name}")
    assert pm.render("test", name="Scalora") == "Hello Scalora"

def test_conversation_memory():
    mem = ConversationMemory(max_history=2)
    mem.add_message("user", "1")
    mem.add_message("user", "2")
    mem.add_message("user", "3")
    assert len(mem.get_history()) == 2
    assert mem.get_history()[0]["content"] == "2"

def test_invalid_provider():
    with pytest.raises(ValueError):
        ProviderFactory.create("invalid_provider", api_key="123")
