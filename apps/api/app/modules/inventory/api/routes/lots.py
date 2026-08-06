from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.inventory.schemas.lot import LotCreate, LotResponse, LotUpdate
from app.modules.inventory.services.lot_service import LotService

router = APIRouter(prefix="/inventory/lots", tags=["Inventory Lots"])
service = LotService()


@router.post("", response_model=LotResponse)
def create_lot(data: LotCreate, db: Session = Depends(get_db)) -> LotResponse:
    return service.create(
        db,
        company_id=data.company_id,
        product_id=data.product_id,
        code=data.code,
        quantity=data.quantity,
        expiration_date=data.expiration_date,
    )


@router.get("", response_model=list[LotResponse])
def list_lots(company_id: int, db: Session = Depends(get_db)) -> list[LotResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{lot_id}", response_model=LotResponse)
def get_lot(lot_id: int, db: Session = Depends(get_db)) -> LotResponse:
    lot = service.get(db, lot_id=lot_id)
    if not lot:
        raise HTTPException(status_code=404, detail="Lot not found")
    return lot


@router.put("/{lot_id}", response_model=LotResponse)
def update_lot(lot_id: int, data: LotUpdate, db: Session = Depends(get_db)) -> LotResponse:
    lot = service.get(db, lot_id=lot_id)
    if not lot:
        raise HTTPException(status_code=404, detail="Lot not found")
    return service.update(db, lot=lot, code=data.code, quantity=data.quantity, expiration_date=data.expiration_date)


@router.delete("/{lot_id}")
def delete_lot(lot_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    lot = service.get(db, lot_id=lot_id)
    if not lot:
        raise HTTPException(status_code=404, detail="Lot not found")
    service.delete(db, lot=lot)
    return {"success": True}
