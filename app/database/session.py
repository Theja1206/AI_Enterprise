from sqlalchemy.orm import sessionmaker
from app.database.database import engine

# Represents one conversation with the database. 
#Every API requests, will recieve one session
#This prevents users from interferring with each other. 

SessionLocal = sessionmaker(
    autoflush=False,
    autocommit=False,
    bind=engine
) 