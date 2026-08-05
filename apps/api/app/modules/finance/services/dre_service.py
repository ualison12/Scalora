from sqlalchemy import func
from sqlalchemy.orm import Session

from app.modules.finance.models.payable import Payable
from app.modules.finance.models.receivable import Receivable


class DreService:
    def get_summary(self, db: Session, *, company_id: int) -> dict[str, float]:
        income_total = db.query(func.coalesce(func.sum(Receivable.amount), 0.0)).filter(
            Receivable.company_id == company_id,
            Receivable.status == "received",
        ).scalar() or 0.0

        expense_total = db.query(func.coalesce(func.sum(Payable.amount), 0.0)).filter(
            Payable.company_id == company_id,
            Payable.status == "paid",
        ).scalar() or 0.0

        return {
            "income_total": float(income_total),
            "expense_total": float(expense_total),
            "net_result": float(income_total) - float(expense_total),
        }
