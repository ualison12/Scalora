from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from app.database import Base


class Product(Base):
    __tablename__ = "inventory_products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    company_id: Mapped[int] = mapped_column(Integer, ForeignKey("companies.id"), nullable=False, index=True)
    category_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("inventory_categories.id"), nullable=True)
    brand_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("inventory_brands.id"), nullable=True)
    supplier_id: Mapped[int | None] = mapped_column(Integer, ForeignKey("inventory_suppliers.id"), nullable=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    sku: Mapped[str | None] = mapped_column(String(100), nullable=True)
    barcode: Mapped[str | None] = mapped_column(String(100), nullable=True)
    cost_price: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False, default=0)
    sale_price: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False, default=0)
    min_stock: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    company = relationship("Company")
    category = relationship("InventoryCategory")
    brand = relationship("Brand")
    supplier = relationship("Supplier")
