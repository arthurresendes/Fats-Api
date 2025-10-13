from fastapi import FastAPI,HTTPException,status, Response
from modelAluno import Alunos

app = FastAPI()
alunos = {
    1: {"nome": "Alice", "idade": 20, "curso": "Engenharia"},
    2: {"nome": "Bruno", "idade": 22, "curso": "Administração"},
    3: {"nome": "Carla", "idade": 19, "curso": "Ciência da Computação"}
}

@app.get("/")
async def raiz():
    return {"Mensagem": "Bem-vindo ao controle de alunos , nele podera ser feito um CRUD!!"}

@app.get("/alunos")
async def ver_todos_alunos():
    return alunos

@app.get("/alunos/{alunos_id}")
async def buscar_aluno_por_id(alunos_id : int):
    if alunos_id in alunos:
        return alunos[alunos_id]
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")

@app.post("/alunos", status_code=status.HTTP_201_CREATED)
async def adicionando_aluno(aluno:Alunos):
    proximo_id = len(alunos) + 1
    alunos[proximo_id] = aluno
    return aluno

@app.put("/alunos/{alunos_id}")
async def atualizar_aluno(alunos_id:int, aluno: Alunos):
    if alunos_id in alunos:
        alunos[alunos_id] = aluno
        return aluno
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")
        
@app.delete("/alunos/{alunos_id}")
async def deletar_aluno(alunos_id:int):
    if alunos_id in alunos:
        del alunos[alunos_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("alunos:app", host="127.0.0.1", port=8000,reload=True)