from datetime import date

from pydantic import BaseModel, ConfigDict


class LotCreate(BaseModel):
    company_id: int
    product_id: int
    code: str
    quantity: int = 0
    expiration_date: date | None = None


class LotUpdate(BaseModel):
    code: str | None = None
    quantity: int | None = None
    expiration_date: date | None = None


class LotResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    product_id: int
    code: str
    quantity: int
    expiration_date: date | None = None
