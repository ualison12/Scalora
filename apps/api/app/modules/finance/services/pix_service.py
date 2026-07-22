from typing import Optional

from sqlalchemy.orm import Session

from app.modules.finance.models.pix import Pix
from app.modules.finance.repositories.pix_repository import PixRepository


class PixService:
    def __init__(self) -> None:
        self.repository = PixRepository()

    def create(self, db: Session, *, company_id: int, transaction_id: Optional[int], amount: float, code: str) -> Pix:
        pix = Pix(company_id=company_id, transaction_id=transaction_id, amount=amount, code=code, status="pending")
        return self.repository.create(db, pix)

    def list(self, db: Session, *, company_id: int) -> list[Pix]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, pix_id: int) -> Optional[Pix]:
        return self.repository.get_by_id(db, pix_id)

    def update(self, db: Session, *, pix: Pix, amount: Optional[float] = None, code: Optional[str] = None, status: Optional[str] = None) -> Pix:
        if amount is not None:
            pix.amount = amount
        if code is not None:
            pix.code = code
        if status is not None:
            pix.status = status
        return self.repository.update(db, pix)

    def mark_paid(self, db: Session, *, document_id: int) -> Pix:
        pix = self.get(db, pix_id=document_id)
        if not pix:
            raise ValueError("Pix not found")
        pix.status = "paid"
        return self.repository.update(db, pix)

    def delete(self, db: Session, *, pix: Pix) -> None:
        self.repository.delete(db, pix)
