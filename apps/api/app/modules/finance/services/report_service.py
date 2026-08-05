from datetime import date

from sqlalchemy import func, or_
from sqlalchemy.orm import Session

from app.modules.finance.models.payable import Payable
from app.modules.finance.models.receivable import Receivable


class ReportService:
    def get_finance_report(
        self,
        db: Session,
        *,
        company_id: int,
        kind: str | None = None,
        start_date: date | None = None,
        end_date: date | None = None,
        category_id: int | None = None,
        cost_center_id: int | None = None,
    ) -> dict[str, object]:
        payables = db.query(Payable).filter(Payable.company_id == company_id)
        receivables = db.query(Receivable).filter(Receivable.company_id == company_id)

        if kind in ("expense", "payable"):
            receivables = receivables.filter(Receivable.id == None)
        elif kind in ("income", "receivable"):
            payables = payables.filter(Payable.id == None)

        if start_date:
            payables = payables.filter(Payable.due_date >= start_date)
            receivables = receivables.filter(Receivable.due_date >= start_date)

        if end_date:
            payables = payables.filter(Payable.due_date <= end_date)
            receivables = receivables.filter(Receivable.due_date <= end_date)

        if category_id:
            payables = payables.filter(Payable.category_id == category_id)
            receivables = receivables.filter(Receivable.category_id == category_id)

        if cost_center_id:
            payables = payables.filter(Payable.cost_center_id == cost_center_id)
            receivables = receivables.filter(Receivable.cost_center_id == cost_center_id)

        total_payables = float(payables.with_entities(func.coalesce(func.sum(Payable.amount), 0.0)).scalar() or 0.0)
        total_receivables = float(receivables.with_entities(func.coalesce(func.sum(Receivable.amount), 0.0)).scalar() or 0.0)
        count_payables = payables.count()
        count_receivables = receivables.count()

        transactions = [
            *[
                {
                    "id": payable.id,
                    "kind": "payable",
                    "company_id": payable.company_id,
                    "category_id": payable.category_id,
                    "cost_center_id": payable.cost_center_id,
                    "description": payable.description,
                    "amount": payable.amount,
                    "due_date": payable.due_date,
                    "status": payable.status,
                }
                for payable in payables.order_by(Payable.due_date.asc()).all()
            ],
            *[
                {
                    "id": receivable.id,
                    "kind": "receivable",
                    "company_id": receivable.company_id,
                    "category_id": receivable.category_id,
                    "cost_center_id": receivable.cost_center_id,
                    "description": receivable.description,
                    "amount": receivable.amount,
                    "due_date": receivable.due_date,
                    "status": receivable.status,
                }
                for receivable in receivables.order_by(Receivable.due_date.asc()).all()
            ],
        ]

        return {
            "company_id": company_id,
            "kind": kind,
            "start_date": start_date,
            "end_date": end_date,
            "category_id": category_id,
            "cost_center_id": cost_center_id,
            "payables_total": total_payables,
            "receivables_total": total_receivables,
            "payables_count": count_payables,
            "receivables_count": count_receivables,
            "transactions": transactions,
        }
