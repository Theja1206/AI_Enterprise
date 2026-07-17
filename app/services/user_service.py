#user_service.py
from app.security.password_handler import PasswordHandler
from app.models.role import Role
from app.repositories.user_repository import UserRepository

class UserService:

    def __init__(self, db):
        self.user_repository = UserRepository(db)

    def register_user(self, username: str, password: str):

        existing_user = (
            self.user_repository
            .get_by_username(username)
        )

        if existing_user:
            return False
        
        hashed_password = (
            PasswordHandler
            .hash_password(password)
        )

        #role = Role.ADMIN if username.lower() == "admin" else Role.USER
        if username.lower() == "admin":
            role = Role.ADMIN.value
        else:
            role = Role.USER.value

        self.user_repository.create_user(
            username=username,
            password=hashed_password,
            role=role
        )
        return True
    
    def validate_user(self, username: str, password: str):
        user = (self.user_repository
                .get_by_username(username)
                )
        
        if user is None:
            return False
        
        return PasswordHandler.verify_password(
            password,
            user.password
        )
    
    def get_user(self, username: str):
        return (
            self.user_repository
            .get_by_username(username)
        )
    

    
    

    
