from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.aluno_model import AlunoModel
from schemas.aluno_schema import AlunoSchema
from core.deps import get_session

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED,response_model=AlunoSchema)
async def post_aluno(aluno: AlunoSchema, db: AsyncSession = Depends(get_session)):
    novo_aluno = AlunoModel(nome=aluno.nome, idade=aluno.idade, ano_escolar = aluno.ano_escolar)
    db.add(novo_aluno)
    await db.refresh(novo_aluno)
    
    return novo_aluno

@router.get("/", response_model=List[AlunoSchema])
async def get_aluno(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel)
        result = await session.execute(query)
        alunos: List[AlunoModel] = result.scalars().all()
        return alunos

@router.get("/{aluno_id}", status_code=status.HTTP_200_OK, response_model=AlunoSchema)
async def get_aluno_individual(aluno_id: int , db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel).filter(AlunoModel.id == aluno_id)
        result = await session.execute(query)
        aluno = result.scalars().one_or_none
        
        if aluno:
            return aluno
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.put("/{aluno_id}", response_model=AlunoSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_aluno(aluno_id: int ,aluno: AlunoSchema ,db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel).filter(AlunoModel.id == aluno_id)
        result = await session.execute(query)
        aluno_up = result.scalars().one_or_none
        
        if aluno_up:
            aluno_up.nome = aluno.nome
            aluno_up.idade = aluno.idade
            aluno_up.ano_escolar = aluno.ano_escolar
            
            await db.commit()
            return aluno_up
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/{aluno_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_aluno(aluno_id:int , db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AlunoModel).filter(AlunoModel.id == aluno_id)
        result = await session.execute(query)
        aluno_del = result.scalar_one_or_none()
    
    if aluno_del:
        await db.delete(aluno_del)
        await db.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)