from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.platform.schemas.subscription import SubscriptionCreate, SubscriptionResponse
from app.modules.platform.services.platform_service import PlatformService

router = APIRouter(prefix="/platform/subscriptions", tags=["Platform Subscriptions"])
service = PlatformService()


@router.post("", response_model=SubscriptionResponse)
def create_subscription(data: SubscriptionCreate, db: Session = Depends(get_db)) -> SubscriptionResponse:
    return service.create_subscription(db, company_id=data.company_id, plan_id=data.plan_id, status=data.status)
