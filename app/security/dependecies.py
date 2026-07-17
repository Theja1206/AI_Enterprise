from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from app.security.auth_handler import AuthHandler
from app.services.user_service import UserService
from sqlalchemy.orm import Session
from app.database.dependencies import get_db

security = HTTPBearer()

def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)

):
    token = credentials.credentials
    
    payload = AuthHandler.verify_token(token)
    username = payload.get("sub")

    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    user_service = UserService(db)
    
    user = user_service.get_user(username)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not Found"
        )
    
    return user
