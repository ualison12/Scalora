from pydantic import BaseModel, ConfigDict


class AutomationCreate(BaseModel):
    company_id: int
    name: str
    trigger: str
    action: str


class AutomationResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    name: str
    trigger: str
    action: str
