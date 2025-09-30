from fastapi import APIRouter
from models import Usuario ,db
from sqlalchemy.orm import sessionmaker 

auth_router = APIRouter(prefix="/auth" , tags=["auth"])


@auth_router.get("/")
async def autenticar():
    return {"mensagem": "Você acessou a rota padrão de autenticado", "autenticado":False}

@auth_router.post("/criar_conta")
async def criar_conta(email: str,senha: str, nome:str,session):
    Session = sessionmaker(bind=db)
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.email == email).first()
    if usuario:
        return {"mensagem": "Usuario já criado"}
    else:
        novo_usuario = Usuario(nome,email,senha)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "Usuario cadastrado com sucesso"}