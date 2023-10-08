from fastapi import FastAPI
from items_views import router as items_router
from users.views import router as users_router
from contextlib import asynccontextmanager
from db.models.base import Base
from db.models.db_helper import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="study of fastapi"
)
app.include_router(items_router)
app.include_router(users_router)


@app.get("/")
def get():
    return {
        "message": "Hello fastapi!"
    }


@app.post("/calc/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b
    }
