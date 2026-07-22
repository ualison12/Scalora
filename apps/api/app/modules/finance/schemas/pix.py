from pydantic import BaseModel, ConfigDict


class PixCreate(BaseModel):
    transaction_id: int | None = None
    amount: float
    code: str


class PixUpdate(BaseModel):
    amount: float | None = None
    code: str | None = None


class PixResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    transaction_id: int | None = None
    amount: float
    code: str
    status: str
