from .router import router
from models import Book as BookModel
from database.session import Session
from database.ORM import Book
from sqlalchemy import select
from fastapi import HTTPException

@router.get("/get")
async def get_book(id: int) -> BookModel:
    with Session() as session:
        command = select(Book).where(Book.book_id == id)
        book_instance = session.execute(command).scalar_one_or_none() 

    if book_instance is None:
        raise HTTPException(404, detail="book ID does not exist")
 
    return BookModel.model_validate(book_instance, from_attributes=True)
