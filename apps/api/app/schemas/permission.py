from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class PermissionCreate(BaseModel):
    name: str
    description: Optional[str] = None


class PermissionResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
