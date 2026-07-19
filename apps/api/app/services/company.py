from sqlalchemy.orm import Session

from app.models.company import Company
from app.repositories.company import create_company


def create_new_company(
    db: Session,
    name: str,
    email: str
):

    company = Company(
        name=name,
        email=email
    )


    return create_company(
        db,
        company
    )