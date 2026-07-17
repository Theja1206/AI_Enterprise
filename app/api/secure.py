#secure.py
from fastapi import APIRouter, Depends
from app.security.dependecies import get_current_user

router = APIRouter(
    prefix="/secure",
    tags=["secure APIs"]
)

@router.get("/profile")
def profile(
    current_user = Depends(get_current_user)
    ):
    return {
        "username": current_user.username,
        "role": current_user["role"],
        "message":"Welcome to your secure profile"
    }

@router.get("/dashboard")
def dashboard(user: str = Depends(get_current_user)):
    return {
        "role": user["role"],
        "message":f"Welcome {user['username']}"
    }

