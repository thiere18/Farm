from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers.api_v1.api import  api_router
# models.Base.metadata.create_all(bind=engine)

app = FastAPI(
        docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
    title="Upwork-user management API",
    description="MTP API documentation ",
    version="2.0",
    openapi_url="/api/v1/openap.json"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/")
def root():
    return {"message": "Hello World",
            "openapiapi documentation url":"/api/v1/docs",
            "redoc documentation url ": "/api/v1/redoc"
            }