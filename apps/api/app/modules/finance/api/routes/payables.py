from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.finance.schemas.payable import PayableCreate, PayableResponse, PayableUpdate
from app.modules.finance.services.payable_service import PayableService

router = APIRouter(prefix="/finance/payables", tags=["Finance Payables"])
service = PayableService()


@router.post("", response_model=PayableResponse)
def create_payable(data: PayableCreate, db: Session = Depends(get_db)) -> PayableResponse:
    return service.create(
        db,
        company_id=data.company_id,
        category_id=data.category_id,
        cost_center_id=data.cost_center_id,
        description=data.description,
        amount=data.amount,
        due_date=data.due_date,
    )


@router.get("", response_model=list[PayableResponse])
def list_payables(company_id: int, db: Session = Depends(get_db)) -> list[PayableResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{payable_id}", response_model=PayableResponse)
def get_payable(payable_id: int, db: Session = Depends(get_db)) -> PayableResponse:
    payable = service.get(db, payable_id=payable_id)
    if not payable:
        raise HTTPException(status_code=404, detail="Payable not found")
    return payable


@router.put("/{payable_id}", response_model=PayableResponse)
def update_payable(payable_id: int, data: PayableUpdate, db: Session = Depends(get_db)) -> PayableResponse:
    payable = service.get(db, payable_id=payable_id)
    if not payable:
        raise HTTPException(status_code=404, detail="Payable not found")
    return service.update(
        db,
        payable=payable,
        description=data.description,
        amount=data.amount,
        due_date=data.due_date,
        status=data.status,
    )


@router.post("/{payable_id}/pay", response_model=PayableResponse)
def mark_payable_paid(payable_id: int, db: Session = Depends(get_db)) -> PayableResponse:
    return service.mark_paid(db, transaction_id=payable_id)


@router.delete("/{payable_id}")
def delete_payable(payable_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    payable = service.get(db, payable_id=payable_id)
    if not payable:
        raise HTTPException(status_code=404, detail="Payable not found")
    service.delete(db, payable=payable)
    return {"success": True}
