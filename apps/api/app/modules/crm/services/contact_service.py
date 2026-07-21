from typing import Optional

from sqlalchemy.orm import Session

from app.modules.crm.models.contact import Contact
from app.modules.crm.repositories.contact_repository import ContactRepository


class ContactService:
    def __init__(self) -> None:
        self.repository = ContactRepository()

    def create(
        self,
        db: Session,
        *,
        company_id: int,
        first_name: str,
        last_name: str,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        job_title: Optional[str] = None,
    ) -> Contact:
        contact = Contact(
            company_id=company_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone=phone,
            job_title=job_title,
        )
        return self.repository.create(db, contact)

    def list(self, db: Session, *, company_id: int) -> list[Contact]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, contact_id: int) -> Optional[Contact]:
        return self.repository.get_by_id(db, contact_id)

    def update(
        self,
        db: Session,
        *,
        contact: Contact,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        job_title: Optional[str] = None,
    ) -> Contact:
        if first_name is not None:
            contact.first_name = first_name
        if last_name is not None:
            contact.last_name = last_name
        if email is not None:
            contact.email = email
        if phone is not None:
            contact.phone = phone
        if job_title is not None:
            contact.job_title = job_title
        return self.repository.update(db, contact)

    def delete(self, db: Session, *, contact: Contact) -> None:
        self.repository.delete(db, contact)
