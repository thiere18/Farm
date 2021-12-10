from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    username: str 
    email: EmailStr
    password: str
    created_at: datetime


# Properties to receive via API on creation
class UserCreate(BaseModel):
    username: str 
    email: EmailStr
    password: str
    user_role: str



# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None
    class Config:
        orm_mode = True

# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
class UserOut(BaseModel):
    id:int
    username: str 
    email: EmailStr
    user_role: str
    
    class Config:
        orm_mode = True
