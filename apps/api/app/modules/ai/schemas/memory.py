from pydantic import BaseModel, ConfigDict


class MemoryCreate(BaseModel):
    company_id: int
    agent_id: int | None = None
    content: str
    kind: str = "memory"


class MemoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    agent_id: int | None = None
    content: str
    kind: str
