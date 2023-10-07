from fastapi import FastAPI
from items_views import router as items_router
from users.views import router as users_router


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
