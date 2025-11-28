from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User, Post

router = APIRouter()


@router.get("/")
async def get_posts(page: int = 0, db: Session = Depends(get_db)):
	posts = (
		db.query(Post, User.name)
		.join(User, Post.owner_id == User.id)
		.where(Post.id.between(1 + 10 * page, 10 + 10 * page))
		.all()
	)

	return {"message": "Successfully fetched posts data", "data": posts}
