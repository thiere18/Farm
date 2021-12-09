from fastapi import APIRouter
from app.config.config import settings
live_router = APIRouter(
    prefix="/lives",
    tags=['Live']
)

@live_router.get('/live-ships{update_id}')
def get_me(update_id: int):
    return {"msg": update_id}


