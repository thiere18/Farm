from typing import Any, List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from sqlalchemy.sql.functions import user
from .. import oauth2
from app.repository import user_repository
from app.schemas import token, user as schemas
from ..database import get_db

router = APIRouter(
    prefix="/api/v1/live",
    tags=['Live']
)

@router.get('/live-ships{update_id}', response_model=schemas.User)
def get_me(update_id: int):
    return {"msg": update_id}


