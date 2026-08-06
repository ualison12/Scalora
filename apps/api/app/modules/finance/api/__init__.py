from .routes.boletos import router as boletos_router
from .routes.categories import router as categories_router
from .routes.cost_centers import router as cost_centers_router
from .routes.dashboard import router as dashboard_router
from .routes.dre import router as dre_router
from .routes.payables import router as payables_router
from .routes.receivables import router as receivables_router
from .routes.pix import router as pix_router
from .routes.reports import router as reports_router

__all__ = [
    "boletos_router",
    "categories_router",
    "cost_centers_router",
    "dashboard_router",
    "dre_router",
    "payables_router",
    "receivables_router",
    "pix_router",
    "reports_router",
]