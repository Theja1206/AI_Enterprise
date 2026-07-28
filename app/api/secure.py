#secure.py
from fastapi import APIRouter, Depends
from app.security.dependecies import get_current_user

router = APIRouter(
    prefix="/secure",
    tags=["secure APIs"]
)

@router.get("/profile")
def profile(
    current_user=Depends(get_current_user)
    ):
    return {
        "message":"Welcome to your secure profile",
        "role": current_user.role,
        "username": current_user.username    
    }

@router.get("/dashboard")
def dashboard(current_user=Depends(get_current_user)):
    return {
        "message":"Welcome to secure dashboard",
        "username":current_user.username,
        "role": current_user.role
        
    }

