from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.database import Base
from app.models.company import Company
from app.modules.inventory.services import (
    BrandService,
    CategoryService,
    InventoryDashboardService,
    LotService,
    MovementService,
    ProductService,
    SupplierService,
)


def create_test_session() -> Session:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)()


def test_inventory_services_workflow() -> None:
    db = create_test_session()
    try:
        company = Company(name="Acme Inventory", email="inventory@example.com")
        db.add(company)
        db.commit()
        db.refresh(company)

        category = CategoryService().create(db, company_id=company.id, name="Eletrônicos")
        brand = BrandService().create(db, company_id=company.id, name="TechCorp")
        supplier = SupplierService().create(
            db,
            company_id=company.id,
            name="Fornecedor Tech",
            contact_name="Ana",
            email="ana@example.com",
        )

        product = ProductService().create(
            db,
            company_id=company.id,
            category_id=category.id,
            brand_id=brand.id,
            supplier_id=supplier.id,
            name="Notebook",
            sku="SKU-001",
            barcode="789000000001",
            cost_price=2500.0,
            sale_price=3200.0,
            min_stock=2,
        )

        lot = LotService().create(
            db,
            company_id=company.id,
            product_id=product.id,
            code="LOT-001",
            quantity=10,
            expiration_date=date(2026, 12, 31),
        )

        MovementService().create(
            db,
            company_id=company.id,
            product_id=product.id,
            lot_id=lot.id,
            movement_type="in",
            quantity=10,
            unit_cost=2500.0,
            reason="Entrada inicial",
        )

        dashboard = InventoryDashboardService().get_summary(db, company_id=company.id)
        assert dashboard["total_products"] == 1
        assert dashboard["total_stock"] == 10
        assert dashboard["low_stock_products"] == 0
    finally:
        db.close()
