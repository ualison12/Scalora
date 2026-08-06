from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.ai.services.ai_service import AIService

router = APIRouter(prefix="/ai/chat", tags=["AI Chat"])
service = AIService()


@router.post("")
def chat(company_id: int, provider: str, prompt: str, db: Session = Depends(get_db)) -> dict[str, object]:
    return service.send_chat(db, company_id=company_id, provider=provider, prompt=prompt)
