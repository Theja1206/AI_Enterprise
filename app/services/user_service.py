#user_service.py
from app.security.password_handler import PasswordHandler
from app.models.role import Role
from app.repositories.user_repository import UserRepository
from sqlalchemy.exc import IntegrityError
from app.core.exceptions import UserAlreadyExistsException, UserNotFoundException
from fastapi import HTTPException, status

class UserService:
    def __init__(self, db):
        self.user_repository = UserRepository(db)

#REGISTER USER
    def register_user(self, username: str, password: str):

        existing_user = (
            self.user_repository
            .get_by_username(username)
        )

        if existing_user:
            raise UserAlreadyExistsException()
        
        hashed_password = (
            PasswordHandler
            .hash_password(password)
        )

        #role = Role.ADMIN if username.lower() == "admin" else Role.USER
        if username.lower() == "admin":
            role = Role.ADMIN.value
        else:
            role = Role.USER.value

        return(

        self.user_repository.create_user(
            username=username,
            password=hashed_password,
            role=role)
        )
    
    #LOGIN USER
    def validate_user(self, username: str, password: str):
        user = self.user_repository.get_by_username(username)
        
        if user is None:
             return None
        
        if not PasswordHandler.verify_password(
            password,
            user.password):
            return None
        return user
        print(user.password)
        print(password)
    

    #GET USER BY ID
    def get_user_by_id(self, user_id: int):
            user = self.user_repository.get_by_id(user_id)
            if user is None:
                raise UserNotFoundException()
            return user 
        

    #GET ALL USERS
    def get_all_users(self):
        return(
            self.user_repository
            .get_all_users()
        )

    #UPDATE USERNAME
    def update_username(self, user, username: str):
            user = self.user_repository.update_user(user, username)
            if user is None:
                 raise UserNotFoundException()
            return self.user_repository.update_user(user, username)
    


    #DELETE USER
    def delete_user(self, user):
            user = self.user_repository.delete_user(user)
            if user is None:
                 raise UserNotFoundException()
            return self.user_repository.delete_user(user)

    #GET USER
    def get_user(self, username: str):
            user = self.user_repository.get_by_username(username)
            if user is None:
                raise UserNotFoundException()
            return user
        
    
    

    
    

    
