from sqlalchemy import text
from app.database.session import SessionLocal

db = SessionLocal()
try:
    db.execute(
        text(
            """INSERT INTO userdata(username,password,role)
            VALUES(
            'testuser',
            'hashedpassword',
            'USER')"""
        )
    )
    db.commit()
    print('Inserted successfully')

finally:
    db.close()