from pydantic import BaseModel, ConfigDict


class PromptTemplateCreate(BaseModel):
    company_id: int
    name: str
    template: str


class PromptTemplateResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    name: str
    template: str
