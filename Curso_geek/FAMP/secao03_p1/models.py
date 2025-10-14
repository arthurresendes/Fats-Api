from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

cursos = [
    Curso(id=1,titulo="Programação em Python", aulas=42,horas=56),
    Curso(id=2,titulo="Programação em C", aulas=52,horas=67)
]