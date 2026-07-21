from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class RoleCreate(BaseModel):
    name: str
    description: Optional[str] = None


class RoleResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    is_system: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
