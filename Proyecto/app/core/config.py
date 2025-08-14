# app/core/config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Gestor de Tareas"
    VERSION: str = "1.0.0"

    class Config:
        env_file = ".env"

settings = Settings()
