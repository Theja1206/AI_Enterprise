from fastapi import APIRouter
from app.api.health import router as health_router
from app.api.auth import router as auth_router
from app.api.secure import router as secure_router
from app.api.admin import router as admin_router
from app.api.users import router as users_router

router = APIRouter() #APIRouter is object assigned to router.

router.include_router(health_router)
router.include_router(auth_router)
router.include_router(secure_router)
router.include_router(admin_router)
router.include_router(users_router)


