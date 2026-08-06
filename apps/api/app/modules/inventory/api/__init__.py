from .routes.brands import router as brands_router
from .routes.categories import router as categories_router
from .routes.dashboard import router as dashboard_router
from .routes.lots import router as lots_router
from .routes.movements import router as movements_router
from .routes.products import router as products_router
from .routes.suppliers import router as suppliers_router

__all__ = [
    "brands_router",
    "categories_router",
    "dashboard_router",
    "lots_router",
    "movements_router",
    "products_router",
    "suppliers_router",
]
