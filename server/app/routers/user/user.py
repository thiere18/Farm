from typing import Any, List
from fastapi import  status, Depends, APIRouter
from sqlalchemy.orm import Session
from app.config import oauth2
from app.repository import user_repository
from app.schemas import user as schemas
from app.config.database import get_db
from app.config.config import settings
user_router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@user_router.get('/me', response_model=schemas.User)
def get_me(db: Session = Depends(get_db),current_user: int= Depends(oauth2.get_current_user)):
    return user_repository.get_me(db, current_user)

@user_router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db))->Any:
    return user_repository.create_user(user, db)


@user_router.get('/{id}', response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db), current_user: int =Depends(oauth2.get_current_user))->Any:
    return user_repository.get_one_user(id,db)

@user_router.get('/', response_model=List[schemas.User])
def get_users_all(db: Session = Depends(get_db),current_user: int =Depends(oauth2.get_current_user))->Any:
    return user_repository.get_all_users(db)
 

  
# update me


#
