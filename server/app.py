from fastapi import FastAPI
from server.routes.item import router as ItemRouter

app = FastAPI()
app.include_router(ItemRouter, tags=["Item"], prefix="/item")

@app.get("/")
async def root():
    return {"message": "Hello FastAPI!"}

