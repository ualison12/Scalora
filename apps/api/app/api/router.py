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
from app.modules.finance.api import (
    boletos_router,
    categories_router,
    cost_centers_router,
    dashboard_router as finance_dashboard_router,
    dre_router,
    payables_router,
    receivables_router,
    pix_router,
    reports_router,
)
from app.modules.inventory.api import (
    brands_router,
    categories_router as inventory_categories_router,
    dashboard_router as inventory_dashboard_router,
    lots_router,
    movements_router,
    products_router,
    suppliers_router,
)
from app.modules.ai.api import (
    agents_router,
    analysis_router,
    automations_router,
    chat_router,
    dashboard_router as ai_dashboard_router,
    memory_router,
    prompt_manager_router,
    providers_router,
    rag_router,
    summary_router,
    tools_router,
)
from app.modules.platform.api import (
    admin_router,
    backups_router,
    billing_router,
    dashboard_router as platform_dashboard_router,
    deploy_router,
    logs_router,
    plans_router,
    sdk_router,
    subscriptions_router,
    webhooks_router,
)


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
api_router.include_router(boletos_router)
api_router.include_router(categories_router)
api_router.include_router(cost_centers_router)
api_router.include_router(finance_dashboard_router)
api_router.include_router(dre_router)
api_router.include_router(payables_router)
api_router.include_router(receivables_router)
api_router.include_router(pix_router)
api_router.include_router(reports_router)
api_router.include_router(inventory_categories_router)
api_router.include_router(brands_router)
api_router.include_router(suppliers_router)
api_router.include_router(products_router)
api_router.include_router(lots_router)
api_router.include_router(movements_router)
api_router.include_router(inventory_dashboard_router)
api_router.include_router(providers_router)
api_router.include_router(agents_router)
api_router.include_router(memory_router)
api_router.include_router(rag_router)
api_router.include_router(prompt_manager_router)
api_router.include_router(tools_router)
api_router.include_router(automations_router)
api_router.include_router(summary_router)
api_router.include_router(analysis_router)
api_router.include_router(chat_router)
api_router.include_router(ai_dashboard_router)
api_router.include_router(plans_router)
api_router.include_router(subscriptions_router)
api_router.include_router(billing_router)
api_router.include_router(webhooks_router)
api_router.include_router(sdk_router)
api_router.include_router(admin_router)
api_router.include_router(logs_router)
api_router.include_router(backups_router)
api_router.include_router(deploy_router)
api_router.include_router(platform_dashboard_router)
