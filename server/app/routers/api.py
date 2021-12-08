from fastapi import APIRouter
from . import user,area, live,auth

api_router= APIRouter()

api_router.include_router(user.router)
api_router.include_router(area.router)
api_router.include_router(auth.router)
api_router.include_router(live.router)
def root():
    return {"message": "Hello World",}