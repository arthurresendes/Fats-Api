from typing import Optional
from pydantic import BaseModel as SCBaseModel

# Para cada tabela deve ter um shcema 

class CursoSchema(SCBaseModel):
    id: Optional[int]
    titulo: str
    aulas: int
    horas: int
    
    class Config:
        orm_mode = True

