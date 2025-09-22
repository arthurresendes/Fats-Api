from  fastapi import FastAPI , APIRouter

app = FastAPI()

auth_routes = APIRouter(prefix="/auth", tags=["auth"])
order_routher = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_routher.get('/listagem')
async def lista():
    return {"Lista produtos": "[Café, Coca-cola, Banana]"}

@auth_routes.post("/pedidos")
async def cadastrar(produto: str , quantidade: int):
    return {"Produto": {produto}, "Quantidade": {quantidade}}

app.include_router(auth_routes)
app.include_router(order_routher)


