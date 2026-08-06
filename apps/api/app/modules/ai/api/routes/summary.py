from fastapi import APIRouter

from app.modules.ai.services.ai_service import AIService

router = APIRouter(prefix="/ai/summary", tags=["AI Summary"])
service = AIService()


@router.post("")
def summarize(text: str) -> dict[str, str]:
    return service.summarize_text(text)
