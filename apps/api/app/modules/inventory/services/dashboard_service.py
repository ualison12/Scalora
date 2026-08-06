from sqlalchemy.orm import Session

from app.modules.inventory.models.product import Product
from app.modules.inventory.models.lot import Lot
from app.modules.inventory.models.movement import Movement


class InventoryDashboardService:
    def get_summary(self, db: Session, *, company_id: int) -> dict[str, int | float]:
        products = db.query(Product).filter(Product.company_id == company_id).all()
        lots = db.query(Lot).filter(Lot.company_id == company_id).all()
        movements = db.query(Movement).filter(Movement.company_id == company_id).all()

        total_stock = sum(lot.quantity for lot in lots)
        total_products = len(products)
        low_stock_products = sum(1 for product in products if product.min_stock and product.min_stock >= total_stock)

        return {
            "total_products": total_products,
            "total_stock": total_stock,
            "low_stock_products": low_stock_products,
            "total_movements": len(movements),
        }
