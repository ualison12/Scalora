from pydantic import BaseModel, ConfigDict


class BoletoCreate(BaseModel):
    transaction_id: int | None = None
    amount: float
    code: str


class BoletoUpdate(BaseModel):
    amount: float | None = None
    code: str | None = None


class BoletoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    transaction_id: int | None = None
    amount: float
    code: str
    status: str
