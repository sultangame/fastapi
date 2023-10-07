from fastapi import FastAPI
from pydantic import EmailStr, BaseModel


app = FastAPI(
    title="study of fastapi"
)


@app.get("/")
def get():
    return {
        "message": "Hello fastapi!"
    }


class CreateUser(BaseModel):
    email: EmailStr
    user: str
    password: str


@app.post('/user/')
def users(user: CreateUser):
    return {
        'message': 'succes',
        "email": user.email
    }


@app.post("/calc/")
def add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "result": a + b
    }