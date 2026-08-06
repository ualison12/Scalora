from pydantic import BaseModel, ConfigDict


class SDKKeyCreate(BaseModel):
    company_id: int
    name: str
    key: str


class SDKKeyResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    name: str
    key: str
