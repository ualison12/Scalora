from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.permission import PermissionCreate, PermissionResponse
from app.services.permission_service import PermissionService

router = APIRouter(prefix="/permissions", tags=["Permissions"])
service = PermissionService()


@router.post("", response_model=PermissionResponse)
def create_permission(data: PermissionCreate, db: Session = Depends(get_db)) -> PermissionResponse:
    return service.create(db, name=data.name, description=data.description)


@router.get("", response_model=list[PermissionResponse])
def list_permissions(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=200), db: Session = Depends(get_db)) -> list[PermissionResponse]:
    return service.list(db, skip=skip, limit=limit)
