from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.database import Base
from app.models.company import Company
from app.modules.platform.services.platform_service import PlatformService


def create_test_session() -> Session:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)()


def test_platform_services_workflow() -> None:
    db = create_test_session()
    try:
        company = Company(name="Acme Platform", email="platform@example.com")
        db.add(company)
        db.commit()
        db.refresh(company)

        service = PlatformService()
        plan = service.create_plan(db, company_id=company.id, name="Enterprise", price=299.0, billing_period="monthly")
        subscription = service.create_subscription(db, company_id=company.id, plan_id=plan.id, status="active")
        billing = service.create_billing_event(db, company_id=company.id, subscription_id=subscription.id, amount=299.0, status="paid")
        webhook = service.create_webhook(db, company_id=company.id, name="Invoice Paid", endpoint="https://example.com/webhook")
        sdk = service.create_sdk_key(db, company_id=company.id, name="Mobile SDK", key="sdk-demo")
        admin = service.create_admin_user(db, company_id=company.id, username="admin", role="owner")
        log = service.create_log_entry(db, company_id=company.id, level="info", message="Deploy realizado")
        backup = service.create_backup(db, company_id=company.id, name="nightly", status="completed")
        deployment = service.create_deployment(db, company_id=company.id, environment="prod", version="1.2.3")
        dashboard = service.get_dashboard(db, company_id=company.id)

        assert plan.name == "Enterprise"
        assert subscription.status == "active"
        assert billing.status == "paid"
        assert webhook.name == "Invoice Paid"
        assert sdk.name == "Mobile SDK"
        assert admin.username == "admin"
        assert log.message == "Deploy realizado"
        assert backup.status == "completed"
        assert deployment.version == "1.2.3"
        assert dashboard["plans_count"] == 1
        assert dashboard["active_subscriptions"] == 1
        assert dashboard["webhooks_count"] == 1
    finally:
        db.close()
