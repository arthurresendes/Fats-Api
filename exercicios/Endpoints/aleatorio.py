from fastapi import FastAPI
from random import randint

app = FastAPI()


@app.get("/random")
async def aleatorio(min:int , max:int):
    num = randint(min,max)
    return {"numero_aleatorio_no_intervalo": num}