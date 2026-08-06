from pydantic import BaseModel, ConfigDict


class MovementCreate(BaseModel):
    company_id: int
    product_id: int
    lot_id: int | None = None
    movement_type: str
    quantity: int = 0
    unit_cost: float = 0
    reason: str | None = None


class MovementUpdate(BaseModel):
    movement_type: str | None = None
    quantity: int | None = None
    unit_cost: float | None = None
    reason: str | None = None


class MovementResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company_id: int
    product_id: int
    lot_id: int | None = None
    movement_type: str
    quantity: int
    unit_cost: float
    reason: str | None = None
