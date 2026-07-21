from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr


# Schema para CRIAÇÃO de empresa (dados obrigatórios)
class CompanyCreate(BaseModel):
    name: str
    email: EmailStr


# Schema para ATUALIZAÇÃO de empresa (dados opcionais)
class CompanyUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None


# Schema para RESPOSTA da API
class CompanyResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)