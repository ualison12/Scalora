from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.crm.models.lead import Lead
from app.modules.crm.schemas.lead import LeadCreate, LeadResponse, LeadUpdate
from app.modules.crm.services.lead_service import LeadService

router = APIRouter(prefix="/crm/leads", tags=["CRM Leads"])
service = LeadService()


@router.post("", response_model=LeadResponse)
def create_lead(data: LeadCreate, db: Session = Depends(get_db)) -> LeadResponse:
    return service.create(
        db,
        company_id=data.company_id,
        name=data.name,
        email=str(data.email) if data.email else None,
        phone=data.phone,
        source=data.source,
    )


@router.get("", response_model=list[LeadResponse])
def list_leads(company_id: int = Query(...), db: Session = Depends(get_db)) -> list[LeadResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{lead_id}", response_model=LeadResponse)
def get_lead(lead_id: int, db: Session = Depends(get_db)) -> LeadResponse:
    lead = service.get(db, lead_id=lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead


@router.put("/{lead_id}", response_model=LeadResponse)
def update_lead(lead_id: int, data: LeadUpdate, db: Session = Depends(get_db)) -> LeadResponse:
    lead = service.get(db, lead_id=lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    return service.update(
        db,
        lead=lead,
        name=data.name,
        email=str(data.email) if data.email else None,
        phone=data.phone,
        source=data.source,
        status=data.status,
    )


@router.delete("/{lead_id}")
def delete_lead(lead_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    lead = service.get(db, lead_id=lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="Lead not found")
    service.delete(db, lead=lead)
    return {"success": True}
