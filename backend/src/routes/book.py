"""
This module contains the API routes for managing books in the inventory management system.
"""

from fastapi import APIRouter, HTTPException
from database.ORM import Book
from models.book import BookCreate, BookDeleteResponse, BookResponse
from database.session import Session
from auth.login import get_admin_depends
from openapi_tags import OpenAPITags


router = APIRouter(
    prefix="/books",
    tags=[OpenAPITags.books.value],
)


@router.post("/")
def create_book(user: get_admin_depends, book: BookCreate) -> BookResponse:
    """
    Create a new book.

    Args:
        book (BookCreate): The book data to create.

    Returns:
        BookResponse: The created book data.
    """
    with Session() as session:
        db_book = Book(**book.model_dump())
        session.add(db_book)
        session.commit()
        session.refresh(db_book)
        return db_book


@router.get("/")
def get_books() -> list[BookResponse]:
    """
    Retrieve a list of all books.

    Returns:
        list[BookResponse]: A list of all books.
    """
    with Session() as session:
        books = session.query(Book).all()

    response = [
        BookResponse.model_validate(book, from_attributes=True) for book in books
    ]
    return response


@router.get("/{book_id}")
def get_book(book_id: int) -> BookResponse:
    """
    Retrieve a book by ID.

    Args:
        book_id (int): The ID of the book to retrieve.

    Returns:
        BookResponse: The book data.

    Raises:
        HTTPException: If the book is not found.
    """
    with Session() as session:
        book = session.query(Book).filter(Book.book_id == book_id).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return BookResponse.model_validate(book, from_attributes=True)


@router.put("/{book_id}", response_model=BookResponse)
def update_book(user: get_admin_depends, book_id: int, book: BookCreate) -> BookResponse:
    """
    Update a book by ID.

    Args:
        book_id (int): The ID of the book to update.
        book (BookCreate): The updated book data.

    Returns:
        BookResponse: The updated book data.

    Raises:
        HTTPException: If the book is not found.
    """
    with Session() as session:
        db_book = session.query(Book).filter(Book.book_id == book_id).first()
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        for key, value in book.dict().items():
            setattr(db_book, key, value)
        session.commit()
        session.refresh(db_book)
        return db_book


@router.delete("/{book_id}")
def delete_book(user: get_admin_depends, book_id: int) -> BookDeleteResponse:
    """
    Delete a book by ID.

    Args:
        book_id (int): The ID of the book to delete.

    Returns:
        BookDeleteResponse: A response indicating the deletion.

    Raises:
        HTTPException: If the book is not found.
    """
    with Session() as session:
        db_book = session.query(Book).filter(Book.book_id == book_id).first()
        if db_book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        session.delete(db_book)
        session.commit()
        return BookDeleteResponse()
