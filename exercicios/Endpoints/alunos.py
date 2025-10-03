from fastapi import FastAPI
from pydantic import BaseModel
# uvicorn main:app --reload
app = FastAPI()

class Aluno(BaseModel):
    nome: str
    nota1: float
    nota2: float

alunos = []
contador_alunos = 1

@app.post("/cadastro")
async def cadastro(aluno: Aluno):
    global contador_alunos
    novo_aluno = {"id": contador_alunos, "nome": aluno.nome , "nota_1": aluno.nota1, "nota_2": aluno.nota2}
    alunos.append(novo_aluno)
    contador_alunos+=1
    return novo_aluno
    
@app.get("/verifica")
def listar_alunos():
    return alunos

@app.get("/verifica/nota/{id}")
async def nota(id: int):
    for i in alunos:
        if i['id'] == id:
            try:
                soma = float(i['nota_1']) + float(i['nota_2'])
                media = soma / 2
                return {
                    "id": i['id'],
                    "nome": i['nome'],
                    "media": media
                }
            except Exception as e:
                return {"erro": f"problema ao calcular média: {str(e)}"}
    return {"mensagem": "aluno_nao_encontrado"}
