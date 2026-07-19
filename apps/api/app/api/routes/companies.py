from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.company import (
    CompanyCreate,
    CompanyResponse,
)

from app.services.company_service import CompanyService

router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)

service = CompanyService()


@router.post(
    "",
    response_model=CompanyResponse
)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db)
):
    return service.create(db, company)


@router.get(
    "",
    response_model=list[CompanyResponse]
)
def list_companies(
    db: Session = Depends(get_db)
):
    return service.list(db)


@router.get(
    "/{company_id}",
    response_model=CompanyResponse
)
def get_company(
    company_id: int,
    db: Session = Depends(get_db)
):

    company = service.get(db, company_id)

    if not company:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    return company


@router.delete(
    "/{company_id}"
)
def delete_company(
    company_id: int,
    db: Session = Depends(get_db)
):

    company = service.get(db, company_id)

    if not company:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    service.delete(db, company)

    return {
        "message": "Company deleted"
    }
