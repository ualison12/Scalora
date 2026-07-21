from typing import Optional

from sqlalchemy.orm import Session

from app.modules.crm.models.deal import Deal


class DealRepository:
    def get_by_id(self, db: Session, deal_id: int) -> Optional[Deal]:
        return db.query(Deal).filter(Deal.id == deal_id).first()

    def list(self, db: Session, *, company_id: int) -> list[Deal]:
        return db.query(Deal).filter(Deal.company_id == company_id).order_by(Deal.id.desc()).all()

    def create(self, db: Session, deal: Deal) -> Deal:
        db.add(deal)
        db.commit()
        db.refresh(deal)
        return deal

    def update(self, db: Session, deal: Deal) -> Deal:
        db.commit()
        db.refresh(deal)
        return deal

    def delete(self, db: Session, deal: Deal) -> None:
        db.delete(deal)
        db.commit()
