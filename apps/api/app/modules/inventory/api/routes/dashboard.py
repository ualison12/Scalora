from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.inventory.services.dashboard_service import InventoryDashboardService

router = APIRouter(prefix="/inventory/dashboard", tags=["Inventory Dashboard"])
service = InventoryDashboardService()


@router.get("")
def get_dashboard(company_id: int, db: Session = Depends(get_db)) -> dict[str, int | float]:
    return service.get_summary(db, company_id=company_id)
