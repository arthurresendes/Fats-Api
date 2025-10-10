from fastapi import FastAPI,status,HTTPException

app = FastAPI()

livros = {
    1: {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "paginas": 256},
    2: {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "paginas": 96},
    3: {"titulo": "1984", "autor": "George Orwell", "paginas": 328}
}



@app.get("/livros")
async def ver_livros():
    return livros

@app.get("/livros/{livro_id}")
async def ver_livro_id(livro_id:int):
    try: 
        livro = livros[livro_id]
        return livro
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Livro não encontrado")

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("ex002:app",host="127.0.0.1" ,port=8000,reload=True)