from fastapi import FastAPI
import uvicorn
from app.api.router import router
from app.core.logging_config import setup_logging
from app.config.settings import settings
from contextlib import asynccontextmanager

logger = setup_logging(settings.LOG_LEVEL)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("============================================")
    logger.info("Application Started")
    logger.info(settings.APP_NAME)
    logger.info(settings.APP_VERSION)
    logger.info("============================================")

    yield
    logger.info("Application shutdown")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan
)

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
