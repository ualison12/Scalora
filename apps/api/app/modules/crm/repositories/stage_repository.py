from typing import Optional

from sqlalchemy.orm import Session

from app.modules.crm.models.stage import Stage


class StageRepository:
    def get_by_id(self, db: Session, stage_id: int) -> Optional[Stage]:
        return db.query(Stage).filter(Stage.id == stage_id).first()

    def list(self, db: Session, *, company_id: int) -> list[Stage]:
        return db.query(Stage).filter(Stage.company_id == company_id).order_by(Stage.position.asc(), Stage.id.asc()).all()

    def create(self, db: Session, stage: Stage) -> Stage:
        db.add(stage)
        db.commit()
        db.refresh(stage)
        return stage

    def update(self, db: Session, stage: Stage) -> Stage:
        db.commit()
        db.refresh(stage)
        return stage

    def delete(self, db: Session, stage: Stage) -> None:
        db.delete(stage)
        db.commit()
