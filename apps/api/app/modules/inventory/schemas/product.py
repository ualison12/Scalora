from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    company_id: int
    category_id: int | None = None
    brand_id: int | None = None
    supplier_id: int | None = None
    name: str
    sku: str | None = None
    barcode: str | None = None
    cost_price: float = 0
    sale_price: float = 0
    min_stock: int = 0


class ProductUpdate(BaseModel):
    name: str | None = None
    sku: str | None = None
    barcode: str | None = None
    cost_price: float | None = None
    sale_price: float | None = None
    min_stock: int | None = None


class ProductResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    category_id: int | None = None
    brand_id: int | None = None
    supplier_id: int | None = None
    name: str
    sku: str | None = None
    barcode: str | None = None
    cost_price: float
    sale_price: float
    min_stock: int
