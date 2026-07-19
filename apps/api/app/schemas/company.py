from datetime import datetime
from pydantic import BaseModel, EmailStr, ConfigDict


class CompanyCreate(BaseModel):
    name: str
    email: EmailStr


class CompanyUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


class CompanyResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)