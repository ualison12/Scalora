from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class DealCreate(BaseModel):
    company_id: int
    title: str
    description: Optional[str] = None
    amount: float = 0.0
    stage_id: Optional[int] = None


class DealUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    amount: Optional[float] = None
    stage_id: Optional[int] = None
    status: Optional[str] = None


class DealResponse(BaseModel):
    id: int
    company_id: int
    stage_id: Optional[int] = None
    title: str
    description: Optional[str] = None
    amount: float
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
