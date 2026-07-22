from datetime import date
from typing import Optional

from sqlalchemy.orm import Session

from app.modules.finance.models.receivable import Receivable
from app.modules.finance.repositories.receivable_repository import ReceivableRepository


class ReceivableService:
    def __init__(self) -> None:
        self.repository = ReceivableRepository()

    def create(
        self,
        db: Session,
        *,
        company_id: int,
        category_id: Optional[int] = None,
        cost_center_id: Optional[int] = None,
        description: str,
        amount: float,
        due_date: date,
    ) -> Receivable:
        receivable = Receivable(
            company_id=company_id,
            category_id=category_id,
            cost_center_id=cost_center_id,
            description=description,
            amount=amount,
            due_date=due_date,
            status="pending",
        )
        return self.repository.create(db, receivable)

    def list(self, db: Session, *, company_id: int) -> list[Receivable]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, receivable_id: int) -> Optional[Receivable]:
        return self.repository.get_by_id(db, receivable_id)

    def update(
        self,
        db: Session,
        *,
        receivable: Receivable,
        description: Optional[str] = None,
        amount: Optional[float] = None,
        due_date: Optional[date] = None,
        status: Optional[str] = None,
    ) -> Receivable:
        if description is not None:
            receivable.description = description
        if amount is not None:
            receivable.amount = amount
        if due_date is not None:
            receivable.due_date = due_date
        if status is not None:
            receivable.status = status
        return self.repository.update(db, receivable)

    def mark_received(self, db: Session, *, transaction_id: int) -> Receivable:
        receivable = self.get(db, receivable_id=transaction_id)
        if not receivable:
            raise ValueError("Receivable not found")
        receivable.status = "received"
        return self.repository.update(db, receivable)

    def delete(self, db: Session, *, receivable: Receivable) -> None:
        self.repository.delete(db, receivable)
