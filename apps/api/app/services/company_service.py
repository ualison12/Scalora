from fastapi import HTTPException

from app.models.company import Company
from app.repositories.company_repository import CompanyRepository


class CompanyService:

    def __init__(self):
        self.repository = CompanyRepository()

    def create(self, db, data):

        if self.repository.get_by_email(db, data.email):
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )

        company = Company(
            name=data.name,
            email=data.email
        )

        return self.repository.create(db, company)

    def list(
        self,
        db,
        skip=0,
        limit=20
    ):
        return self.repository.get_all(
            db,
            skip,
            limit
        )

    def get(
        self,
        db,
        company_id
    ):
        return self.repository.get_by_id(
            db,
            company_id
        )

    def search(
        self,
        db,
        name
    ):
        return self.repository.search(
            db,
            name
        )

    def update(
        self,
        db,
        company,
        data
    ):

        company.name = data.name
        company.email = data.email

        return self.repository.update(
            db,
            company
        )

    def delete(
        self,
        db,
        company
    ):
        self.repository.delete(
            db,
            company
        )