from typing import Optional
from pydantic import BaseModel as SCBaseModel


class MateriaSchema(SCBaseModel):
    id: Optional[int] = None
    nome_materia: str
    id_professor: int
    
    class Config:
        from_attributes = True