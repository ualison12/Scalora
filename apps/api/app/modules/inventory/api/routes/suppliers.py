from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.inventory.schemas.supplier import SupplierCreate, SupplierResponse, SupplierUpdate
from app.modules.inventory.services.supplier_service import SupplierService

router = APIRouter(prefix="/inventory/suppliers", tags=["Inventory Suppliers"])
service = SupplierService()


@router.post("", response_model=SupplierResponse)
def create_supplier(data: SupplierCreate, db: Session = Depends(get_db)) -> SupplierResponse:
    return service.create(db, company_id=data.company_id, name=data.name, contact_name=data.contact_name, email=data.email)


@router.get("", response_model=list[SupplierResponse])
def list_suppliers(company_id: int, db: Session = Depends(get_db)) -> list[SupplierResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{supplier_id}", response_model=SupplierResponse)
def get_supplier(supplier_id: int, db: Session = Depends(get_db)) -> SupplierResponse:
    supplier = service.get(db, supplier_id=supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return supplier


@router.put("/{supplier_id}", response_model=SupplierResponse)
def update_supplier(supplier_id: int, data: SupplierUpdate, db: Session = Depends(get_db)) -> SupplierResponse:
    supplier = service.get(db, supplier_id=supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return service.update(db, supplier=supplier, name=data.name, contact_name=data.contact_name, email=data.email)


@router.delete("/{supplier_id}")
def delete_supplier(supplier_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    supplier = service.get(db, supplier_id=supplier_id)
    if not supplier:
        raise HTTPException(status_code=404, detail="Supplier not found")
    service.delete(db, supplier=supplier)
    return {"success": True}
