from pydantic import BaseModel, ConfigDict


class ProviderCreate(BaseModel):
    company_id: int
    provider_name: str
    api_key: str
    model_name: str
    enabled: bool = True


class ProviderResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    provider_name: str
    model_name: str
    enabled: bool
