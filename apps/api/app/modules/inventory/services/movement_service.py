from typing import Optional

from sqlalchemy.orm import Session

from app.modules.inventory.models.lot import Lot
from app.modules.inventory.models.movement import Movement
from app.modules.inventory.repositories.movement_repository import MovementRepository


class MovementService:
    def __init__(self) -> None:
        self.repository = MovementRepository()

    def create(
        self,
        db: Session,
        *,
        company_id: int,
        product_id: int,
        lot_id: Optional[int] = None,
        movement_type: str = "in",
        quantity: int = 0,
        unit_cost: float = 0,
        reason: Optional[str] = None,
    ) -> Movement:
        movement = Movement(
            company_id=company_id,
            product_id=product_id,
            lot_id=lot_id,
            movement_type=movement_type,
            quantity=quantity,
            unit_cost=unit_cost,
            reason=reason,
        )
        return self.repository.create(db, movement)

    def list(self, db: Session, *, company_id: int) -> list[Movement]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, movement_id: int) -> Optional[Movement]:
        return self.repository.get_by_id(db, movement_id)

    def update(
        self,
        db: Session,
        *,
        movement: Movement,
        movement_type: Optional[str] = None,
        quantity: Optional[int] = None,
        unit_cost: Optional[float] = None,
        reason: Optional[str] = None,
    ) -> Movement:
        if movement_type is not None:
            movement.movement_type = movement_type
        if quantity is not None:
            movement.quantity = quantity
        if unit_cost is not None:
            movement.unit_cost = unit_cost
        if reason is not None:
            movement.reason = reason
        return self.repository.update(db, movement)

    def delete(self, db: Session, *, movement: Movement) -> None:
        self.repository.delete(db, movement)
