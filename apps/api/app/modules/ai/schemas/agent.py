from pydantic import BaseModel, ConfigDict


class AgentCreate(BaseModel):
    company_id: int
    name: str
    provider: str
    model: str


class AgentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    name: str
    provider: str
    model: str
