from sqlalchemy.orm import Session

from app.models.company import Company


class CompanyRepository:

    def create(self, db: Session, company: Company):
        db.add(company)
        db.commit()
        db.refresh(company)
        return company

    def get_all(
        self,
        db: Session,
        skip: int = 0,
        limit: int = 20
    ):
        return (
            db.query(Company)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def get_by_id(
        self,
        db: Session,
        company_id: int
    ):
        return (
            db.query(Company)
            .filter(Company.id == company_id)
            .first()
        )

    def get_by_email(
        self,
        db: Session,
        email: str
    ):
        return (
            db.query(Company)
            .filter(Company.email == email)
            .first()
        )

    def search(
        self,
        db: Session,
        name: str
    ):
        return (
            db.query(Company)
            .filter(Company.name.ilike(f"%{name}%"))
            .all()
        )

    def update(
        self,
        db: Session,
        company: Company
    ):
        db.commit()
        db.refresh(company)
        return company

    def delete(
        self,
        db: Session,
        company: Company
    ):
        db.delete(company)
        db.commit()