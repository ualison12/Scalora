from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.role import Role
from app.repositories.role_repository import RoleRepository


class RoleService:
    def __init__(self) -> None:
        self.repository = RoleRepository()

    def create(self, db: Session, *, name: str, description: str | None = None) -> Role:
        if self.repository.get_by_name(db, name):
            raise HTTPException(status_code=400, detail="Role already exists")
        role = Role(name=name, description=description)
        return self.repository.create(db, role)

    def list(self, db: Session, *, skip: int = 0, limit: int = 100) -> list[Role]:
        return self.repository.list(db, skip=skip, limit=limit)
