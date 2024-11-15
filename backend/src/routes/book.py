from fastapi import APIRouter, HTTPException, Query
from models.book import Book as BookModel, BookCreate as BookCreateModel
from database.session import Session
from database.ORM import Book
from sqlalchemy import select
from typing import Optional
from math import ceil

router = APIRouter(
    prefix="/books",
    tags=["books"],
)

BOOKS_PER_PAGE = 7

@router.get("/get")
async def get_book(id: int) -> BookModel:
    """get info about a book"""
    with Session() as session:
        command = select(Book).where(Book.book_id == id)
        book_instance = session.execute(command).scalar_one_or_none()
        
        if book_instance is None:
            raise HTTPException(404, detail="book ID does not exist")
        
        return BookModel.model_validate(book_instance, from_attributes=True)

@router.get("/list")
async def list_books(
    page: int = 1,
    title: Optional[str] = Query(None, description="Search by title"),
    author: Optional[str] = Query(None, description="Filter by author"),
    genre: Optional[str] = Query(None, description="Filter by genre")
) -> dict:
    if page < 1:
        raise HTTPException(400, detail="Page number must be greater than 0")
    
    with Session() as session:
        # Start with base query
        query = select(Book)
        
        # Apply filters
        if title:
            query = query.where(Book.title.ilike(f"%{title}%"))
            
        if author:
            query = query.where(Book.author.ilike(f"%{author}%"))
            
        if genre:
            query = query.where(Book.genre == genre)
        
        # Get total count for pagination
        total_books = session.execute(query).all().__len__()
        total_pages = ceil(total_books / BOOKS_PER_PAGE)
        
        if page > total_pages and total_pages > 0:
            raise HTTPException(404, detail=f"Page {page} does not exist. Total pages: {total_pages}")
        
        # Calculate offset and apply pagination
        offset = (page - 1) * BOOKS_PER_PAGE
        query = query.offset(offset).limit(BOOKS_PER_PAGE)
        
        # Execute query
        books = session.execute(query).scalars().all()
        
        # Convert to Pydantic models
        book_list = [BookModel.model_validate(book, from_attributes=True) for book in books]
        
        # Get available genres for filter dropdown
        genres = session.execute(select(Book.genre).distinct()).scalars().all()
        
        return {
            "books": book_list,
            "pagination": {
                "current_page": page,
                "total_pages": total_pages,
                "total_books": total_books,
                "books_per_page": BOOKS_PER_PAGE,
                "has_next": page < total_pages,
                "has_previous": page > 1
            },
            "available_genres": genres
        }

@router.post("/add")
async def add_book(book: BookCreateModel) -> bool:
    """add a book"""
    with Session() as session:
        book_instance = Book(**book.model_dump())
        session.add(book_instance)
        session.commit()
        
    return True
