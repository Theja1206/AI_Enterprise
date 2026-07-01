from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    ENVIRONMENT: str
    HOST: str
    PORT: int
    LOG_LEVEL: str

    class Config:
        env_file = ".env"

settings = Settings()# lower case settings is the object of settings class where we are mapping with .env folder
