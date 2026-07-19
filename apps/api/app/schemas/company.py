from datetime import datetime

from pydantic import BaseModel


class CompanyCreate(BaseModel):

    name: str

    email: str



class CompanyResponse(BaseModel):

    id: int

    name: str

    email: str

    created_at: datetime


    class Config:

        from_attributes = True