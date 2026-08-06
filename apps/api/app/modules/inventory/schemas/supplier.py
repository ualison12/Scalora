from pydantic import BaseModel, ConfigDict


class SupplierCreate(BaseModel):
    company_id: int
    name: str
    contact_name: str | None = None
    email: str | None = None


class SupplierUpdate(BaseModel):
    name: str | None = None
    contact_name: str | None = None
    email: str | None = None


class SupplierResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    name: str
    contact_name: str | None = None
    email: str | None = None
