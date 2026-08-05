from sqlalchemy import func
from sqlalchemy.orm import Session

from app.modules.finance.models.payable import Payable
from app.modules.finance.models.receivable import Receivable


class DashboardService:
    def get_summary(self, db: Session, *, company_id: int) -> dict[str, float | int]:
        cash_inflow = db.query(func.coalesce(func.sum(Receivable.amount), 0.0)).filter(
            Receivable.company_id == company_id,
            Receivable.status == "received",
        ).scalar() or 0.0

        cash_outflow = db.query(func.coalesce(func.sum(Payable.amount), 0.0)).filter(
            Payable.company_id == company_id,
            Payable.status == "paid",
        ).scalar() or 0.0

        pending_receivables = db.query(Receivable).filter(
            Receivable.company_id == company_id,
            Receivable.status != "received",
        ).count()

        pending_payables = db.query(Payable).filter(
            Payable.company_id == company_id,
            Payable.status != "paid",
        ).count()

        return {
            "cash_inflow": float(cash_inflow),
            "cash_outflow": float(cash_outflow),
            "pending_receivables": pending_receivables,
            "pending_payables": pending_payables,
        }
