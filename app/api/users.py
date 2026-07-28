#users.py
from fastapi import HTTPException, APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.schemas.user_schema import UserResponse, UserUpdateRequest
from app.security.dependecies import get_current_user
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

#GET CURRENT USER 
@router.get("/me", response_model = UserResponse)
def get_my_profile(
    current_user=Depends(
        get_current_user
    )
):
    return current_user

#GET ALL USERS
@router.get("/", response_model=list[UserResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
        )
):
    service = UserService(db)
    return service.get_all_users()

#GET USER BY ID
@router.get("/{user_id}", response_model= UserResponse)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):
    service = UserService(db)
    user = service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

#UPDATE USER 
@router.put("/{user_id}", response_model= UserResponse)
def update_user(
    user_id: int,
    request: UserUpdateRequest,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    )
):

    service = UserService(db)
    user = service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    updated_user = service.update_username(
        user,
        request.username
    )

    db.commit()
    return updated_user


#DELETE USER
@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(
        get_current_user
    ) 
):
    service = UserService(db)
    user = service.get_user_by_id(user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    service.delete_user(user)
    db.commit()
    return {
        "message": "User deleted successfully",
        "user_id": user_id
    }

