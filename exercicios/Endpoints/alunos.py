from fastapi import FastAPI
from pydantic import BaseModel
# uvicorn main:app --reload
app = FastAPI()

class Aluno(BaseModel):
    nome: str
    idade: int

alunos = []
contador_alunos = 1

@app.post("/cadastro")
async def cadastro(aluno: Aluno):
    global contador_alunos
    novo_aluno = {"id": contador_alunos, "nome": aluno.nome , "idade": aluno.idade}
    alunos.append(novo_aluno)
    contador_alunos+=1
    return novo_aluno
    
@app.get("/verifica")
def listar_alunos():
    return alunos