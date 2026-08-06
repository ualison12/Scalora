from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database import Base


class AIMemory(Base):
    __tablename__ = "ai_memories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    company_id: Mapped[int] = mapped_column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    agent_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("ai_agents.id"), nullable=True)
    content: Mapped[str] = mapped_column(String(2000), nullable=False)
    kind: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    company = relationship("Company")
    agent = relationship("AIAgent")
