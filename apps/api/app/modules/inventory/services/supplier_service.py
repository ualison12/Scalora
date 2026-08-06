from typing import Optional

from sqlalchemy.orm import Session

from app.modules.inventory.models.supplier import Supplier
from app.modules.inventory.repositories.supplier_repository import SupplierRepository


class SupplierService:
    def __init__(self) -> None:
        self.repository = SupplierRepository()

    def create(
        self,
        db: Session,
        *,
        company_id: int,
        name: str,
        contact_name: Optional[str] = None,
        email: Optional[str] = None,
    ) -> Supplier:
        supplier = Supplier(company_id=company_id, name=name, contact_name=contact_name, email=email)
        return self.repository.create(db, supplier)

    def list(self, db: Session, *, company_id: int) -> list[Supplier]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, supplier_id: int) -> Optional[Supplier]:
        return self.repository.get_by_id(db, supplier_id)

    def update(
        self,
        db: Session,
        *,
        supplier: Supplier,
        name: Optional[str] = None,
        contact_name: Optional[str] = None,
        email: Optional[str] = None,
    ) -> Supplier:
        if name is not None:
            supplier.name = name
        if contact_name is not None:
            supplier.contact_name = contact_name
        if email is not None:
            supplier.email = email
        return self.repository.update(db, supplier)

    def delete(self, db: Session, *, supplier: Supplier) -> None:
        self.repository.delete(db, supplier)
