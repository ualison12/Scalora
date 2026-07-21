from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])
service = UserService()


@router.post("", response_model=UserResponse)
def create_user(data: UserCreate, db: Session = Depends(get_db)) -> UserResponse:
    user = service.create(
        db,
        company_id=data.company_id,
        name=data.name,
        email=str(data.email),
        password=data.password,
    )
    return user


@router.get("", response_model=list[UserResponse])
def list_users(skip: int = Query(0, ge=0), limit: int = Query(100, ge=1, le=200), db: Session = Depends(get_db)) -> list[UserResponse]:
    return service.list(db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)) -> UserResponse:
    user = service.get(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)) -> UserResponse:
    user = service.get(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return service.update(db, user=user, name=data.name, email=str(data.email) if data.email else None)


@router.delete("/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    user = service.get(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    service.delete(db, user=user)
    return {"success": True}
