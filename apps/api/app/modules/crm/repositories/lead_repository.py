from typing import Optional

from sqlalchemy.orm import Session

from app.modules.crm.models.lead import Lead


class LeadRepository:
    def get_by_id(self, db: Session, lead_id: int) -> Optional[Lead]:
        return db.query(Lead).filter(Lead.id == lead_id).first()

    def list(self, db: Session, *, company_id: int) -> list[Lead]:
        return db.query(Lead).filter(Lead.company_id == company_id).order_by(Lead.id.desc()).all()

    def create(self, db: Session, lead: Lead) -> Lead:
        db.add(lead)
        db.commit()
        db.refresh(lead)
        return lead

    def update(self, db: Session, lead: Lead) -> Lead:
        db.commit()
        db.refresh(lead)
        return lead

    def delete(self, db: Session, lead: Lead) -> None:
        db.delete(lead)
        db.commit()
