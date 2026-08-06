from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.platform.schemas.backup import BackupCreate, BackupResponse
from app.modules.platform.services.platform_service import PlatformService

router = APIRouter(prefix="/platform/backups", tags=["Platform Backups"])
service = PlatformService()


@router.post("", response_model=BackupResponse)
def create_backup(data: BackupCreate, db: Session = Depends(get_db)) -> BackupResponse:
    return service.create_backup(db, company_id=data.company_id, name=data.name, status=data.status)
