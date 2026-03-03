
from fastapi import APIRouter,status , Depends
from typing import List
from fastapi.exceptions import HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.service import BookService
from src.books.schemas import Book,BookUpdateModel
from src.db.main import get_session

book_router = APIRouter()    
book_service = BookService()

@book_router.get('/',response_model=List[Book])
async def get_all_books(session:AsyncSession = Depends(get_session)):
    books = book_service.get_all_books(session)
    return books

@book_router.post('/',status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data:Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@book_router.get('/{book_id}')
async def get_book(book_id:int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail='Book Not found')

@book_router.patch('/{book_id}')
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



@book_router.delete('/{book_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return 
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='book Not found')
