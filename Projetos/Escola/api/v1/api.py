from fastapi import APIRouter
from api.v1.endpoints import aluno,materia,professor

api_router = APIRouter()
api_router.include_router(aluno.router, prefix="/alunos", tags=['alunos'])
api_router.include_router(materia.router, prefix="/materia", tags=['materias'])
api_router.include_router(professor.router, prefix="/professores", tags=['professores'])