from typing import List, Optional
from .user import User, UserCreate,UserOut
from datetime import datetime
from pydantic import BaseModel


class Role(BaseModel):
    name:str 

class RoleOut(BaseModel):
    id: int
    name: str
    created_at: datetime
    users: List[UserOut]
    class Config:
        orm_mode = True
        
class RoleUpdate(Role):
    pass
    