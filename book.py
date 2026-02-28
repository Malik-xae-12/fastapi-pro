from fastapi import FastAPI,status
from pydantic import BaseModel
from typing import List
from fastapi.exceptions import HTTPException

app = FastAPI()


books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "publisher": "O'Reilly Media",
        "published_date": "2020-05-15",
        "page_count": 850,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Python Crash Course",
        "author": "Eric Matthes",
        "publisher": "No Starch Press",
        "published_date": "2019-08-10",
        "page_count": 544,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Automate the Boring Stuff",
        "author": "Al Sweigart",
        "publisher": "No Starch Press",
        "published_date": "2018-04-14",
        "page_count": 592,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Effective Python",
        "author": "Brett Slatkin",
        "publisher": "Pearson",
        "published_date": "2021-03-30",
        "page_count": 480,
        "language": "English",
    },
    {
        "id": 7,
        "title": "Learning FastAPI",
        "author": "Abhishek Mishra",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2023-02-01",
        "page_count": 350,
        "language": "English",
    },
    {
        "id": 8,
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "publisher": "Prentice Hall",
        "published_date": "2008-08-11",
        "page_count": 464,
        "language": "English",
    },
    {
        "id": 9,
        "title": "The Pragmatic Programmer",
        "author": "Andrew Hunt",
        "publisher": "Addison-Wesley",
        "published_date": "2019-09-13",
        "page_count": 352,
        "language": "English",
    },
    {
        "id": 10,
        "title": "Deep Learning with Python",
        "author": "Francois Chollet",
        "publisher": "Manning Publications",
        "published_date": "2021-10-20",
        "page_count": 500,
        "language": "English",
    }
]


class Book(BaseModel):
    id:int
    title:str
    author:str
    publisher:str
    published_date:str
    page_count:int

class BookUpdateModel(BaseModel):
    id:int
    title:str
    author:str
    publisher:str
    page_count:int
    

@app.get('/books',response_model=List[Book])
async def get_all_books():
    return books

@app.post('/books',status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get('/book/{book_id}')
async def get_book(book_id:int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail='Book Not found')

@app.patch('/book/{book_id}')
async def update_book(book_id:int,book_update:BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['id'] = book_update.id
            book['title'] = book_update.title
            book['author'] = book_update.author
            book['publisher'] = book_update.publisher
            book['page_count'] = book_update.page_count
            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book Not Found")



@app.delete('/book/{book_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return 
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='book Not found')
