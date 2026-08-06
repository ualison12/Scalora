from pydantic import BaseModel, ConfigDict


class BackupCreate(BaseModel):
    company_id: int
    name: str
    status: str


class BackupResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    name: str
    status: str
