from passlib.context import CryptContext

from app.repository import user_repository
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from app.models import users as models

def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



# def is_active( user: models.User)-> bool:
#     return user.is_active

# def is_superuser( user: models.User) -> bool:
    
#     return user.is_superuser