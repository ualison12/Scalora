from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.platform.schemas.plan import PlanCreate, PlanResponse
from app.modules.platform.services.platform_service import PlatformService

router = APIRouter(prefix="/platform/plans", tags=["Platform Plans"])
service = PlatformService()


@router.post("", response_model=PlanResponse)
def create_plan(data: PlanCreate, db: Session = Depends(get_db)) -> PlanResponse:
    return service.create_plan(db, company_id=data.company_id, name=data.name, price=data.price, billing_period=data.billing_period)
