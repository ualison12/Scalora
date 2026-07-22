from pydantic import BaseModel, ConfigDict


class CategoryCreate(BaseModel):
    name: str
    kind: str = "expense"


class CategoryUpdate(BaseModel):
    name: str | None = None
    kind: str | None = None


class CategoryResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    name: str
    kind: str
