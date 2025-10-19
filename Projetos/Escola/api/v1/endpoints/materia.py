from typing import List
from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.materia_model import MateriaModel
from schemas.materia_schema import MateriaSchema
from core.deps import get_session

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=MateriaSchema)
async def post_materia(materia: MateriaSchema, db: AsyncSession = Depends(get_session)):
    nova_materia = MateriaModel(
        nome_materia=materia.nome_materia,
        id_professor=materia.id_professor
    )
    db.add(nova_materia)
    await db.commit()
    await db.refresh(nova_materia)

    return nova_materia


@router.get("/", response_model=List[MateriaSchema])
async def get_materias(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MateriaModel)
        result = await session.execute(query)
        materias: List[MateriaModel] = result.scalars().all()
        return materias


@router.get("/{materia_id}", response_model=MateriaSchema, status_code=status.HTTP_200_OK)
async def get_materia_individual(materia_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MateriaModel).filter(MateriaModel.id == materia_id)
        result = await session.execute(query)
        materia = result.scalars().one_or_none()

        if materia:
            return materia
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Matéria não encontrada.")


@router.put("/{materia_id}", response_model=MateriaSchema, status_code=status.HTTP_202_ACCEPTED)
async def put_materia(materia_id: int, materia: MateriaSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MateriaModel).filter(MateriaModel.id == materia_id)
        result = await session.execute(query)
        materia_up = result.scalars().one_or_none()

        if materia_up:
            materia_up.nome_materia = materia.nome_materia
            materia_up.id_professor = materia.id_professor

            await db.commit()
            await db.refresh(materia_up)
            return materia_up
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Matéria não encontrada.")


@router.delete("/{materia_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_materia(materia_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(MateriaModel).filter(MateriaModel.id == materia_id)
        result = await session.execute(query)
        materia_del = result.scalars().one_or_none()

        if materia_del:
            await session.delete(materia_del)
            await session.commit()
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Matéria não encontrada.")
