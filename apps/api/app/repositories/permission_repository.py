from typing import Optional

from sqlalchemy.orm import Session

from app.models.permission import Permission


class PermissionRepository:
    def get_by_name(self, db: Session, name: str) -> Optional[Permission]:
        return db.query(Permission).filter(Permission.name == name).first()

    def list(self, db: Session, skip: int = 0, limit: int = 100) -> list[Permission]:
        return db.query(Permission).offset(skip).limit(limit).all()

    def create(self, db: Session, permission: Permission) -> Permission:
        db.add(permission)
        db.commit()
        db.refresh(permission)
        return permission
