from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.ai.schemas.memory import MemoryCreate, MemoryResponse
from app.modules.ai.services.ai_service import AIService

router = APIRouter(prefix="/ai/memory", tags=["AI Memory"])
service = AIService()


@router.post("", response_model=MemoryResponse)
def create_memory(data: MemoryCreate, db: Session = Depends(get_db)) -> MemoryResponse:
    return service.store_memory(db, company_id=data.company_id, agent_id=data.agent_id, content=data.content, kind=data.kind)
