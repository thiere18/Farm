from typing import Any, List
from fastapi import  status, HTTPException,Response
from sqlalchemy.orm import Session

from app.utils import  utils
# from app.models import users, roles as models
# from app.schemas import role, user as schemas
from app.schemas import role as roleSchema
# from app.schemas import user as userSchema
from app.models.roles import *
from app.models.users import *







# /users/
# /users


def create_role(role: roleSchema.Role, db: Session )->Any:
    verify_already_exists=db.query(Role).filter(Role.name==role.name).first()
    if verify_already_exists:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"role {role.name} already exists"
                            )

    new_role = Role(**role.dict())
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role



def get_one_role(id: int, db: Session )->Any:

     role = db.query(Role).filter(Role.id == id).first()
     if not role:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Role with id: {id} does not exist")

     return role

  
def get_all_role(db: Session )->Any:


     role = db.query(Role).all()
     if not role:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=" no role for now")
     return role

# # def get_me(db: Session , current_user:int)->Any:
# #     role= db.query(roleModels.Role).filter(roleModels.Role.id==current_user.id).first()
# #     if not role:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=" no role for now")
    
# #     return role
def update_role( id: int, updated_post:roleSchema.RoleUpdate, db: Session, current_user: int):
    user= db.query(User).filter(User.id==current_user.id).first()
    is_admin=user.user_role=="admin"
    if not is_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="not an admin user")
    
    role_query = db.query(Role).filter(Role.id == id)
    role = role_query.first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"role with id: {id} was not found")

    role_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return role_query



def delete_role( id: int,  db: Session, current_user: int):
    user= db.query(User).filter(User.id==current_user.id).first()
    is_admin=user.user_role=="admin"
    if not is_admin:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="not an admin user")
    
    role_query = db.query(Role).filter(Role.id == id)
    role = role_query.first()
    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"role with id: {id} was not found")
    role_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

