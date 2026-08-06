from pydantic import BaseModel, ConfigDict


class ToolCreate(BaseModel):
    company_id: int
    name: str
    tool_type: str


class ToolResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    name: str
    tool_type: str
