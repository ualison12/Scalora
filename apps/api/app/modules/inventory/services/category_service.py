from typing import Optional

from sqlalchemy.orm import Session

from app.modules.inventory.models.category import InventoryCategory
from app.modules.inventory.repositories.category_repository import CategoryRepository


class CategoryService:
    def __init__(self) -> None:
        self.repository = CategoryRepository()

    def create(self, db: Session, *, company_id: int, name: str) -> InventoryCategory:
        category = InventoryCategory(company_id=company_id, name=name)
        return self.repository.create(db, category)

    def list(self, db: Session, *, company_id: int) -> list[InventoryCategory]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, category_id: int) -> Optional[InventoryCategory]:
        return self.repository.get_by_id(db, category_id)

    def update(self, db: Session, *, category: InventoryCategory, name: Optional[str] = None) -> InventoryCategory:
        if name is not None:
            category.name = name
        return self.repository.update(db, category)

    def delete(self, db: Session, *, category: InventoryCategory) -> None:
        self.repository.delete(db, category)
