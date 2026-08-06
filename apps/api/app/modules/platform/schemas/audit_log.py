from pydantic import BaseModel, ConfigDict


class PlatformLogCreate(BaseModel):
    company_id: int
    level: str
    message: str


class PlatformLogResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    level: str
    message: str
