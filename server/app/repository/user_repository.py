from typing import Any, List
from fastapi import  status, HTTPException,Response
from sqlalchemy.orm import Session

from app.utils import  utils
from app.models import users as models
from app.models import roles as modelsRole
from app.schemas import user as schemas
# from app.schemas import role as roleSchemas




# /users/
# /users


def create_user(user: schemas.UserCreate, db: Session )->Any:
    verify_email_exists=db.query(models.User).filter(models.User.email == user.email).first()
    verify_username_exists=db.query(models.User).filter(models.User.username == user.username).first()
    # verif_role=db.query(modelsRole.Role).filter(modelsRole.Role.name == user.user_role).first()
    if verify_email_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"a user with this email already exists"
                            )
    if verify_username_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"a user with this username already exists"
                            )
    # if verif_role:
    #     raise HTTPException(status_code=status.HTTP_409_CONFLICT,
    #                         detail =f"role {user.user_role} doesn't exist"
    #                         )
    
    
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

    new_user = models.User(**user.dict())
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
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id: {id} does not exist")

    return user

  
def get_all_users(db: Session )->Any:
    """Get all models

    Args:
        db (Session, optional): [description]. Defaults to Depends(get_db).
        current_user (int, optional): [description]. Defaults to Depends(oauth2.get_current_user).

    Raises:
        HTTPException: [description]

    Returns:
        Any: [description]
    """
    user = db.query(models.User).all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=" no user for now")


    return user

def get_me(db: Session , current_user:int)->Any:
    user= db.query(models.User).filter(models.User.id==current_user.id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=" no user for now")
    
    return user

def update_user( id: int, updated_post:schemas.UserUpdate, db: Session, current_user: int):
    user= db.query(models.User).filter(models.User.id==current_user.id).first()
    is_admin=user.user_role=="admin"
    if not is_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="not an admin user")
    
    role_query = db.query(modelsRole.Role).filter(modelsRole.Role.id == id)
    role = role_query.first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"role with id: {id} was not found")

    role_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return role_query



def delete_user( id: int,  db: Session, current_user: int):
    user= db.query(models.User).filter(models.User.id==current_user.id).first()
    is_admin=user.user_role=="admin"
    if not is_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="not an admin user")
    
    role_query = db.query(modelsRole.Role).filter(modelsRole.Role.id == id)
    role = role_query.first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"role with id: {id} was not found")
    role_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)




