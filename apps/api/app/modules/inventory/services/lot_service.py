from datetime import date
from typing import Optional

from sqlalchemy.orm import Session

from app.modules.inventory.models.lot import Lot
from app.modules.inventory.repositories.lot_repository import LotRepository


class LotService:
    def __init__(self) -> None:
        self.repository = LotRepository()

    def create(
        self,
        db: Session,
        *,
        company_id: int,
        product_id: int,
        code: str,
        quantity: int = 0,
        expiration_date: Optional[date] = None,
    ) -> Lot:
        lot = Lot(company_id=company_id, product_id=product_id, code=code, quantity=quantity, expiration_date=expiration_date)
        return self.repository.create(db, lot)

    def list(self, db: Session, *, company_id: int) -> list[Lot]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, lot_id: int) -> Optional[Lot]:
        return self.repository.get_by_id(db, lot_id)

    def update(
        self,
        db: Session,
        *,
        lot: Lot,
        code: Optional[str] = None,
        quantity: Optional[int] = None,
        expiration_date: Optional[date] = None,
    ) -> Lot:
        if code is not None:
            lot.code = code
        if quantity is not None:
            lot.quantity = quantity
        if expiration_date is not None:
            lot.expiration_date = expiration_date
        return self.repository.update(db, lot)

    def delete(self, db: Session, *, lot: Lot) -> None:
        self.repository.delete(db, lot)
