from fastapi import FastAPI,Header
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
async def main():
    return {"message":"Hello World!"}


@app.get("/greet/{name}")
async def greet(name:str):
    return {"message":f"hello {name}","age":f"{age}"}


# pass Multiple Query Parameters
@app.get("/greet")
async def greet(name:Optional[str]="malik",age:Optional[int]=22):
    return {"message":f"hello {name}","age":f"{age}"}    


class BookCreateModel(BaseModel):
    title : str
    author : str
    records : int



@app.post('/create_book')
async def create_book(book_data:BookCreateModel):
    return {
        "title":book_data.title,
        "author":book_data.author,
        "records" :book_data.records
    }


@app.get('/get_headers',status_code=201)
async def get_headers(
    accept:str=Header(None),
    content_type:str = Header(None),
    host:str = Header(None),
    user_agent:str= Header(None)
):
    request_headers={}
    request_headers["Accept"] = accept
    request_headers['Content-Type']=content_type
    request_headers['host'] = host
    request_headers['User-Agent'] = user_agent
    return request_headers


