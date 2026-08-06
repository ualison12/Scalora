from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.ai.schemas.tool import ToolCreate, ToolResponse
from app.modules.ai.services.ai_service import AIService

router = APIRouter(prefix="/ai/tools", tags=["AI Tools"])
service = AIService()


@router.post("", response_model=ToolResponse)
def create_tool(data: ToolCreate, db: Session = Depends(get_db)) -> ToolResponse:
    return service.create_tool(db, company_id=data.company_id, name=data.name, tool_type=data.tool_type)
