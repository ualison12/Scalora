from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.platform.schemas.deployment import DeploymentCreate, DeploymentResponse
from app.modules.platform.services.platform_service import PlatformService

router = APIRouter(prefix="/platform/deploy", tags=["Platform Deploy"])
service = PlatformService()


@router.post("", response_model=DeploymentResponse)
def create_deployment(data: DeploymentCreate, db: Session = Depends(get_db)) -> DeploymentResponse:
    return service.create_deployment(db, company_id=data.company_id, environment=data.environment, version=data.version)
