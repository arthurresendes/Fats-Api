from fastapi import FastAPI

app = FastAPI()


@app.get("/palindormo/{palavra}")
async def palindro(palavra:str):
    inverte = palavra[::-1]
    if palavra == inverte:
        return {"palavra_eh_palindromo": inverte}
    else:
        return {"palavra_nao_eh_palindromo": inverte}