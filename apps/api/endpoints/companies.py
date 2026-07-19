from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from app.db.session import SessionLocal

from app.schemas.company import CompanyCreate, CompanyResponse

from app.services.company import create_new_company


router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)



def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()



@router.post(
    "",
    response_model=CompanyResponse
)
def create_company_endpoint(
    company: CompanyCreate,
    db: Session = Depends(get_db)
):

    return create_new_company(
        db,
        company.name,
        company.email
    )