from fastapi import APIRouter, HTTPException
from database.session import Session
from database.ORM import Book
from models.book import BookInstance

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
)


@router.get("/list")
async def view_inventory() -> list[BookInstance]:
    """list store inventory"""
    with Session() as session:
        books = session.query(Book).all()
        return [BookInstance.model_validate(book, from_attributes=True) for book in books]


@router.get("/{book_id}")
async def view_inventory_for_book(book_id: int) -> BookInstance:
    """view inventory of a specific book"""
    with Session() as session:
        book = session.query(Book).filter(Book.book_id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="book not found")
        return BookInstance.model_validate(book, from_attributes=True)


# FIXME:
#   1) I do not think this is correct
#   2) I am fairly sure this will break because the return is not a pydantic model
#   3) book ID should be autoincrementing in the database
@router.post("/{book_id}")
async def add_to_inventory(book_id: int):
    """add a book to inventory"""
    with Session() as session:
        book = session.query(Book).filter(Book.book_id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="book not found")
        session.add(book)
        session.commit()
        return book


@router.delete("/{book_id}")
async def remove_from_inventory(book_id: int) -> BookInstance:
    """remove a book from inventory"""
    with Session() as session:
        book = session.query(Book).filter(Book.book_id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="book not found")
        session.delete(book)
        session.commit()
        return BookInstance.model_validate(book, from_attributes=True)


# FIXME
#   1) this does not actually update the inventory
@router.put("/{book_id}")
async def update_inventory(book_id: int):
    """update inventory of a specific book"""
    with Session() as session:
        book = session.query(Book).filter(Book.book_id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="book not found")
        return book
