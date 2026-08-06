from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.inventory.schemas.product import ProductCreate, ProductResponse, ProductUpdate
from app.modules.inventory.services.product_service import ProductService

router = APIRouter(prefix="/inventory/products", tags=["Inventory Products"])
service = ProductService()


@router.post("", response_model=ProductResponse)
def create_product(data: ProductCreate, db: Session = Depends(get_db)) -> ProductResponse:
    return service.create(
        db,
        company_id=data.company_id,
        category_id=data.category_id,
        brand_id=data.brand_id,
        supplier_id=data.supplier_id,
        name=data.name,
        sku=data.sku,
        barcode=data.barcode,
        cost_price=data.cost_price,
        sale_price=data.sale_price,
        min_stock=data.min_stock,
    )


@router.get("", response_model=list[ProductResponse])
def list_products(company_id: int, db: Session = Depends(get_db)) -> list[ProductResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)) -> ProductResponse:
    product = service.get(db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, data: ProductUpdate, db: Session = Depends(get_db)) -> ProductResponse:
    product = service.get(db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return service.update(
        db,
        product=product,
        name=data.name,
        sku=data.sku,
        barcode=data.barcode,
        cost_price=data.cost_price,
        sale_price=data.sale_price,
        min_stock=data.min_stock,
    )


@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    product = service.get(db, product_id=product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    service.delete(db, product=product)
    return {"success": True}
