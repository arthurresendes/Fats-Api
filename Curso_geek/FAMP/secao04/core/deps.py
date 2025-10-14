from typing import AsyncGenerator # Uso reduzido de memoria assincronico
from sqlalchemy.ext.asyncio import AsyncSession 
from core.database import Session

async def get_session() -> AsyncGenerator:
    session: AsyncSession = Session()
    
    try:
        yield session
    finally:
        await session.close()