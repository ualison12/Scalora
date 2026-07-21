from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.crm.services.dashboard_service import DashboardService

router = APIRouter(prefix="/crm/dashboard", tags=["CRM Dashboard"])
service = DashboardService()


@router.get("", response_model=dict[str, int])
def get_dashboard_summary(company_id: int = Query(...), db: Session = Depends(get_db)) -> dict[str, int]:
    return service.get_summary(db, company_id=company_id)
