from typing import Optional

from sqlalchemy.orm import Session

from app.modules.finance.models.category import Category
from app.modules.finance.repositories.category_repository import CategoryRepository


class CategoryService:
    def __init__(self) -> None:
        self.repository = CategoryRepository()

    def create(self, db: Session, *, company_id: int, name: str, kind: str = "expense") -> Category:
        category = Category(company_id=company_id, name=name, kind=kind)
        return self.repository.create(db, category)

    def list(self, db: Session, *, company_id: int) -> list[Category]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, category_id: int) -> Optional[Category]:
        return self.repository.get_by_id(db, category_id)

    def update(self, db: Session, *, category: Category, name: Optional[str] = None, kind: Optional[str] = None) -> Category:
        if name is not None:
            category.name = name
        if kind is not None:
            category.kind = kind
        return self.repository.update(db, category)

    def delete(self, db: Session, *, category: Category) -> None:
        self.repository.delete(db, category)
