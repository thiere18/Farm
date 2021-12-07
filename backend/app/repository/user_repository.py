from typing import Any, List
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import  utils,oauth2
from app.models import users
from app.schemas import user
from ..database import get_db



# /users/
# /users


def create_user(user: user.UserCreate, db: Session )->Any:
    """Register new user

    Args:
        user (user.UserCreate): [description]
        db (Session, optional): [description]. Defaults to Depends(get_db).

    Returns:
        Any: [description]
    """

    # hash the password - user.password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = users.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



def get_one_user(id: int, db: Session )->Any:
    """[Get single user by id]

    Args:
        id (int): [description]
        db (Session, optional): [description]. Defaults to Depends(get_db).
        current_user (int, optional): [description]. Defaults to Depends(oauth2.get_current_user).

    Raises:
        HTTPException: [description]

    Returns:
        Any: [description]
    """
    user = db.query(users.User).filter(users.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user

  
def get_all_users(db: Session )->Any:
    """Get all users

    Args:
        db (Session, optional): [description]. Defaults to Depends(get_db).
        current_user (int, optional): [description]. Defaults to Depends(oauth2.get_current_user).

    Raises:
        HTTPException: [description]

    Returns:
        Any: [description]
    """
    user = db.query(users.User).all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=" no user for now")

    return user

def get_me(db: Session ,current_user: int =Depends(oauth2.get_current_user))->Any:
    """Return my information

    Args:
        db (Session, optional): [description]. Defaults to Depends(get_db).
        current_user (int, optional): [description]. Defaults to Depends(oauth2.get_current_user).

    Returns:
        Any: [description]
    """
    return current_user

# update me

#