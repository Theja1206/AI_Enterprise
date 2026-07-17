#database.py
from sqlalchemy import create_engine
from app.config.settings import settings

#This file creates SQLAlchemy Engine.
#It opens connections ,manages connection pulling
#sends sql to postgresql and recieves results.
#There should be only one engine for the entire application.


DATABASE_URL = (
    f"postgresql://"
    f"{settings.DB_USERNAME}:"
    f"{settings.DB_PASSWORD}@"
    f"{settings.DB_HOST}:"
    f"{settings.DB_PORT}/"
    f"{settings.DB_NAME}"
)

engine = create_engine(
    settings.DATABASE_URL,
    echo=True
)

