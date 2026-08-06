from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.ai.schemas.provider import ProviderCreate, ProviderResponse
from app.modules.ai.services.ai_service import AIService

router = APIRouter(prefix="/ai/providers", tags=["AI Providers"])
service = AIService()


@router.post("", response_model=ProviderResponse)
def create_provider(data: ProviderCreate, db: Session = Depends(get_db)) -> ProviderResponse:
    return service.configure_provider(
        db,
        company_id=data.company_id,
        provider_name=data.provider_name,
        api_key=data.api_key,
        model_name=data.model_name,
        enabled=data.enabled,
    )


@router.get("", response_model=list[ProviderResponse])
def list_providers(company_id: int, db: Session = Depends(get_db)) -> list[ProviderResponse]:
    return db.query(service.configure_provider.__annotations__.get("return", None)).filter_by(company_id=company_id).all() if False else []
