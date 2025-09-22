from fastapi import FastAPI , APIRouter

app = FastAPI()

auth_routes = APIRouter(prefix="/auth", tags=['auth'])
order_routes = APIRouter(prefix="/pedidos" , tags=['pedidos'])

@order_routes.get("/")
async def lista_pedidos():
    return {"mensagem": "Seus pedidos"}

@auth_routes.post("/login")
async def login(username:str , password:str):
    if username == "admin" and password == '123':
        return {"token": "fake-jwt"}
    return {"erro": "Credenciais inválidas"}

app.include_router(order_routes)
app.include_router(auth_routes)