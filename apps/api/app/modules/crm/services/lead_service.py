from typing import Optional

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.crm.models.lead import Lead
from app.modules.crm.repositories.lead_repository import LeadRepository


class LeadService:
    def __init__(self) -> None:
        self.repository = LeadRepository()

    def create(
        self,
        db: Session,
        *,
        company_id: int,
        name: str,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        source: Optional[str] = None,
    ) -> Lead:
        lead = Lead(
            company_id=company_id,
            name=name,
            email=email,
            phone=phone,
            source=source,
            status="new",
        )
        return self.repository.create(db, lead)

    def list(self, db: Session, *, company_id: int) -> list[Lead]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, lead_id: int) -> Optional[Lead]:
        return self.repository.get_by_id(db, lead_id)

    def update(
        self,
        db: Session,
        *,
        lead: Lead,
        name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        source: Optional[str] = None,
        status: Optional[str] = None,
    ) -> Lead:
        if name is not None:
            lead.name = name
        if email is not None:
            lead.email = email
        if phone is not None:
            lead.phone = phone
        if source is not None:
            lead.source = source
        if status is not None:
            lead.status = status
        return self.repository.update(db, lead)

    def delete(self, db: Session, *, lead: Lead) -> None:
        self.repository.delete(db, lead)
