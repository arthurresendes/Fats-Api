from fastapi import FastAPI, status,HTTPException

app = FastAPI()

alunos = {
    1: {"nome": "Alice", "idade": 20, "curso": "Engenharia"},
    2: {"nome": "Bruno", "idade": 22, "curso": "Administração"},
    3: {"nome": "Carla", "idade": 19, "curso": "Ciência da Computação"}
}

@app.get("/alunos")
async def ver_alunos():
    return alunos

@app.get("/alunos/{aluno_id}")
async def ver_aluno_id(aluno_id: int):
    try:
        aluno = alunos[aluno_id]
        return aluno
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id não encontrado")

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("ex001:app", host="127.0.0.1", port=8000, reload=True)