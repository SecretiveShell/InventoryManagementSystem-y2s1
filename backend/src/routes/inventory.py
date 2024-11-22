from fastapi import APIRouter, HTTPException
from database.session import Session
from database.ORM import Book
from models.book import BookInstance
from auth.login import get_admin_depends

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
)


@router.get("/list")
async def view_inventory() -> list[BookInstance]:
    """
    Retrieve a list of all books in the store inventory.

    Returns:
        list[BookInstance]: A list of BookInstance objects representing the books in the inventory.
    """
    with Session() as session:
        books = session.query(Book).all()
        return [
            BookInstance.model_validate(book, from_attributes=True) for book in books
        ]


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
async def update_inventory(user: get_admin_depends, book_id: int, book_data: BookInstance) -> BookInstance:
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
