#dependencies.py
from app.database.session import SessionLocal

# this is a dependency injection 
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        