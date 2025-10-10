from fastapi import FastAPI, status,HTTPException
from models01 import Alunos

app = FastAPI()

alunos = {
    1: {"nome": "Alice", "idade": 20, "curso": "Engenharia"},
    2: {"nome": "Bruno", "idade": 22, "curso": "Administração"},
    3: {"nome": "Carla", "idade": 19, "curso": "Ciência da Computação"}
}

@app.get("/alunos")
async def ver_alunos():
    return alunos

@app.post("/alunos" , status_code=status.HTTP_201_CREATED)
async def envia_dados(aluno: Alunos):
    next_id = len(alunos) + 1
    alunos[next_id] = aluno
    del aluno.id
    return aluno


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("ex001:app", host="127.0.0.1", port=8000, reload=True)

