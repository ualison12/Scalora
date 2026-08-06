from pydantic import BaseModel, ConfigDict


class WebhookCreate(BaseModel):
    company_id: int
    name: str
    endpoint: str


class WebhookResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    name: str
    endpoint: str
