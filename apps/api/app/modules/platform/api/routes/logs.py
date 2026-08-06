from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.platform.schemas.audit_log import PlatformLogCreate, PlatformLogResponse
from app.modules.platform.services.platform_service import PlatformService

router = APIRouter(prefix="/platform/logs", tags=["Platform Logs"])
service = PlatformService()


@router.post("", response_model=PlatformLogResponse)
def create_log(data: PlatformLogCreate, db: Session = Depends(get_db)) -> PlatformLogResponse:
    return service.create_log_entry(db, company_id=data.company_id, level=data.level, message=data.message)
