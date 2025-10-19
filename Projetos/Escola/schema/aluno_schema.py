from typing import Optional
from pydantic import BaseModel as SCBaseModel


class AlunoSchema(SCBaseModel):
    id: Optional[int] = None
    nome: str 
    idade: int
    ano_escolar:int
    
    class Config:
        from_attributes = True