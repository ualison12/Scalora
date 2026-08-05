from datetime import date

from pydantic import BaseModel, ConfigDict


class ReceivableCreate(BaseModel):
    company_id: int
    category_id: int | None = None
    cost_center_id: int | None = None
    description: str
    amount: float
    due_date: date


class ReceivableUpdate(BaseModel):
    category_id: int | None = None
    cost_center_id: int | None = None
    description: str | None = None
    amount: float | None = None
    due_date: date | None = None
    status: str | None = None


class ReceivableResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    category_id: int | None = None
    cost_center_id: int | None = None
    description: str
    amount: float
    due_date: date
    status: str
