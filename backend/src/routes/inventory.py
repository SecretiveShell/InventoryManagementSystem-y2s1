from fastapi import APIRouter, HTTPException
from database.session import Session
from database.ORM import Book

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
)

@router.get("/list")
async def view_inventory():
    """list store inventory"""
    with Session() as session:
        books = session.query(Book).all()
        return books
    
@router.get("/{book_id}")
async def view_inventory_for_book(book_id: int):
    """view inventory of a specific book"""
    with Session() as session:
        book = session.query(Book).filter(Book.book_id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="book not found")
        return book

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
async def remove_from_inventory(book_id: int):
    """remove a book from inventory"""
    with Session() as session:
        book = session.query(Book).filter(Book.book_id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="book not found")
        session.delete(book)
        session.commit()
        return book 
    
        
@router.put("/{book_id}")
async def update_inventory(book_id: int):
    """update inventory of a specific book"""
    with Session() as session:
        book = session.query(Book).filter(Book.book_id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="book not found")
        return book     
    
