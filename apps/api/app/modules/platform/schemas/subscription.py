from pydantic import BaseModel, ConfigDict


class SubscriptionCreate(BaseModel):
    company_id: int
    plan_id: int
    status: str


class SubscriptionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    plan_id: int
    status: str
