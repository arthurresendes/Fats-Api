from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Setting(BaseSettings):
    """
    Configurações gerais utilizadas na aplicação
    """
    API_V1_STR:str = '/api/v1'
    DB_URL: str = "sqlite:///./faculdade.db"
    DBBaseModel  = declarative_base()
    
    class Config:
        case_sensitive = True


settings = Setting()
