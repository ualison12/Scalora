from typing import Optional

from sqlalchemy.orm import Session

from app.modules.crm.models.contact import Contact


class ContactRepository:
    def get_by_id(self, db: Session, contact_id: int) -> Optional[Contact]:
        return db.query(Contact).filter(Contact.id == contact_id).first()

    def list(self, db: Session, *, company_id: int) -> list[Contact]:
        return db.query(Contact).filter(Contact.company_id == company_id).order_by(Contact.id.desc()).all()

    def create(self, db: Session, contact: Contact) -> Contact:
        db.add(contact)
        db.commit()
        db.refresh(contact)
        return contact

    def update(self, db: Session, contact: Contact) -> Contact:
        db.commit()
        db.refresh(contact)
        return contact

    def delete(self, db: Session, contact: Contact) -> None:
        db.delete(contact)
        db.commit()
