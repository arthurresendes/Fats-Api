from fastapi import FastAPI
# uvicorn main:app --reload
app = FastAPI()


@app.get("/conversor")
async def convertendo(graus: float):
    c = 5/9 * (graus - 32)
    return {"graus em Celsius": round(c,2)}