from  fastapi import FastAPI , APIRouter

app = FastAPI()

auth_routes = APIRouter(prefix="/auth", tags=["auth"])
order_routher = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_routher.get('/')
async def 


app.include_router(auth_routes)
app.include_router(order_routher)


