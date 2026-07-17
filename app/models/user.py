from sqlalchemy import Column, Integer, String
from app.database.base import Base

class User(Base):
    __tablename__ = "userdata" #here  tablename acting like a constructor and we are giving table name as Users
    id = Column(
        Integer, 
        primary_key=True,
        index=True
    )
    
    username = Column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(
        String(20),
        nullable=False
    )

    role = Column(
        String(20),
        nullable=False,
        default="User"
    )


