from typing import Optional

from sqlalchemy.orm import Session

from app.modules.finance.models.cost_center import CostCenter
from app.modules.finance.repositories.cost_center_repository import CostCenterRepository


class CostCenterService:
    def __init__(self) -> None:
        self.repository = CostCenterRepository()

    def create(self, db: Session, *, company_id: int, name: str, code: str) -> CostCenter:
        cost_center = CostCenter(company_id=company_id, name=name, code=code)
        return self.repository.create(db, cost_center)

    def list(self, db: Session, *, company_id: int) -> list[CostCenter]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, cost_center_id: int) -> Optional[CostCenter]:
        return self.repository.get_by_id(db, cost_center_id)

    def update(self, db: Session, *, cost_center: CostCenter, name: Optional[str] = None, code: Optional[str] = None) -> CostCenter:
        if name is not None:
            cost_center.name = name
        if code is not None:
            cost_center.code = code
        return self.repository.update(db, cost_center)

    def delete(self, db: Session, *, cost_center: CostCenter) -> None:
        self.repository.delete(db, cost_center)
