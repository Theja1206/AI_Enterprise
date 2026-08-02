from sqlalchemy.orm import Session

class TransactionManager:
    def __init__(self, db: Session):
        self.db = db

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def close(self):
        self.db.close()

