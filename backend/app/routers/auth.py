from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.repository import auth_repository
from .. import database, utils, oauth2
from app.schemas import user ,token as schemas
from app.models import users as models

router = APIRouter(tags=['Authentication'] , prefix="/api/v1")


@router.post('/token', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    return auth_repository.login(user_credentials, db)