from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.crm.schemas.deal import DealCreate, DealResponse, DealUpdate
from app.modules.crm.services.deal_service import DealService

router = APIRouter(prefix="/crm/deals", tags=["CRM Deals"])
service = DealService()


@router.post("", response_model=DealResponse)
def create_deal(data: DealCreate, db: Session = Depends(get_db)) -> DealResponse:
    return service.create(
        db,
        company_id=data.company_id,
        title=data.title,
        description=data.description,
        amount=data.amount,
        stage_id=data.stage_id,
    )


@router.get("", response_model=list[DealResponse])
def list_deals(company_id: int = Query(...), db: Session = Depends(get_db)) -> list[DealResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{deal_id}", response_model=DealResponse)
def get_deal(deal_id: int, db: Session = Depends(get_db)) -> DealResponse:
    deal = service.get(db, deal_id=deal_id)
    if not deal:
        raise HTTPException(status_code=404, detail="Deal not found")
    return deal


@router.put("/{deal_id}", response_model=DealResponse)
def update_deal(deal_id: int, data: DealUpdate, db: Session = Depends(get_db)) -> DealResponse:
    deal = service.get(db, deal_id=deal_id)
    if not deal:
        raise HTTPException(status_code=404, detail="Deal not found")
    return service.update(
        db,
        deal=deal,
        title=data.title,
        description=data.description,
        amount=data.amount,
        stage_id=data.stage_id,
        status=data.status,
    )


@router.delete("/{deal_id}")
def delete_deal(deal_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    deal = service.get(db, deal_id=deal_id)
    if not deal:
        raise HTTPException(status_code=404, detail="Deal not found")
    service.delete(db, deal=deal)
    return {"success": True}
