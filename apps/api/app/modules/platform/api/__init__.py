from .routes.admin import router as admin_router
from .routes.backups import router as backups_router
from .routes.billing import router as billing_router
from .routes.dashboard import router as dashboard_router
from .routes.deploy import router as deploy_router
from .routes.logs import router as logs_router
from .routes.plans import router as plans_router
from .routes.sdk import router as sdk_router
from .routes.subscriptions import router as subscriptions_router
from .routes.webhooks import router as webhooks_router

__all__ = [
    "admin_router",
    "backups_router",
    "billing_router",
    "dashboard_router",
    "deploy_router",
    "logs_router",
    "plans_router",
    "sdk_router",
    "subscriptions_router",
    "webhooks_router",
]
