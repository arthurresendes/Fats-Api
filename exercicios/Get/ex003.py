from fastapi import FastAPI,status,HTTPException

app = FastAPI()

filmes = {
    1: {"titulo": "Interestelar", "genero": "Ficção Científica", "duracao": 169},
    2: {"titulo": "Vingadores: Ultimato", "genero": "Ação", "duracao": 181},
    3: {"titulo": "Toy Story", "genero": "Animação", "duracao": 81}
}

@app.get("/filmes")
async def ver_filmes():
    return filmes

@app.get("/filmes/{id}")
async def ver_filmes_id(id:int):
    try:
        filme = filmes[id]
        return filme
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id nao identificado")

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("ex003:app",host="127.0.0.1",port=8000, reload=True)