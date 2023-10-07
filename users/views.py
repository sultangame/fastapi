from fastapi import APIRouter
from users.schemas import CreateUser
from users.crud import create_user

router = APIRouter(prefix="/user", tags=["User"])


@router.post('/')
def users(user: CreateUser):
    return create_user(user_in=user)
