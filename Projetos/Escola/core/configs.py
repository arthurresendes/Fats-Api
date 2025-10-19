from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "sqlite+aiosqlite:///./escola.db"
    DBBaseModel: ClassVar = declarative_base()
    
    class Config:
        case_sensitive = True

settings = Settings()