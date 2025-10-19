from core.configs import settings
from sqlalchemy import Column,Integer,String,ForeignKey


class MateriaModel(settings.DBBaseModel):
    __tablename__ = 'materias'
    
    id:int = Column(Integer , primary_key=True, autoincrement=True)
    nome_materia:str = Column(String(100))
    id_professor: int = Column(Integer, ForeignKey('professores.id'))

