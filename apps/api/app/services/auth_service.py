from datetime import datetime, timedelta, timezone
from typing import Any, Optional
from uuid import uuid4

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.security import create_access_token, hash_password, verify_password
from app.models.audit_log import AuditLog
from app.models.refresh_token import RefreshToken
from app.models.session import Session
from app.repositories.audit_log_repository import AuditLogRepository
from app.repositories.refresh_token_repository import RefreshTokenRepository
from app.repositories.session_repository import SessionRepository
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self) -> None:
        self.user_repository = UserRepository()
        self.refresh_token_repository = RefreshTokenRepository()
        self.session_repository = SessionRepository()
        self.audit_log_repository = AuditLogRepository()

    def login(
        self,
        db: Session,
        *,
        email: str,
        password: str,
        company_id: int,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
    ) -> dict[str, Any]:
        user = self.user_repository.get_by_email(db, email)
        if not user or not verify_password(password, user.password_hash):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        if user.company_id != company_id:
            raise HTTPException(status_code=403, detail="User does not belong to this company")

        access_token = create_access_token({"sub": str(user.id), "company_id": user.company_id})
        refresh_token_value = str(uuid4())
        refresh_expires_at = datetime.now(timezone.utc) + timedelta(days=7)

        refresh_token = RefreshToken(
            user_id=user.id,
            token=refresh_token_value,
            expires_at=refresh_expires_at,
        )
        self.refresh_token_repository.create(db, refresh_token)

        session = Session(
            user_id=user.id,
            token=refresh_token_value,
            ip_address=ip_address,
            user_agent=user_agent,
            expires_at=refresh_expires_at,
        )
        self.session_repository.create(db, session)

        self.audit_log_repository.create(
            db,
            AuditLog(
                user_id=user.id,
                company_id=user.company_id,
                action="login",
                entity="auth",
                details="User logged in",
                ip_address=ip_address,
                user_agent=user_agent,
            ),
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token_value,
            "token_type": "bearer",
        }

    def logout(self, db: Session, *, token: str, user_id: int) -> None:
        refresh_token = self.refresh_token_repository.get_by_token(db, token)
        if refresh_token:
            refresh_token.revoked = True
            self.refresh_token_repository.update(db, refresh_token)

        self.audit_log_repository.create(
            db,
            AuditLog(
                user_id=user_id,
                action="logout",
                entity="auth",
                details="User logged out",
            ),
        )

    def refresh(self, db: Session, *, token: str) -> dict[str, Any]:
        refresh_token = self.refresh_token_repository.get_by_token(db, token)
        if not refresh_token or refresh_token.revoked:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
        user = self.user_repository.get_by_id(db, refresh_token.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        access_token = create_access_token({"sub": str(user.id), "company_id": user.company_id})
        return {"access_token": access_token, "token_type": "bearer"}

    def me(self, db: Session, *, user_id: int) -> Any:
        return self.user_repository.get_by_id(db, user_id)
