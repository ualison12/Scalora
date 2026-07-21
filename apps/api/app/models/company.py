from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Company(Base):

    __tablename__ = "companies"


    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )


    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )


    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    users: Mapped[list["User"]] = relationship(
        "User",
        back_populates="company",
        cascade="all, delete-orphan",
    )
    audit_logs: Mapped[list["AuditLog"]] = relationship(
        "AuditLog",
        back_populates="company",
        cascade="all, delete-orphan",
    )