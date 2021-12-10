from fastapi import APIRouter
from app.config.config import settings
from ..live import live
from ..auth import auth
from ..user import user
from ..area import area
from ..role import role
api_router= APIRouter(prefix=f'{settings.api_prefix}')

api_router.include_router(auth.auth_router)
api_router.include_router(live.live_router)
api_router.include_router(user.user_router)
api_router.include_router(area.area_router)
# api_router.include_router(role.role_router)

