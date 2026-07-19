from fastapi import FastAPI
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

@app.get("/health", tags=["Health"])
async def health_check():
    """
    Endpoint de Health Check para monitoramento e validação do status da API.
    """
    return {
        "status": "healthy",
        "project": settings.PROJECT_NAME,
        "version": settings.VERSION
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)