from pydantic import BaseModel as SCBaseModel
from typing import Optional

class ProfessorSchema(SCBaseModel):
    id: Optional[int] = None
    nome:str
    idade:int
    aula_ano_escolar: int
    
    class Config:
        from_attributes = True