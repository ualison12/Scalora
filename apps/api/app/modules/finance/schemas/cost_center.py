from pydantic import BaseModel, ConfigDict


class CostCenterCreate(BaseModel):
    name: str
    code: str


class CostCenterUpdate(BaseModel):
    name: str | None = None
    code: str | None = None


class CostCenterResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    name: str
    code: str
