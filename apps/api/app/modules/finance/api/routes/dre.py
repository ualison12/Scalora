from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.finance.schemas.report import DreSummaryResponse
from app.modules.finance.services.dre_service import DreService

router = APIRouter(prefix="/finance/dre", tags=["Finance DRE"])
service = DreService()


@router.get("", response_model=DreSummaryResponse)
def get_dre_summary(company_id: int = Query(...), db: Session = Depends(get_db)) -> DreSummaryResponse:
    return service.get_summary(db, company_id=company_id)
