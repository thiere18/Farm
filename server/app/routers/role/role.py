# from typing import Any, List
# from fastapi import  status, Depends, APIRouter
# from sqlalchemy.orm import Session
# from app.config import oauth2
# from app.repository import role_repository
# from app.schemas import role as schemas
# from app.config.database import get_db
# role_router = APIRouter(
#     prefix="/roles",
#     tags=['Roles']
# )

# # @role_router.get('/me', response_model=schemas.Role)
# # def get_me(db: Session = Depends(get_db),current_user: int= Depends(oauth2.get_current_user)):
# #     return role_repository.get_me(db, current_user)

# @role_router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.RoleOut)
# def create_user(user: schemas.Role, db: Session = Depends(get_db))->Any:
#     return role_repository.create_role(user, db)

# @role_router.get('/{id}', response_model=schemas.RoleOut)
# def get_role(id: int, db: Session = Depends(get_db), current_user: int =Depends(oauth2.get_current_user))->Any:
#     return role_repository.get_one_role(id,db)

# @role_router.get('/', response_model=List[schemas.RoleOut])
# def get_all_role(db: Session = Depends(get_db),current_user: int =Depends(oauth2.get_current_user))->Any:
#     return role_repository.get_all_role(db)

# @role_router.put('/{id',response_model=schemas.RoleOut, )
# def update_role(role:schemas.RoleUpdate, id:int, db: Session= Depends(get_db),current_user: int = Depends(oauth2.get_current_user))->Any:
#     return role_repository.update_role(role,id,db,current_user)

# @role_router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_role(id:int, db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user)):
#     return role_repository.delete_role(id,db,current_user)
#     pass

# #
