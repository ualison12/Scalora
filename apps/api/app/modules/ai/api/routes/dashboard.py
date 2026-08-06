from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.ai.services.ai_service import AIService

router = APIRouter(prefix="/ai/dashboard", tags=["AI Dashboard"])
service = AIService()


@router.get("")
def dashboard(company_id: int, db: Session = Depends(get_db)) -> dict[str, int]:
    return service.get_dashboard(db, company_id=company_id)
