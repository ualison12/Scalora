from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.finance.schemas.category import CategoryCreate, CategoryResponse, CategoryUpdate
from app.modules.finance.services.category_service import CategoryService

router = APIRouter(prefix="/finance/categories", tags=["Finance Categories"])
service = CategoryService()


@router.post("", response_model=CategoryResponse)
def create_category(data: CategoryCreate, db: Session = Depends(get_db)) -> CategoryResponse:
    return service.create(db, company_id=data.company_id, name=data.name, kind=data.kind)


@router.get("", response_model=list[CategoryResponse])
def list_categories(company_id: int, db: Session = Depends(get_db)) -> list[CategoryResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{category_id}", response_model=CategoryResponse)
def get_category(category_id: int, db: Session = Depends(get_db)) -> CategoryResponse:
    category = service.get(db, category_id=category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.put("/{category_id}", response_model=CategoryResponse)
def update_category(category_id: int, data: CategoryUpdate, db: Session = Depends(get_db)) -> CategoryResponse:
    category = service.get(db, category_id=category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return service.update(db, category=category, name=data.name, kind=data.kind)


@router.delete("/{category_id}")
def delete_category(category_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    category = service.get(db, category_id=category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    service.delete(db, category=category)
    return {"success": True}
