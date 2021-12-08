from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import  user, auth
# models.Base.metadata.create_all(bind=engine)

app = FastAPI(
        docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
    title="Upwork-user management API",
    description="MTP API documentation ",
    version="2.0",
    openapi_url="/api/v1/openapi.json"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)
# app.include_router(post.router)

@app.get("/")
def root():
    return {"message": "Hello World",}