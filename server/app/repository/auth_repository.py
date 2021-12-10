from fastapi import  status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.config import oauth2
from app.utils import  utils
from app.models import users as models



def login(user_credentials: OAuth2PasswordRequestForm , db: Session ):

    user = db.query(models.User).filter((models.User.email == user_credentials.username) | (models.User.username == user_credentials.username)).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail=f"Invalid Credentials")

    # create a token
    # return token
    if user.user_role=='admin':
        permissions = "admin"
    elif user.user_role=='normal':
        permissions = "normal"
    else:
        permissions ="restricted"
    access_token = oauth2.create_access_token(data={"user_id": user.id, "permissions": permissions})

    return {"access_token": access_token, "token_type": "bearer"}
