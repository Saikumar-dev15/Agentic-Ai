from pydantic import BaseModel, Field, conint
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        from_attributes = True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id : int
    owner : UserOut

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    email: str
    password: str


    
class UserLogin(BaseModel):
    email: str
    password : str
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None


    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)