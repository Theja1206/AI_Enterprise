from sqlalchemy.orm import Session
from app.database.dependencies import get_db
from app.services.user_service import UserService
from fastapi import Depends

def get_user_service(
        db: Session = Depends(get_db)
):
    return UserService(db)
    

