#auth_handler.py
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from app.config.settings import settings 

class AuthHandler:
    @staticmethod
    def create_access_token(data: dict):
        payload = data.copy()
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        payload.update({"exp":expire})
        return jwt.encode(
            payload, 
            settings.SECRET_KEY,
            algorithm=settings.JWT_ALGORITHM
        )
    
    @staticmethod
    def decode_access_token(token: str):
        try:
            return jwt.decode(
                token,
                settings.SECRET_KEY,
                algorithms=[settings.JWT_ALGORITHM]
            )
        except JWTError:
            return None

