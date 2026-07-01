from fastapi import APIRouter
from app.api.health import router as health_router

router = APIRouter() #APIRouter is object assigned to router.

router.include_router(health_router)
