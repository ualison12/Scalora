from pydantic import BaseModel, ConfigDict


class BrandCreate(BaseModel):
    company_id: int
    name: str


class BrandUpdate(BaseModel):
    name: str | None = None


class BrandResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    name: str
