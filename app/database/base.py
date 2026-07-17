#base.py
from sqlalchemy.orm import DeclarativeBase

#Every Database entity(Entity class ) will inherit from base
#This allows  SQLAlchemy to discover all entities automatically.

class Base(DeclarativeBase):
    pass