from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    ENVIRONMENT: str
    HOST: str
    PORT: int
    LOG_LEVEL: str
    SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str

    @property
    def DATABASE_URL(self): # here self meaning object.
        return(
            f"postgresql://"
            f"{settings.DB_USERNAME}:"
            f"{settings.DB_PASSWORD}@"
            f"{settings.DB_HOST}:"
            f"{settings.DB_PORT}/"
            f"{settings.DB_NAME}"
        )

    class Config:
        env_file = ".env"

settings = Settings()# lower case settings is the object of settings class where we are mapping with .env folder
