from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class StageCreate(BaseModel):
    company_id: int
    name: str
    position: int = 0


class StageUpdate(BaseModel):
    name: Optional[str] = None
    position: Optional[int] = None


class StageResponse(BaseModel):
    id: int
    company_id: int
    name: str
    position: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
