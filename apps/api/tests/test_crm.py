from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.database import Base
from app.models.company import Company
from app.models.user import User
from app.modules.crm.models.lead import Lead
from app.modules.crm.models.contact import Contact
from app.modules.crm.models.deal import Deal
from app.modules.crm.models.stage import Stage
from app.modules.crm.models.activity import Activity
from app.modules.crm.models.note import Note
from app.modules.crm.models.task import Task
from app.modules.crm.services.contact_service import ContactService
from app.modules.crm.services.deal_service import DealService
from app.modules.crm.services.stage_service import StageService
from app.modules.crm.services.lead_service import LeadService
from app.modules.crm.services.dashboard_service import DashboardService


def create_test_session() -> Session:
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    return sessionmaker(bind=engine)()


def test_lead_service_create_and_list() -> None:
    db = create_test_session()
    try:
        company = Company(name="Acme", email="acme@example.com")
        db.add(company)
        db.commit()
        db.refresh(company)

        service = LeadService()
        lead = service.create(
            db,
            company_id=company.id,
            name="Jane Doe",
            email="jane@example.com",
            phone="123456",
            source="Website",
        )

        leads = service.list(db, company_id=company.id)
        assert len(leads) == 1
        assert leads[0].id == lead.id
        assert leads[0].status == "new"
    finally:
        db.close()


def test_dashboard_service_summary() -> None:
    db = create_test_session()
    try:
        company = Company(name="Globex", email="globex@example.com")
        db.add(company)
        db.commit()
        db.refresh(company)

        stage = Stage(company_id=company.id, name="Qualified", position=1)
        db.add(stage)
        db.commit()
        db.refresh(stage)

        lead = Lead(company_id=company.id, name="John", email="john@example.com", source="Referral")
        contact = Contact(company_id=company.id, first_name="John", last_name="Smith", email="john@smith.com")
        deal = Deal(company_id=company.id, title="Expansion", stage_id=stage.id, amount=5000)
        activity = Activity(company_id=company.id, type="call", notes="Follow-up")
        note = Note(company_id=company.id, content="Great opportunity")
        task = Task(company_id=company.id, title="Send proposal", completed=False)
        db.add_all([lead, contact, deal, activity, note, task])
        db.commit()

        summary = DashboardService().get_summary(db, company_id=company.id)
        assert summary["leads"] == 1
        assert summary["contacts"] == 1
        assert summary["deals"] == 1
        assert summary["activities"] == 1
        assert summary["tasks"] == 1
        assert summary["notes"] == 1
    finally:
        db.close()


def test_contact_and_deal_services() -> None:
    db = create_test_session()
    try:
        company = Company(name="Initech", email="initech@example.com")
        db.add(company)
        db.commit()
        db.refresh(company)

        stage_service = StageService()
        stage = stage_service.create(db, company_id=company.id, name="Discovery", position=1)

        contact_service = ContactService()
        contact = contact_service.create(
            db,
            company_id=company.id,
            first_name="Ada",
            last_name="Lovelace",
            email="ada@example.com",
            phone="555-0000",
        )

        deal_service = DealService()
        deal = deal_service.create(
            db,
            company_id=company.id,
            title="New partnership",
            stage_id=stage.id,
            amount=12000,
            description="Strategic deal",
        )

        fetched_deals = deal_service.list(db, company_id=company.id)
        assert len(fetched_deals) == 1
        assert fetched_deals[0].id == deal.id
        assert contact.first_name == "Ada"
    finally:
        db.close()
