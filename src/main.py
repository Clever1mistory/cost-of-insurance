import uvicorn
from fastapi import FastAPI

from src.ops.routers import router
from src.database import init_db, close_db


app = FastAPI()
app.include_router(router, prefix="/api")


@app.on_event("startup")
async def startup():
    await init_db()


@app.on_event("shutdown")
async def shutdown():
    await close_db()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
