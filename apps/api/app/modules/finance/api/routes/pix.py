from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.finance.schemas.pix import PixCreate, PixResponse, PixUpdate
from app.modules.finance.services.pix_service import PixService

router = APIRouter(prefix="/finance/pix", tags=["Finance PIX"])
service = PixService()


@router.post("", response_model=PixResponse)
def create_pix(data: PixCreate, db: Session = Depends(get_db)) -> PixResponse:
    return service.create(
        db,
        company_id=data.company_id,
        transaction_id=data.transaction_id,
        amount=data.amount,
        code=data.code,
    )


@router.get("", response_model=list[PixResponse])
def list_pix(company_id: int, db: Session = Depends(get_db)) -> list[PixResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{pix_id}", response_model=PixResponse)
def get_pix(pix_id: int, db: Session = Depends(get_db)) -> PixResponse:
    pix = service.get(db, pix_id=pix_id)
    if not pix:
        raise HTTPException(status_code=404, detail="PIX not found")
    return pix


@router.put("/{pix_id}", response_model=PixResponse)
def update_pix(pix_id: int, data: PixUpdate, db: Session = Depends(get_db)) -> PixResponse:
    pix = service.get(db, pix_id=pix_id)
    if not pix:
        raise HTTPException(status_code=404, detail="PIX not found")
    return service.update(
        db,
        pix=pix,
        amount=data.amount,
        code=data.code,
    )


@router.post("/{pix_id}/pay", response_model=PixResponse)
def mark_pix_paid(pix_id: int, db: Session = Depends(get_db)) -> PixResponse:
    return service.mark_paid(db, document_id=pix_id)


@router.delete("/{pix_id}")
def delete_pix(pix_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    pix = service.get(db, pix_id=pix_id)
    if not pix:
        raise HTTPException(status_code=404, detail="PIX not found")
    service.delete(db, pix=pix)
    return {"success": True}
