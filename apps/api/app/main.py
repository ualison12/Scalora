import logging
from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from app.api.router import api_router
from app.api.routes.auth import router as auth_router
from app.api.routes.companies import router as company_router
from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("scalora")

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.APP_DEBUG,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = request.headers.get("x-request-id", str(uuid4()))
    logger.info("request_start", extra={"request_id": request_id, "path": request.url.path, "method": request.method})
    response = await call_next(request)
    response.headers["x-request-id"] = request_id
    logger.info("request_end", extra={"request_id": request_id, "status_code": response.status_code})
    return response

@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    logger.exception("unhandled_exception", extra={"path": request.url.path, "error": str(exc)})
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

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