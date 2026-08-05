from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.finance.schemas.receivable import ReceivableCreate, ReceivableResponse, ReceivableUpdate
from app.modules.finance.services.receivable_service import ReceivableService

router = APIRouter(prefix="/finance/receivables", tags=["Finance Receivables"])
service = ReceivableService()


@router.post("", response_model=ReceivableResponse)
def create_receivable(data: ReceivableCreate, db: Session = Depends(get_db)) -> ReceivableResponse:
    return service.create(
        db,
        company_id=data.company_id,
        category_id=data.category_id,
        cost_center_id=data.cost_center_id,
        description=data.description,
        amount=data.amount,
        due_date=data.due_date,
    )


@router.get("", response_model=list[ReceivableResponse])
def list_receivables(company_id: int, db: Session = Depends(get_db)) -> list[ReceivableResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{receivable_id}", response_model=ReceivableResponse)
def get_receivable(receivable_id: int, db: Session = Depends(get_db)) -> ReceivableResponse:
    receivable = service.get(db, receivable_id=receivable_id)
    if not receivable:
        raise HTTPException(status_code=404, detail="Receivable not found")
    return receivable


@router.put("/{receivable_id}", response_model=ReceivableResponse)
def update_receivable(receivable_id: int, data: ReceivableUpdate, db: Session = Depends(get_db)) -> ReceivableResponse:
    receivable = service.get(db, receivable_id=receivable_id)
    if not receivable:
        raise HTTPException(status_code=404, detail="Receivable not found")
    return service.update(
        db,
        receivable=receivable,
        description=data.description,
        amount=data.amount,
        due_date=data.due_date,
        status=data.status,
    )


@router.post("/{receivable_id}/receive", response_model=ReceivableResponse)
def mark_receivable_received(receivable_id: int, db: Session = Depends(get_db)) -> ReceivableResponse:
    return service.mark_received(db, transaction_id=receivable_id)


@router.delete("/{receivable_id}")
def delete_receivable(receivable_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    receivable = service.get(db, receivable_id=receivable_id)
    if not receivable:
        raise HTTPException(status_code=404, detail="Receivable not found")
    service.delete(db, receivable=receivable)
    return {"success": True}
