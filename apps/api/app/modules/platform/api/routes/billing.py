from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.platform.schemas.billing_event import BillingEventCreate, BillingEventResponse
from app.modules.platform.services.platform_service import PlatformService

router = APIRouter(prefix="/platform/billing", tags=["Platform Billing"])
service = PlatformService()


@router.post("", response_model=BillingEventResponse)
def create_billing_event(data: BillingEventCreate, db: Session = Depends(get_db)) -> BillingEventResponse:
    return service.create_billing_event(db, company_id=data.company_id, subscription_id=data.subscription_id, amount=data.amount, status=data.status)
