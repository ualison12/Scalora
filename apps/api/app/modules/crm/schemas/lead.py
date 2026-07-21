from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class LeadCreate(BaseModel):
    company_id: int
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    source: Optional[str] = None


class LeadUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    source: Optional[str] = None
    status: Optional[str] = None


class LeadResponse(BaseModel):
    id: int
    company_id: int
    name: str
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    source: Optional[str] = None
    status: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
