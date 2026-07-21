from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.role import RoleCreate, RoleResponse
from app.services.role_service import RoleService

router = APIRouter(prefix="/roles", tags=["Roles"])
service = RoleService()


@router.post("", response_model=RoleResponse)
def create_role(data: RoleCreate, db: Session = Depends(get_db)) -> RoleResponse:
    return service.create(db, name=data.name, description=data.description)


@router.get("", response_model=list[RoleResponse])
def list_roles(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=200), db: Session = Depends(get_db)) -> list[RoleResponse]:
    return service.list(db, skip=skip, limit=limit)
