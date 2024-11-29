from fastapi import APIRouter, HTTPException
from sqlalchemy import func
from database.session import Session
from database.ORM import Book
from models.book import BookInstance
from auth.login import get_admin_depends
from openapi_tags import OpenAPITags

router = APIRouter(
    prefix="/inventory",
    tags=[OpenAPITags.inventory.value],
)


@router.get("/list")
async def view_inventory(
    page: int = 1,  # Page number, minimum 1
    page_size: int = 7,  # Default 7 items per page, max 100
) -> dict:
    """
    Retrieve a paginated list of books in the store inventory.

    Args:
        page (int, optional): The page number to retrieve. Defaults to 1.
        page_size (int, optional): Number of items per page. Defaults to 7.

    Returns:
        dict: A dictionary containing:
            - books: List of BookInstance objects for the current page
            - total_books: Total number of books in the inventory
            - current_page: Current page number
            - total_pages: Total number of pages
    """
    with Session() as session:
        # Count total books
        total_books = session.query(func.count(Book.book_id)).scalar()
        
        # Calculate total pages
        total_pages = (total_books + page_size - 1) // page_size
        
        # Calculate offset
        offset = (page - 1) * page_size
        
        # Retrieve books for the current page
        books = (
            session.query(Book)
            .offset(offset)
            .limit(page_size)
            .all()
        )
        
        # Convert to BookInstance
        book_instances = [
            BookInstance.model_validate(book, from_attributes=True) 
            for book in books
        ]
        
        return {
            "books": book_instances,
            "total_books": total_books,
            "current_page": page,
            "total_pages": total_pages
        }


@router.get("/{book_id}")
async def view_inventory_for_book(book_id: int) -> BookInstance:
    """
    Retrieve the inventory details for a specific book.

    Args:
        book_id (int): The ID of the book to view.

    Returns:
        BookInstance: A BookInstance object representing the book in the inventory.

    Raises:
        HTTPException: If the book with the specified ID is not found.
    """
    with Session() as session:
        book = session.query(Book).filter(Book.book_id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        return BookInstance.model_validate(book, from_attributes=True)


@router.post("/{book_id}")
async def add_to_inventory(user: get_admin_depends, book_id: int) -> BookInstance:
    """
    Add a book to the inventory.

    Args:
        book_id (int): The ID of the book to add. Note: The book ID should be autoincrementing in the database.

    Returns:
        BookInstance: A BookInstance object representing the book that was added to the inventory.

    Raises:
        HTTPException: If the book with the specified ID is not found.
    """
    with Session() as session:
        book = session.query(Book).filter(Book.book_id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        session.add(book)
        session.commit()
        return BookInstance.model_validate(book, from_attributes=True)


@router.delete("/{book_id}")
async def remove_from_inventory(user: get_admin_depends, book_id: int) -> BookInstance:
    """
    Remove a book from the inventory.

    Args:
        book_id (int): The ID of the book to remove.

    Returns:
        BookInstance: A BookInstance object representing the book that was removed from the inventory.

    Raises:
        HTTPException: If the book with the specified ID is not found.
    """
    with Session() as session:
        book = session.query(Book).filter(Book.book_id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        session.delete(book)
        session.commit()
        return BookInstance.model_validate(book, from_attributes=True)


@router.put("/{book_id}")
async def update_inventory(
    user: get_admin_depends, book_id: int, book_data: BookInstance
) -> BookInstance:
    """
    Update the inventory details for a specific book.

    Args:
        book_id (int): The ID of the book to update.
        book_data (BookInstance): The updated book data.

    Returns:
        BookInstance: A BookInstance object representing the book that was updated in the inventory.

    Raises:
        HTTPException: If the book with the specified ID is not found.
    """
    with Session() as session:
        book = session.query(Book).filter(Book.book_id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")
        for key, value in book_data.model_dump().items():
            setattr(book, key, value)
        session.commit()
        return BookInstance.model_validate(book, from_attributes=True)
