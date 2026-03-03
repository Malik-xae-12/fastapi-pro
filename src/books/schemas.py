
from pydantic import BaseModel
import uuid
from datetime import datetime,date

class Book(BaseModel):
    uid:uuid.UUID
    title:str
    author:str
    publisher:str
    published_date:date
    page_count:int
    created_at :datetime
    update_at: datetime

class BookCreateModel(BaseModel):
    id:int
    title:str
    author:str
    publisher:str
    published_date:date
    page_count:int


class BookUpdateModel(BaseModel):
    id:int
    title:str
    author:str
    publisher:str
    page_count:int