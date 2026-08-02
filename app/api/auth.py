#auth.py
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi import Depends
from app.schemas.user_schema import UserRegisterRequest
from app.schemas.auth_schema import LoginRequest
from app.schemas.token_schema import TokenResponse
from app.services.user_service import UserService
from app.services.dependencies import get_user_service
from app.security.auth_handler import AuthHandler


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(
    request: UserRegisterRequest,
    user_service: UserService = Depends(get_user_service)
    ):

    user = user_service.register_user(
        request.username,
        request.password
    )

    # if not success:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="user already exist"
    #     )
    
    return {
        "message":"User registered successfully",
        "user": user.username
    }


@router.post("/login", response_model=TokenResponse)
def login(
    request : LoginRequest,
    user_service: UserService = Depends(get_user_service)
    ):

    user = user_service.validate_user(
        request.username,
        request.password
    )
    
    # if user is None:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="Invaid username/password"
    #     )
    
    token = AuthHandler.create_access_token(
        {
            "sub":request.username
        }
    )

    return TokenResponse(
        access_token=token,
        token_type="Bearer" 

    )



