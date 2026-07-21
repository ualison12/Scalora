from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.permission import Permission
from app.repositories.permission_repository import PermissionRepository


class PermissionService:
    def __init__(self) -> None:
        self.repository = PermissionRepository()

    def create(self, db: Session, *, name: str, description: str | None = None) -> Permission:
        if self.repository.get_by_name(db, name):
            raise HTTPException(status_code=400, detail="Permission already exists")
        permission = Permission(name=name, description=description)
        return self.repository.create(db, permission)

    def list(self, db: Session, *, skip: int = 0, limit: int = 100) -> list[Permission]:
        return self.repository.list(db, skip=skip, limit=limit)
