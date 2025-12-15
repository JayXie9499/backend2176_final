import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .schemas import Config
from .database import engine
from .routes import auth_router, posts_router

models.Base.metadata.create_all(bind=engine)

config = Config()  # type: ignore
app = FastAPI(docs_url=None, redoc_url=None)
app.add_middleware(
	CORSMiddleware,
	allow_origins=config.ALLOWED_ORIGINS,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)
app.include_router(auth_router, prefix="/auth")
app.include_router(posts_router, prefix="/posts")

if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=config.PORT)
