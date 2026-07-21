from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.crm.schemas.stage import StageCreate, StageResponse, StageUpdate
from app.modules.crm.services.stage_service import StageService

router = APIRouter(prefix="/crm/stages", tags=["CRM Stages"])
service = StageService()


@router.post("", response_model=StageResponse)
def create_stage(data: StageCreate, db: Session = Depends(get_db)) -> StageResponse:
    return service.create(db, company_id=data.company_id, name=data.name, position=data.position)


@router.get("", response_model=list[StageResponse])
def list_stages(company_id: int = Query(...), db: Session = Depends(get_db)) -> list[StageResponse]:
    return service.list(db, company_id=company_id)


@router.get("/{stage_id}", response_model=StageResponse)
def get_stage(stage_id: int, db: Session = Depends(get_db)) -> StageResponse:
    stage = service.get(db, stage_id=stage_id)
    if not stage:
        raise HTTPException(status_code=404, detail="Stage not found")
    return stage


@router.put("/{stage_id}", response_model=StageResponse)
def update_stage(stage_id: int, data: StageUpdate, db: Session = Depends(get_db)) -> StageResponse:
    stage = service.get(db, stage_id=stage_id)
    if not stage:
        raise HTTPException(status_code=404, detail="Stage not found")
    return service.update(db, stage=stage, name=data.name, position=data.position)


@router.delete("/{stage_id}")
def delete_stage(stage_id: int, db: Session = Depends(get_db)) -> dict[str, bool]:
    stage = service.get(db, stage_id=stage_id)
    if not stage:
        raise HTTPException(status_code=404, detail="Stage not found")
    service.delete(db, stage=stage)
    return {"success": True}
