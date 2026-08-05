from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.finance.schemas.cost_center import CostCenterCreate, CostCenterResponse, CostCenterUpdate
from app.modules.finance.services.cost_center_service import CostCenterService

router = APIRouter(prefix="/finance/cost-centers", tags=["Finance Cost Centers"])
service = CostCenterService()


@router.post("", response_model=CostCenterResponse)
def create_cost_center(data: CostCenterCreate, db: Session = Depends(get_db)) -> CostCenterResponse:
    return service.create(db, company_id=data.company_id, name=data.name, code=data.code)


@router.get("", response_model=list[CostCenterResponse])
def list_cost_centers(company_id: int, db: Session = Depends(get_db)) -> list[CostCenterResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{cost_center_id}", response_model=CostCenterResponse)
def get_cost_center(cost_center_id: int, db: Session = Depends(get_db)) -> CostCenterResponse:
    cost_center = service.get(db, cost_center_id=cost_center_id)
    if not cost_center:
        raise HTTPException(status_code=404, detail="Cost center not found")
    return cost_center


@router.put("/{cost_center_id}", response_model=CostCenterResponse)
def update_cost_center(cost_center_id: int, data: CostCenterUpdate, db: Session = Depends(get_db)) -> CostCenterResponse:
    cost_center = service.get(db, cost_center_id=cost_center_id)
    if not cost_center:
        raise HTTPException(status_code=404, detail="Cost center not found")
    return service.update(db, cost_center=cost_center, name=data.name, code=data.code)


@router.delete("/{cost_center_id}")
def delete_cost_center(cost_center_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    cost_center = service.get(db, cost_center_id=cost_center_id)
    if not cost_center:
        raise HTTPException(status_code=404, detail="Cost center not found")
    service.delete(db, cost_center=cost_center)
    return {"success": True}
