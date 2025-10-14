from core.configs import settings
from sqlalchemy import Column,Integer,String
# Criação do banco
class CursoModel(settings.DBBaseModel):
    __tablename__ = 'cursos'
    
    id:int = Column(Integer , primary_key=True, autoincrement=True)
    titulp: str = Column(String(100))
    aulas: int = Column(Integer)
    horas: int = Column(Integer)

