from fastapi import APIRouter
from app.config.settings import settings

router = APIRouter() #APIRouter is object assigned to router.


@router.get("/health")#We are defining end point. 
def health():
    return {
        "status": "UP",
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT
        }
