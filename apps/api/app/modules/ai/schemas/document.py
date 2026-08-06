from pydantic import BaseModel, ConfigDict


class DocumentCreate(BaseModel):
    company_id: int
    title: str
    content: str
    source: str


class DocumentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    title: str
    content: str
    source: str
