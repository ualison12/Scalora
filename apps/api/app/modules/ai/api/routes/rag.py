from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.modules.ai.schemas.document import DocumentCreate, DocumentResponse
from app.modules.ai.services.ai_service import AIService

router = APIRouter(prefix="/ai/rag", tags=["AI RAG"])
service = AIService()


@router.post("/documents", response_model=DocumentResponse)
def create_document(data: DocumentCreate, db: Session = Depends(get_db)) -> DocumentResponse:
    return service.create_document(db, company_id=data.company_id, title=data.title, content=data.content, source=data.source)
