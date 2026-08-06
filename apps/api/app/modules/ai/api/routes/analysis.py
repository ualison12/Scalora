from fastapi import APIRouter

from app.modules.ai.services.ai_service import AIService

router = APIRouter(prefix="/ai/analysis", tags=["AI Analysis"])
service = AIService()


@router.post("")
def analyze(text: str) -> dict[str, str]:
    return service.analyze_text(text)
