from typing import Optional
from pydantic import BaseModel

class Alunos(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    curso: str