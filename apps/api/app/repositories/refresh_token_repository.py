from typing import Optional

from sqlalchemy.orm import Session

from app.models.refresh_token import RefreshToken


class RefreshTokenRepository:
    def get_by_token(self, db: Session, token: str) -> Optional[RefreshToken]:
        return db.query(RefreshToken).filter(RefreshToken.token == token).first()

    def create(self, db: Session, refresh_token: RefreshToken) -> RefreshToken:
        db.add(refresh_token)
        db.commit()
        db.refresh(refresh_token)
        return refresh_token

    def update(self, db: Session, refresh_token: RefreshToken) -> RefreshToken:
        db.commit()
        db.refresh(refresh_token)
        return refresh_token
