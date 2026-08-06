from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.ai.schemas.prompt import PromptTemplateCreate, PromptTemplateResponse
from app.modules.ai.services.ai_service import AIService

router = APIRouter(prefix="/ai/prompts", tags=["AI Prompt Manager"])
service = AIService()


@router.post("", response_model=PromptTemplateResponse)
def create_prompt(data: PromptTemplateCreate, db: Session = Depends(get_db)) -> PromptTemplateResponse:
    return service.create_prompt_template(db, company_id=data.company_id, name=data.name, template=data.template)
