from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.inventory.schemas.movement import MovementCreate, MovementResponse, MovementUpdate
from app.modules.inventory.services.movement_service import MovementService

router = APIRouter(prefix="/inventory/movements", tags=["Inventory Movements"])
service = MovementService()


@router.post("", response_model=MovementResponse)
def create_movement(data: MovementCreate, db: Session = Depends(get_db)) -> MovementResponse:
    return service.create(
        db,
        company_id=data.company_id,
        product_id=data.product_id,
        lot_id=data.lot_id,
        movement_type=data.movement_type,
        quantity=data.quantity,
        unit_cost=data.unit_cost,
        reason=data.reason,
    )


@router.get("", response_model=list[MovementResponse])
def list_movements(company_id: int, db: Session = Depends(get_db)) -> list[MovementResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{movement_id}", response_model=MovementResponse)
def get_movement(movement_id: int, db: Session = Depends(get_db)) -> MovementResponse:
    movement = service.get(db, movement_id=movement_id)
    if not movement:
        raise HTTPException(status_code=404, detail="Movement not found")
    return movement


@router.put("/{movement_id}", response_model=MovementResponse)
def update_movement(movement_id: int, data: MovementUpdate, db: Session = Depends(get_db)) -> MovementResponse:
    movement = service.get(db, movement_id=movement_id)
    if not movement:
        raise HTTPException(status_code=404, detail="Movement not found")
    return service.update(
        db,
        movement=movement,
        movement_type=data.movement_type,
        quantity=data.quantity,
        unit_cost=data.unit_cost,
        reason=data.reason,
    )


@router.delete("/{movement_id}")
def delete_movement(movement_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    movement = service.get(db, movement_id=movement_id)
    if not movement:
        raise HTTPException(status_code=404, detail="Movement not found")
    service.delete(db, movement=movement)
    return {"success": True}
