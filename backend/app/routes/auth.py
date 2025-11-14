from fastapi import APIRouter
from ..schemas import UserCreate

router = APIRouter()


@router.post("/register")
async def user_register(data: UserCreate):
    data_dict = data.model_dump()
