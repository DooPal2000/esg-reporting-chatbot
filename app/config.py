# Application Configuration
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8080
    DATABASE_URL: str = "postgresql://user:password@localhost/esg_db"
    DEBUG: bool = True
    SECRET_KEY: str = "your-secret-key-here"

    class Config:
        env_file = ".env"

settings = Settings()
