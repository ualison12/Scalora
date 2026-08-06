from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.ai.schemas.automation import AutomationCreate, AutomationResponse
from app.modules.ai.services.ai_service import AIService

router = APIRouter(prefix="/ai/automations", tags=["AI Automations"])
service = AIService()


@router.post("", response_model=AutomationResponse)
def create_automation(data: AutomationCreate, db: Session = Depends(get_db)) -> AutomationResponse:
    return service.create_automation(db, company_id=data.company_id, name=data.name, trigger=data.trigger, action=data.action)
