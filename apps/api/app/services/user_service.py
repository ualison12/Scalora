from typing import Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import hash_password, verify_password
from app.models.user import User
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self) -> None:
        self.repository = UserRepository()

    def create(
        self,
        db: Session,
        *,
        company_id: int,
        name: str,
        email: str,
        password: str,
    ) -> User:
        if self.repository.get_by_email(db, email):
            raise HTTPException(status_code=400, detail="Email already exists")

        user = User(
            company_id=company_id,
            name=name,
            email=email,
            password_hash=hash_password(password),
        )
        return self.repository.create(db, user)

    def list(self, db: Session, *, skip: int = 0, limit: int = 100) -> list[User]:
        return self.repository.list(db, skip=skip, limit=limit)

    def get(self, db: Session, *, user_id: int) -> Optional[User]:
        return self.repository.get_by_id(db, user_id)

    def update(
        self,
        db: Session,
        *,
        user: User,
        name: Optional[str] = None,
        email: Optional[str] = None,
    ) -> User:
        if name is not None:
            user.name = name
        if email is not None:
            user.email = email
        return self.repository.update(db, user)

    def delete(self, db: Session, *, user: User) -> None:
        self.repository.delete(db, user)

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.repository.get_by_email(db, email)
        if not user:
            return None
        if not verify_password(password, user.password_hash):
            return None
        return user
