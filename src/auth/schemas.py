from pydantic import BaseModel,Field
from datetime import datetime
import uuid
from typing import Optional,List
from src.books.schemas import Book



class UserCreateModel(BaseModel):
    first_name: str = Field(max_length=20)
    last_name: str = Field(max_length=20)
    username: str = Field(max_length=8)
    email: str = Field(max_length=40)
    password: str = Field(max_length=6)


class UserModel(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    id_verified: bool  
    created_at: datetime
    updated_at: datetime
    uid: uuid.UUID


class UserBooksModel(UserModel):
    books: List[Book]


class UserLoginModel(BaseModel):
    email:str
    password :str