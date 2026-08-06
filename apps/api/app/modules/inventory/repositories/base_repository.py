from typing import Optional

from sqlalchemy.orm import Session


class BaseRepository:
    model = None

    def get_by_id(self, db: Session, entity_id: int) -> Optional[object]:
        if self.model is None:
            raise NotImplementedError
        return db.query(self.model).filter(self.model.id == entity_id).first()

    def list(self, db: Session, *, company_id: int) -> list[object]:
        if self.model is None:
            raise NotImplementedError
        return db.query(self.model).filter(self.model.company_id == company_id).order_by(self.model.id.desc()).all()

    def create(self, db: Session, entity: object) -> object:
        db.add(entity)
        db.commit()
        db.refresh(entity)
        return entity

    def update(self, db: Session, entity: object) -> object:
        db.commit()
        db.refresh(entity)
        return entity

    def delete(self, db: Session, entity: object) -> None:
        db.delete(entity)
        db.commit()
