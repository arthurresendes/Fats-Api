from fastapi import FastAPI, status,HTTPException
from models02 import Livros

app = FastAPI()

livros = {
    1: {"titulo": "1984", "autor": "George Orwell"},
    2: {"titulo": "O Hobbit", "autor": "J.R.R. Tolkien"}
}


@app.get("/livros")
async def ver_alunos():
    return livros

@app.post("/livros" , status_code=status.HTTP_201_CREATED)
async def envia_dados(livro: Livros):
    next_id = len(livros) + 1
    livros[next_id] = livro
    del livro.id
    return livro


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("ex002:app", host="127.0.0.1", port=8000, reload=True)