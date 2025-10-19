from core.configs import settings
from sqlalchemy import Column,Integer,String


class AlunoModel(settings.DBBaseModel):
    __tablename__ = 'materias'
    
    id:int = Column(Integer , primary_key=True, autoincrement=True)
    nome_materia:str = Column(String(100))
    

