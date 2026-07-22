from typing import Optional

from sqlalchemy.orm import Session

from app.modules.finance.models.boleto import Boleto
from app.modules.finance.repositories.boleto_repository import BoletoRepository


class BoletoService:
    def __init__(self) -> None:
        self.repository = BoletoRepository()

    def create(self, db: Session, *, company_id: int, transaction_id: Optional[int], amount: float, code: str) -> Boleto:
        boleto = Boleto(company_id=company_id, transaction_id=transaction_id, amount=amount, code=code, status="pending")
        return self.repository.create(db, boleto)

    def list(self, db: Session, *, company_id: int) -> list[Boleto]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, boleto_id: int) -> Optional[Boleto]:
        return self.repository.get_by_id(db, boleto_id)

    def update(self, db: Session, *, boleto: Boleto, amount: Optional[float] = None, code: Optional[str] = None, status: Optional[str] = None) -> Boleto:
        if amount is not None:
            boleto.amount = amount
        if code is not None:
            boleto.code = code
        if status is not None:
            boleto.status = status
        return self.repository.update(db, boleto)

    def mark_paid(self, db: Session, *, document_id: int) -> Boleto:
        boleto = self.get(db, boleto_id=document_id)
        if not boleto:
            raise ValueError("Boleto not found")
        boleto.status = "paid"
        return self.repository.update(db, boleto)

    def delete(self, db: Session, *, boleto: Boleto) -> None:
        self.repository.delete(db, boleto)
