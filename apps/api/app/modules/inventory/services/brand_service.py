from typing import Optional

from sqlalchemy.orm import Session

from app.modules.inventory.models.brand import Brand
from app.modules.inventory.repositories.brand_repository import BrandRepository


class BrandService:
    def __init__(self) -> None:
        self.repository = BrandRepository()

    def create(self, db: Session, *, company_id: int, name: str) -> Brand:
        brand = Brand(company_id=company_id, name=name)
        return self.repository.create(db, brand)

    def list(self, db: Session, *, company_id: int) -> list[Brand]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, brand_id: int) -> Optional[Brand]:
        return self.repository.get_by_id(db, brand_id)

    def update(self, db: Session, *, brand: Brand, name: Optional[str] = None) -> Brand:
        if name is not None:
            brand.name = name
        return self.repository.update(db, brand)

    def delete(self, db: Session, *, brand: Brand) -> None:
        self.repository.delete(db, brand)
