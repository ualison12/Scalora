from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.platform.schemas.admin_user import AdminUserCreate, AdminUserResponse
from app.modules.platform.services.platform_service import PlatformService

router = APIRouter(prefix="/platform/admin", tags=["Platform Admin"])
service = PlatformService()


@router.post("", response_model=AdminUserResponse)
def create_admin_user(data: AdminUserCreate, db: Session = Depends(get_db)) -> AdminUserResponse:
    return service.create_admin_user(db, company_id=data.company_id, username=data.username, role=data.role)
