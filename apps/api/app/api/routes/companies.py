from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.company import (
    CompanyCreate,
    CompanyUpdate,
    CompanyResponse
)

from app.services.company_service import CompanyService

router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)

service = CompanyService()


@router.post("", response_model=CompanyResponse)
def create_company(
    company: CompanyCreate,
    db: Session = Depends(get_db)
):
    return service.create(db, company)


@router.get("", response_model=list[CompanyResponse])
def list_companies(
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    return service.list(db, skip, limit)


@router.get("/search", response_model=list[CompanyResponse])
def search_company(
    name: str,
    db: Session = Depends(get_db)
):
    return service.search(db, name)


@router.get("/{company_id}", response_model=CompanyResponse)
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


@router.put("/{company_id}", response_model=CompanyResponse)
def update_company(
    company_id: int,
    data: CompanyUpdate,
    db: Session = Depends(get_db)
):
    company = service.get(db, company_id)

    if not company:
        raise HTTPException(
            status_code=404,
            detail="Company not found"
        )

    return service.update(db, company, data)


@router.delete("/{company_id}")
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
        "success": True,
        "message": "Company deleted successfully"
    }