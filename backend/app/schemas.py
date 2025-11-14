from pydantic import BaseModel
from datetime import datetime


class PostBase(BaseModel):
	title: str
	content: str


class Post(PostBase):
	id: int
	created_at: datetime
	owner_id: int

	class Config:
		orm_mode = True


class UserBase(BaseModel):
	username: str


class UserCreate(UserBase):
	password: str


class User(UserBase):
	id: int
	posts: list[Post]

	class Config:
		orm_mode = True
