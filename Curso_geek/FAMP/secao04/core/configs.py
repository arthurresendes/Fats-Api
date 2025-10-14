from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar

class Setting(BaseSettings):
    """
    Configurações gerais utilizadas na aplicação
    """
    API_V1_STR:str = '/api/v1'
    DB_URL: str = "sqlite+aiosqlite:///./faculdade.db"
    DBBaseModel: ClassVar = declarative_base()
    
    class Config:
        case_sensitive = True


settings = Setting()
