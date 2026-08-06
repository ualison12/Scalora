from .routes.agents import router as agents_router
from .routes.analysis import router as analysis_router
from .routes.automations import router as automations_router
from .routes.chat import router as chat_router
from .routes.dashboard import router as dashboard_router
from .routes.memory import router as memory_router
from .routes.prompt_manager import router as prompt_manager_router
from .routes.providers import router as providers_router
from .routes.rag import router as rag_router
from .routes.summary import router as summary_router
from .routes.tools import router as tools_router

__all__ = [
    "agents_router",
    "analysis_router",
    "automations_router",
    "chat_router",
    "dashboard_router",
    "memory_router",
    "prompt_manager_router",
    "providers_router",
    "rag_router",
    "summary_router",
    "tools_router",
]
