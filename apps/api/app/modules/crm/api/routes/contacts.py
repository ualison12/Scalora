from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.crm.schemas.contact import ContactCreate, ContactResponse, ContactUpdate
from app.modules.crm.services.contact_service import ContactService

router = APIRouter(prefix="/crm/contacts", tags=["CRM Contacts"])
service = ContactService()


@router.post("", response_model=ContactResponse)
def create_contact(data: ContactCreate, db: Session = Depends(get_db)) -> ContactResponse:
    return service.create(
        db,
        company_id=data.company_id,
        first_name=data.first_name,
        last_name=data.last_name,
        email=str(data.email) if data.email else None,
        phone=data.phone,
        job_title=data.job_title,
    )


@router.get("", response_model=list[ContactResponse])
def list_contacts(company_id: int = Query(...), db: Session = Depends(get_db)) -> list[ContactResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{contact_id}", response_model=ContactResponse)
def get_contact(contact_id: int, db: Session = Depends(get_db)) -> ContactResponse:
    contact = service.get(db, contact_id=contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.put("/{contact_id}", response_model=ContactResponse)
def update_contact(contact_id: int, data: ContactUpdate, db: Session = Depends(get_db)) -> ContactResponse:
    contact = service.get(db, contact_id=contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return service.update(
        db,
        contact=contact,
        first_name=data.first_name,
        last_name=data.last_name,
        email=str(data.email) if data.email else None,
        phone=data.phone,
        job_title=data.job_title,
    )


@router.delete("/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    contact = service.get(db, contact_id=contact_id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    service.delete(db, contact=contact)
    return {"success": True}
