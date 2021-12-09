from typing import Any, List
from fastapi import  status, HTTPException, Depends
from sqlalchemy.orm import Session

from app.utils import  utils
# from app.models import users, roles as models
# from app.schemas import role, user as schemas
from app.schemas import role as roleSchema
from app.schemas import user as userSchema
from app.models import roles as roleModels
from app.models import users as userModels





# /users/
# /users


def create_role(role: roleSchema.Role, db: Session )->Any:
    """Register new role

    Args:
        role (role.Role): [description]
        db (Session, optional): [description]. Defaults to Depends(get_db).

    Returns:
        Any: [description]
    """


    new_user = roleModels.Role(**role.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



# # def get_one_user(id: int, db: Session )->Any:
# #     """[Get single role by id]

# #     Args:
# #         id (int): [description]
# #         db (Session, optional): [description]. Defaults to Depends(get_db).
# #         current_user (int, optional): [description]. Defaults to Depends(oauth2.get_current_user).

# #     Raises:
# #         HTTPException: [description]

# #     Returns:
# #         Any: [description]
# #     """
# #     role = db.query(roleModels.Role).filter(roleModels.Role.id == id).first()
# #     if not role:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                             detail=f"Role with id: {id} does not exist")

# #     return role

  
# # def get_all_users(db: Session )->Any:
# #     """Get all models

# #     Args:
# #         db (Session, optional): [description]. Defaults to Depends(get_db).
# #         current_user (int, optional): [description]. Defaults to Depends(oauth2.get_current_user).

# #     Raises:
# #         HTTPException: [description]

# #     Returns:
# #         Any: [description]
# #     """
# #     role = db.query(roleModels.Role).all()
# #     if not role:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                             detail=" no role for now")


# #     return role

# # def get_me(db: Session , current_user:int)->Any:
# #     role= db.query(roleModels.Role).filter(roleModels.Role.id==current_user.id).first()
# #     if not role:
# #         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=" no role for now")
    
# #     return role


