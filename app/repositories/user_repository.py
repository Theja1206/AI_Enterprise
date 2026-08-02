from sqlalchemy.orm import Session
from app.models.user import User
from sqlalchemy.exc import SQLAlchemyError
from app.core.exceptions import DatabaseException


class UserRepository:
    def __init__(self, db: Session):
        self.db = db
  
     #below method is python code equivalent to writing sql query for SELECT command
     # READ USER 
    def get_by_username(self, username: str):
        return (
            self.db.query(User)
            .filter(User.username == username)
            .first()
        )
    
     #CREATE USER
    def create_user(
            self, 
            username: str,
            password: str,
            role: str
    ):
        user = User(
            username=username,
            password=password,
            role=role
            )
        try:
        
            self.db.add(user)
            self.db.commit() #Saves to the database
            self.db.flush() #It inserts into the database and ensures primary key is  generated ,but it doesn't save the record to the db.
            self.db.refresh(user)
            return user
        except SQLAlchemyError as e:
            self.db.rollback()
            raise DatabaseException(str(e))
        
 
    #GET/READ BY ID
    def get_by_id(self, user_id: int):
        return(
            self.db.query(User)
            .filter(User.id == user_id)
            .first()
        )

    #GET ALL USERS
    def get_all_users(self):
        return(
            self.db.query(User)
            .all()
        )

    #UPDATE USER
    def update_user(self, user: User, username: str):
        user.username = username
        self.db.flush()
        self.db.refresh(user)
        return user

    #DELETE USER
    def delete_user(self, user: User):
        self.db.delete(user)
        self.db.flush()
        



