from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.professor_model import ProfessorModel
from schemas.professor_schema import ProfessorSchema
from core.deps import get_session

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED,response_model=ProfessorSchema)
async def post_professor(professor: ProfessorSchema, db: AsyncSession = Depends(get_session)):
    novo_professor = ProfessorModel(nome=professor.nome, idade=professor.idade, ano_escolar = professor.aula_ano_escolar)
    db.add(novo_professor)
    await db.refresh(novo_professor)
    
    return novo_professor

@router.get("/", response_model=List[ProfessorSchema])
async def get_professor(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel)
        result = await session.execute(query)
        professores: List[ProfessorModel] = result.scalars().all()
        return professores

@router.get("/{professor_id}", status_code=status.HTTP_200_OK, response_model=ProfessorSchema)
async def get_professor_individual(professor_id: int , db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == professor_id)
        result = await session.execute(query)
        professor = result.scalars().one_or_none
        
        if professor:
            return professor
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{professor_id}", response_model=ProfessorSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_professor(professor_id: int ,professor: ProfessorSchema ,db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == professor_id)
        result = await session.execute(query)
        prof_up = result.scalars().one_or_none
        
        if prof_up:
            prof_up.nome = professor.nome
            prof_up.idade = professor.idade
            prof_up.aula_ano_escolar = professor.aula_ano_escolar
            
            await db.commit()
            return prof_up
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/{professor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_aluno(professor_id:int , db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == professor_id)
        result = await session.execute(query)
        professor_del = result.scalar_one_or_none()
    
    if professor_del:
        await db.delete(professor_del)
        await db.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)