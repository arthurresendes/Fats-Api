from core.configs import settings
from core.database import engine



async def create_tables() -> None:
    import models._all_models
    
    