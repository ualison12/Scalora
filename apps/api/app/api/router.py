from fastapi import APIRouter

from app.api.endpoints.health import router as health_router
from app.api.routes.companies import router as companies_router
from app.api.routes.permissions import router as permissions_router
from app.api.routes.roles import router as roles_router
from app.api.routes.users import router as users_router
from app.modules.crm.api.routes.contacts import router as crm_contacts_router
from app.modules.crm.api.routes.dashboard import router as crm_dashboard_router
from app.modules.crm.api.routes.deals import router as crm_deals_router
from app.modules.crm.api.routes.leads import router as crm_leads_router
from app.modules.crm.api.routes.stages import router as crm_stages_router


api_router = APIRouter()


api_router.include_router(health_router)
api_router.include_router(companies_router)
api_router.include_router(users_router)
api_router.include_router(roles_router)
api_router.include_router(permissions_router)
api_router.include_router(crm_leads_router)
api_router.include_router(crm_contacts_router)
api_router.include_router(crm_deals_router)
api_router.include_router(crm_stages_router)
api_router.include_router(crm_dashboard_router)
