from typing import Optional

from sqlalchemy.orm import Session

from app.modules.crm.models.deal import Deal
from app.modules.crm.repositories.deal_repository import DealRepository


class DealService:
    def __init__(self) -> None:
        self.repository = DealRepository()

    def create(
        self,
        db: Session,
        *,
        company_id: int,
        title: str,
        description: Optional[str] = None,
        amount: float = 0.0,
        stage_id: Optional[int] = None,
    ) -> Deal:
        deal = Deal(
            company_id=company_id,
            title=title,
            description=description,
            amount=amount,
            stage_id=stage_id,
            status="open",
        )
        return self.repository.create(db, deal)

    def list(self, db: Session, *, company_id: int) -> list[Deal]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, deal_id: int) -> Optional[Deal]:
        return self.repository.get_by_id(db, deal_id)

    def update(
        self,
        db: Session,
        *,
        deal: Deal,
        title: Optional[str] = None,
        description: Optional[str] = None,
        amount: Optional[float] = None,
        stage_id: Optional[int] = None,
        status: Optional[str] = None,
    ) -> Deal:
        if title is not None:
            deal.title = title
        if description is not None:
            deal.description = description
        if amount is not None:
            deal.amount = amount
        if stage_id is not None:
            deal.stage_id = stage_id
        if status is not None:
            deal.status = status
        return self.repository.update(db, deal)

    def delete(self, db: Session, *, deal: Deal) -> None:
        self.repository.delete(db, deal)
