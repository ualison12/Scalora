from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.platform.schemas.sdk_key import SDKKeyCreate, SDKKeyResponse
from app.modules.platform.services.platform_service import PlatformService

router = APIRouter(prefix="/platform/sdk", tags=["Platform SDK"])
service = PlatformService()


@router.post("", response_model=SDKKeyResponse)
def create_sdk_key(data: SDKKeyCreate, db: Session = Depends(get_db)) -> SDKKeyResponse:
    return service.create_sdk_key(db, company_id=data.company_id, name=data.name, key=data.key)
