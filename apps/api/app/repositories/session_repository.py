from typing import Optional

from sqlalchemy.orm import Session

from app.models.session import Session


class SessionRepository:
    def get_by_token(self, db: Session, token: str) -> Optional[Session]:
        return db.query(Session).filter(Session.token == token).first()

    def create(self, db: Session, session: Session) -> Session:
        db.add(session)
        db.commit()
        db.refresh(session)
        return session

    def update(self, db: Session, session: Session) -> Session:
        db.commit()
        db.refresh(session)
        return session
