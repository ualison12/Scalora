from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.finance.schemas.boleto import BoletoCreate, BoletoResponse, BoletoUpdate
from app.modules.finance.services.boleto_service import BoletoService

router = APIRouter(prefix="/finance/boletos", tags=["Finance Boletos"])
service = BoletoService()


@router.post("", response_model=BoletoResponse)
def create_boleto(data: BoletoCreate, db: Session = Depends(get_db)) -> BoletoResponse:
    return service.create(
        db,
        company_id=data.company_id,
        transaction_id=data.transaction_id,
        amount=data.amount,
        code=data.code,
    )


@router.get("", response_model=list[BoletoResponse])
def list_boletos(company_id: int, db: Session = Depends(get_db)) -> list[BoletoResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{boleto_id}", response_model=BoletoResponse)
def get_boleto(boleto_id: int, db: Session = Depends(get_db)) -> BoletoResponse:
    boleto = service.get(db, boleto_id=boleto_id)
    if not boleto:
        raise HTTPException(status_code=404, detail="Boleto not found")
    return boleto


@router.put("/{boleto_id}", response_model=BoletoResponse)
def update_boleto(boleto_id: int, data: BoletoUpdate, db: Session = Depends(get_db)) -> BoletoResponse:
    boleto = service.get(db, boleto_id=boleto_id)
    if not boleto:
        raise HTTPException(status_code=404, detail="Boleto not found")
    return service.update(
        db,
        boleto=boleto,
        amount=data.amount,
        code=data.code,
    )


@router.post("/{boleto_id}/pay", response_model=BoletoResponse)
def mark_boleto_paid(boleto_id: int, db: Session = Depends(get_db)) -> BoletoResponse:
    return service.mark_paid(db, document_id=boleto_id)


@router.delete("/{boleto_id}")
def delete_boleto(boleto_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    boleto = service.get(db, boleto_id=boleto_id)
    if not boleto:
        raise HTTPException(status_code=404, detail="Boleto not found")
    service.delete(db, boleto=boleto)
    return {"success": True}
