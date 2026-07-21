from .routes.contacts import router as contacts_router
from .routes.dashboard import router as dashboard_router
from .routes.deals import router as deals_router
from .routes.leads import router as leads_router
from .routes.stages import router as stages_router

__all__ = ["contacts_router", "dashboard_router", "deals_router", "leads_router", "stages_router"]
