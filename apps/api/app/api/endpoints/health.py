from fastapi import APIRouter

router = APIRouter()

@router.get(
    "/health",
    tags=["Health"],
    summary="Health Check",
)
async def health():
    return {
        "status": "ok",
        "service": "Scalora API",
        "version": "0.1.0",
    }