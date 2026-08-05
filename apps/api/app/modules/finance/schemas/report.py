from datetime import date

from pydantic import BaseModel, ConfigDict


class TransactionResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    kind: str
    company_id: int
    category_id: int | None = None
    cost_center_id: int | None = None
    description: str
    amount: float
    due_date: date
    status: str


class DreSummaryResponse(BaseModel):
    income_total: float
    expense_total: float
    net_result: float


class FinanceDashboardResponse(BaseModel):
    cash_inflow: float
    cash_outflow: float
    pending_receivables: int
    pending_payables: int


class FinanceReportResponse(BaseModel):
    company_id: int
    kind: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    category_id: int | None = None
    cost_center_id: int | None = None
    payables_total: float
    receivables_total: float
    payables_count: int
    receivables_count: int
    transactions: list[TransactionResponse]
