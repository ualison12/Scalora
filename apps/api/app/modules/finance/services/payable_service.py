from datetime import date
from typing import Optional

from sqlalchemy.orm import Session

from app.modules.finance.models.payable import Payable
from app.modules.finance.repositories.payable_repository import PayableRepository


class PayableService:
    def __init__(self) -> None:
        self.repository = PayableRepository()

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
    ) -> Payable:
        payable = Payable(
            company_id=company_id,
            category_id=category_id,
            cost_center_id=cost_center_id,
            description=description,
            amount=amount,
            due_date=due_date,
            status="pending",
        )
        return self.repository.create(db, payable)

    def list(self, db: Session, *, company_id: int) -> list[Payable]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, payable_id: int) -> Optional[Payable]:
        return self.repository.get_by_id(db, payable_id)

    def update(
        self,
        db: Session,
        *,
        payable: Payable,
        description: Optional[str] = None,
        amount: Optional[float] = None,
        due_date: Optional[date] = None,
        status: Optional[str] = None,
    ) -> Payable:
        if description is not None:
            payable.description = description
        if amount is not None:
            payable.amount = amount
        if due_date is not None:
            payable.due_date = due_date
        if status is not None:
            payable.status = status
        return self.repository.update(db, payable)

    def mark_paid(self, db: Session, *, transaction_id: int) -> Payable:
        payable = self.get(db, payable_id=transaction_id)
        if not payable:
            raise ValueError("Payable not found")
        payable.status = "paid"
        return self.repository.update(db, payable)

    def delete(self, db: Session, *, payable: Payable) -> None:
        self.repository.delete(db, payable)
