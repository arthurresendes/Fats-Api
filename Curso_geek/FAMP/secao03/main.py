from fastapi import FastAPI
from fastapi import status, HTTPException
from models import Curso
# & "C:\Users\arregomes\Envs\famp-secao03\Scripts\Activate.ps1"
app = FastAPI()

cursos = {
    1:{
        "titulo": "Programação",
        "aulas": 112,
        "horas": 58
    },
    2:{
        "titulo": "Python",
        "aulas": 300,
        "horas": 64
    }
}

@app.get('/cursos')
async def get_cursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def get_cursos_id(curso_id:int):
    try:
        curso = cursos[curso_id]
        curso.update({"id": curso_id})
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    next_id:int = len(cursos) + 1
    cursos[next_id] = curso
    del curso.id
    return curso

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="127.0.0.1", port=8000, debug=True, reload=True)
