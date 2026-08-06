from pydantic import BaseModel, ConfigDict


class AdminUserCreate(BaseModel):
    company_id: int
    username: str
    role: str


class AdminUserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    username: str
    role: str
