from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.finance.schemas.report import FinanceDashboardResponse
from app.modules.finance.services.dashboard_service import DashboardService

router = APIRouter(prefix="/finance/dashboard", tags=["Finance Dashboard"])
service = DashboardService()


@router.get("", response_model=FinanceDashboardResponse)
def get_finance_dashboard(company_id: int = Query(...), db: Session = Depends(get_db)) -> FinanceDashboardResponse:
    return service.get_summary(db, company_id=company_id)
