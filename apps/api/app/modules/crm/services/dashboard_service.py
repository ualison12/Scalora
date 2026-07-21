from sqlalchemy.orm import Session

from app.modules.crm.models.activity import Activity
from app.modules.crm.models.contact import Contact
from app.modules.crm.models.deal import Deal
from app.modules.crm.models.lead import Lead
from app.modules.crm.models.note import Note
from app.modules.crm.models.stage import Stage
from app.modules.crm.models.task import Task


class DashboardService:
    def get_summary(self, db: Session, *, company_id: int) -> dict[str, int]:
        return {
            "leads": db.query(Lead).filter(Lead.company_id == company_id).count(),
            "contacts": db.query(Contact).filter(Contact.company_id == company_id).count(),
            "deals": db.query(Deal).filter(Deal.company_id == company_id).count(),
            "stages": db.query(Stage).filter(Stage.company_id == company_id).count(),
            "activities": db.query(Activity).filter(Activity.company_id == company_id).count(),
            "notes": db.query(Note).filter(Note.company_id == company_id).count(),
            "tasks": db.query(Task).filter(Task.company_id == company_id).count(),
        }
