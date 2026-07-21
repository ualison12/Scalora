from fastapi import FastAPI
from app.api.router import api_router
from app.api.routes.auth import router as auth_router
from app.api.routes.companies import router as company_router
from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.APP_DEBUG,
)

app.include_router(company_router)
app.include_router(auth_router)

app.include_router(
    api_router,
    prefix=settings.API_PREFIX,
)

@app.get("/", tags=["Root"])
async def root():
    return {
        "name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }