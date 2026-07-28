from sqlalchemy import Column, Integer, String
from app.database.base import Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "userdata"
     #here  tablename acting like a constructor and we are giving table name as Users
    id: Mapped[int] = mapped_column(
        Integer, 
        primary_key=True,
        index=True
    )
    
    username: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
        index=True
    )

    password: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    role: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )


