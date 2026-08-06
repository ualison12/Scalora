from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.inventory.schemas.brand import BrandCreate, BrandResponse, BrandUpdate
from app.modules.inventory.services.brand_service import BrandService

router = APIRouter(prefix="/inventory/brands", tags=["Inventory Brands"])
service = BrandService()


@router.post("", response_model=BrandResponse)
def create_brand(data: BrandCreate, db: Session = Depends(get_db)) -> BrandResponse:
    return service.create(db, company_id=data.company_id, name=data.name)


@router.get("", response_model=list[BrandResponse])
def list_brands(company_id: int, db: Session = Depends(get_db)) -> list[BrandResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{brand_id}", response_model=BrandResponse)
def get_brand(brand_id: int, db: Session = Depends(get_db)) -> BrandResponse:
    brand = service.get(db, brand_id=brand_id)
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")
    return brand


@router.put("/{brand_id}", response_model=BrandResponse)
def update_brand(brand_id: int, data: BrandUpdate, db: Session = Depends(get_db)) -> BrandResponse:
    brand = service.get(db, brand_id=brand_id)
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")
    return service.update(db, brand=brand, name=data.name)


@router.delete("/{brand_id}")
def delete_brand(brand_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    brand = service.get(db, brand_id=brand_id)
    if not brand:
        raise HTTPException(status_code=404, detail="Brand not found")
    service.delete(db, brand=brand)
    return {"success": True}
