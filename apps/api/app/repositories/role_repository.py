from typing import Optional

from sqlalchemy.orm import Session

from app.models.role import Role


class RoleRepository:
    def get_by_name(self, db: Session, name: str) -> Optional[Role]:
        return db.query(Role).filter(Role.name == name).first()

    def list(self, db: Session, skip: int = 0, limit: int = 100) -> list[Role]:
        return db.query(Role).offset(skip).limit(limit).all()

    def create(self, db: Session, role: Role) -> Role:
        db.add(role)
        db.commit()
        db.refresh(role)
        return role
