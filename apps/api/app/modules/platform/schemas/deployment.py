from pydantic import BaseModel, ConfigDict


class DeploymentCreate(BaseModel):
    company_id: int
    environment: str
    version: str


class DeploymentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    environment: str
    version: str
