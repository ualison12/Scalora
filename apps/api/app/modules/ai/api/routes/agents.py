from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.ai.schemas.agent import AgentCreate, AgentResponse
from app.modules.ai.services.ai_service import AIService

router = APIRouter(prefix="/ai/agents", tags=["AI Agents"])
service = AIService()


@router.post("", response_model=AgentResponse)
def create_agent(data: AgentCreate, db: Session = Depends(get_db)) -> AgentResponse:
    return service.create_agent(db, company_id=data.company_id, name=data.name, provider=data.provider, model=data.model)
