from typing import Any
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from ..schemas import UserCreate
from ..database import get_db
from ..models import User
from ..security import hash_password, verify_password, generate_jwt_token
from ..dependencies import auth_dependency

router = APIRouter()

@router.post("/login")
async def user_login(data: UserCreate,response: Response, db: Session = Depends(get_db)):
	data_dict = data.model_dump()
	username = data_dict["username"]
	password = data_dict["password"]
	user = db.query(User).where(User.name == username).first()
	if not user:
		response.status_code = status.HTTP_400_BAD_REQUEST
		return{"message":"User does not exist"}
	correct_password = verify_password(password,user.hashed_pwd)
	if not correct_password:
		response.status_code = status.HTTP_401_UNAUTHORIZED
		return{"message":"Password error"}
	token = generate_jwt_token({"id":user.id})
	if not token:
		response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
		return {"message": "An error occurred while creating the token"}
	response.set_cookie("jwt_token",token)
	return{"message":"Successfully generate token"}
	
		
	

@router.post("/register")
async def user_register(
	data: UserCreate, response: Response, db: Session = Depends(get_db)
):
	data_dict = data.model_dump()
	username = data_dict["username"]
	password = data_dict["password"]
	existing_user = db.query(User).where(User.name == username).first()
	if existing_user:
		response.status_code = status.HTTP_400_BAD_REQUEST
		return {"message": "Username already taken"}

	hashed_pwd = hash_password(password)
	db.add(User(name=username, hashed_pwd=hashed_pwd))
	db.commit()

	return {"message": "Successfully registered"}


@router.post("/logout")
async def user_logout(response: Response, _: dict[str, Any] = Depends(auth_dependency)):
	response.delete_cookie(key="jwt_token")
	return {"message": "Successfully logged out"}
