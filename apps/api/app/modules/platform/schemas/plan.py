from pydantic import BaseModel, ConfigDict


class PlanCreate(BaseModel):
    company_id: int
    name: str
    price: float
    billing_period: str


class PlanResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    name: str
    price: float
    billing_period: str
