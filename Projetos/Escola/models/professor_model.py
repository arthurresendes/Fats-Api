from core.configs import settings
from sqlalchemy import Column,Integer,String


class AlunoModel(settings.DBBaseModel):
    __tablename__ = 'professores'
    
    id:int = Column(Integer , primary_key=True, autoincrement=True)
    nome: str = Column(String(100))
    idade: int = Column(Integer)
    aula_ano_escolar: int = Column(Integer)

