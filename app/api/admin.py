#admin.py
from fastapi import APIRouter , Depends
from app.security.role_dependency import require_admin

router = APIRouter(
    prefix="/admin",
    tags=["Admin APIs"]
)

@router.get("/users")
def users(user = Depends(require_admin)):
    return {
        "message":f"Welcome {user['username']}",
        "role":user["role"],
        "permissions":["User Management","Role Management","System Configuration"]
    }