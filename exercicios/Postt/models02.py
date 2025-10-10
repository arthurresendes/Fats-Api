from pydantic import BaseModel
from typing import Optional

class Livros(BaseModel):
    id: Optional[int] = None
    titulo: str
    autor: str