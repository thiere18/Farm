from fastapi import APIRouter, Depends
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.repository import auth_repository
from app.config import database
from app.config.config import settings
from app.schemas import token as schemas


auth_router = APIRouter(
    tags=['Authentication'] ,
)


@auth_router.post('/token', response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    return auth_repository.login(user_credentials, db)