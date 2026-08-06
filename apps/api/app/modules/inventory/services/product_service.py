from typing import Optional

from sqlalchemy.orm import Session

from app.modules.inventory.models.product import Product
from app.modules.inventory.repositories.product_repository import ProductRepository


class ProductService:
    def __init__(self) -> None:
        self.repository = ProductRepository()

    def create(
        self,
        db: Session,
        *,
        company_id: int,
        category_id: Optional[int] = None,
        brand_id: Optional[int] = None,
        supplier_id: Optional[int] = None,
        name: str,
        sku: Optional[str] = None,
        barcode: Optional[str] = None,
        cost_price: float = 0,
        sale_price: float = 0,
        min_stock: int = 0,
    ) -> Product:
        product = Product(
            company_id=company_id,
            category_id=category_id,
            brand_id=brand_id,
            supplier_id=supplier_id,
            name=name,
            sku=sku,
            barcode=barcode,
            cost_price=cost_price,
            sale_price=sale_price,
            min_stock=min_stock,
        )
        return self.repository.create(db, product)

    def list(self, db: Session, *, company_id: int) -> list[Product]:
        return self.repository.list(db, company_id=company_id)

    def get(self, db: Session, *, product_id: int) -> Optional[Product]:
        return self.repository.get_by_id(db, product_id)

    def update(
        self,
        db: Session,
        *,
        product: Product,
        name: Optional[str] = None,
        sku: Optional[str] = None,
        barcode: Optional[str] = None,
        cost_price: Optional[float] = None,
        sale_price: Optional[float] = None,
        min_stock: Optional[int] = None,
    ) -> Product:
        if name is not None:
            product.name = name
        if sku is not None:
            product.sku = sku
        if barcode is not None:
            product.barcode = barcode
        if cost_price is not None:
            product.cost_price = cost_price
        if sale_price is not None:
            product.sale_price = sale_price
        if min_stock is not None:
            product.min_stock = min_stock
        return self.repository.update(db, product)

    def delete(self, db: Session, *, product: Product) -> None:
        self.repository.delete(db, product)
