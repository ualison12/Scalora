from pydantic import BaseModel, ConfigDict


class BillingEventCreate(BaseModel):
    company_id: int
    subscription_id: int
    amount: float
    status: str


class BillingEventResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    subscription_id: int
    amount: float
    status: str
