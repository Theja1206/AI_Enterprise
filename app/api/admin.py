#admin.py
from fastapi import APIRouter , Depends, HTTPException, status
from app.security.dependecies import get_current_user
from app.models.role import Role

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/users")
def admin_users(
    current_user=Depends(get_current_user)
):
    if current_user.role != Role.ADMIN.value:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only Admin can access this API"
        )
    return {
        "message": "Welcome Admin",
        "Logged_in_user": current_user.username
    }
