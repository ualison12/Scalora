from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.auth import LoginRequest, RefreshRequest, TokenResponse
from app.services.auth_service import AuthService
from app.services.user_service import UserService

router = APIRouter(prefix="/auth", tags=["Authentication"])

service = UserService()
auth_service = AuthService()


@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)) -> dict[str, Any]:
    user = service.authenticate(db, email=str(data.email), password=data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return auth_service.login(
        db,
        email=str(user.email),
        password=data.password,
        company_id=user.company_id,
        ip_address="unknown",
        user_agent="api",
    )


@router.post("/logout", response_model=dict[str, bool])
def logout(token: str, db: Session = Depends(get_db)) -> dict[str, bool]:
    auth_service.logout(db, token=token, user_id=1)
    return {"success": True}


@router.post("/refresh", response_model=TokenResponse)
def refresh(data: RefreshRequest, db: Session = Depends(get_db)) -> dict[str, Any]:
    return auth_service.refresh(db, token=data.refresh_token)


@router.get("/me", response_model=dict[str, Any])
def me(db: Session = Depends(get_db)) -> dict[str, Any]:
    user = auth_service.me(db, user_id=1)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"id": user.id, "email": user.email, "company_id": user.company_id}
