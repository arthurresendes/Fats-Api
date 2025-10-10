from pydantic import BaseModel
from typing import Optional

class Alunos(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    curso: str