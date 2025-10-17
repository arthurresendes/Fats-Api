from typing import List, ClassVar
from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "sqlite+aiosqlite:///./faculdade.db"
    DBBaseModel: ClassVar  = declarative_base()
    
    JWT_SECRET: str = 'UbkXnRReI2kei3dBQSLdvZ8nBBJjN3tWwcRzqy8_Iyw'
    '''
    terminal
    python
    import secrets
    token:str = secrets.token_urlsafe(32) # Gera um token de tamanho 32
    '''
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sensitive = True
        

settings : Settings = Settings()