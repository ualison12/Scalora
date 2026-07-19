from app.models.company import Company
from app.repositories.company_repository import CompanyRepository


class CompanyService:

    def __init__(self):
        self.repository = CompanyRepository()

    def create(self, db, data):
        company = Company(
            name=data.name,
            email=data.email
        )

        return self.repository.create(db, company)

    def list(self, db):
        return self.repository.get_all(db)

    def get(self, db, company_id):
        return self.repository.get_by_id(db, company_id)

    def delete(self, db, company):
        self.repository.delete(db, company)from app.models.company import Company
from app.repositories.company_repository import CompanyRepository


class CompanyService:

    def __init__(self):
        self.repository = CompanyRepository()

    def create(self, db, data):
        company = Company(
            name=data.name,
            email=data.email
        )

        return self.repository.create(db, company)

    def list(self, db):
        return self.repository.get_all(db)

    def get(self, db, company_id):
        return self.repository.get_by_id(db, company_id)

    def delete(self, db, company):
        self.repository.delete(db, company)