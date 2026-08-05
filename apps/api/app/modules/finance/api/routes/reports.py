from datetime import date

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.finance.schemas.report import FinanceReportResponse
from app.modules.finance.services.report_service import ReportService

router = APIRouter(prefix="/finance/reports", tags=["Finance Reports"])
service = ReportService()


@router.get("", response_model=FinanceReportResponse)
def get_finance_report(
    company_id: int = Query(...),
    kind: str | None = Query(None),
    start_date: date | None = Query(None),
    end_date: date | None = Query(None),
    category_id: int | None = Query(None),
    cost_center_id: int | None = Query(None),
    db: Session = Depends(get_db),
) -> FinanceReportResponse:
    return service.get_finance_report(
        db,
        company_id=company_id,
        kind=kind,
        start_date=start_date,
        end_date=end_date,
        category_id=category_id,
        cost_center_id=cost_center_id,
    )
