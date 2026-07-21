from typing import Optional

from sqlalchemy.orm import Session

from app.modules.crm.models.stage import Stage
from app.modules.crm.repositories.stage_repository import StageRepository


class StageService:
    def __init__(self) -> None:
        self.repository = StageRepository()

    def create(
        self,
        db: Session,
        *,
        company_id: int,
        name: str,
        position: int = 0,
    ) -> Stage:
        stage = Stage(company_id=company_id, name=name, position=position)
        return self.repository.create(db, stage)

    def list(self, db: Session, *, company_id: int) -> list[Stage]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, stage_id: int) -> Optional[Stage]:
        return self.repository.get_by_id(db, stage_id)

    def update(
        self,
        db: Session,
        *,
        stage: Stage,
        name: Optional[str] = None,
        position: Optional[int] = None,
    ) -> Stage:
        if name is not None:
            stage.name = name
        if position is not None:
            stage.position = position
        return self.repository.update(db, stage)

    def delete(self, db: Session, *, stage: Stage) -> None:
        self.repository.delete(db, stage)
