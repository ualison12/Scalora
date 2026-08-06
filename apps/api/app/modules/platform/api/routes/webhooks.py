from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.platform.schemas.webhook import WebhookCreate, WebhookResponse
from app.modules.platform.services.platform_service import PlatformService

router = APIRouter(prefix="/platform/webhooks", tags=["Platform Webhooks"])
service = PlatformService()


@router.post("", response_model=WebhookResponse)
def create_webhook(data: WebhookCreate, db: Session = Depends(get_db)) -> WebhookResponse:
    return service.create_webhook(db, company_id=data.company_id, name=data.name, endpoint=data.endpoint)
