from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.platform.services.platform_service import PlatformService

router = APIRouter(prefix="/platform/dashboard", tags=["Platform Dashboard"])
service = PlatformService()


@router.get("")
def platform_dashboard(company_id: int, db: Session = Depends(get_db)) -> dict[str, int]:
    return service.get_dashboard(db, company_id=company_id)
