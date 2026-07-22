from datetime import date

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.database import Base
from app.models.company import Company
from app.modules.finance.services import (
    BoletoService,
    CategoryService,
    CostCenterService,
    DashboardService,
    DreService,
    PayableService,
    PixService,
    ReceivableService,
)


def create_test_session() -> Session:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)()


def test_finance_services_workflow() -> None:
    db = create_test_session()
    try:
        company = Company(name="Acme Finance", email="finance@example.com")
        db.add(company)
        db.commit()
        db.refresh(company)

        category_service = CategoryService()
        category = category_service.create(db, company_id=company.id, name="Software", kind="expense")

        cost_center_service = CostCenterService()
        cost_center = cost_center_service.create(db, company_id=company.id, name="TI", code="TI-01")

        payable_service = PayableService()
        payable = payable_service.create(
            db,
            company_id=company.id,
            category_id=category.id,
            cost_center_id=cost_center.id,
            description="Hosting mensal",
            amount=150.0,
            due_date=date(2026, 7, 25),
        )

        receivable_service = ReceivableService()
        receivable = receivable_service.create(
            db,
            company_id=company.id,
            category_id=category.id,
            cost_center_id=cost_center.id,
            description="Projeto consultoria",
            amount=500.0,
            due_date=date(2026, 7, 30),
        )

        pix_service = PixService()
        pix = pix_service.create(
            db,
            company_id=company.id,
            transaction_id=receivable.id,
            amount=500.0,
            code="PIX-001",
        )

        boleto_service = BoletoService()
        boleto = boleto_service.create(
            db,
            company_id=company.id,
            transaction_id=payable.id,
            amount=150.0,
            code="BOLETO-001",
        )

        payable_service.mark_paid(db, transaction_id=payable.id)
        receivable_service.mark_received(db, transaction_id=receivable.id)
        pix_service.mark_paid(db, document_id=pix.id)
        boleto_service.mark_paid(db, document_id=boleto.id)

        dashboard = DashboardService().get_summary(db, company_id=company.id)
        assert dashboard["cash_inflow"] == 500.0
        assert dashboard["cash_outflow"] == 150.0
        assert dashboard["pending_receivables"] == 0
        assert dashboard["pending_payables"] == 0

        dre = DreService().get_summary(db, company_id=company.id)
        assert dre["income_total"] == 500.0
        assert dre["expense_total"] == 150.0
        assert dre["net_result"] == 350.0
    finally:
        db.close()
