from fastapi import APIRouter, HTTPException
from sqlalchemy import func
from database.session import Session
from database.ORM import Book, Inventory
from models.book import BookInstance
from auth.login import get_admin_depends
from openapi_tags import OpenAPITags
from typing import Optional
from pydantic import BaseModel


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

        # Retrieve books with their inventory information
        books = (
            session.query(Book, Inventory)
            .join(Inventory)
            .offset(offset)
            .limit(page_size)
            .all()
        )

        # Convert to BookInstance with inventory and author data
        book_instances = []
        for book, inventory in books:
            book_dict = BookInstance.model_validate(
                book, from_attributes=True
            ).model_dump()
            book_dict["quantity_in_stock"] = inventory.quantity_in_stock
            book_dict["price"] = inventory.price

            # Add author information
            authors = []
            for author in book.authors:
                author_info = {
                    "author_id": author.author_id,
                    "name": author.name,
                    "bio": author.bio,
                }
                authors.append(author_info)
            book_dict["authors"] = authors

            book_instances.append(BookInstance(**book_dict))

        return {
            "books": book_instances,
            "total_books": total_books,
            "current_page": page,
            "total_pages": total_pages,
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
        # Query book with inventory information
        result = (
            session.query(Book, Inventory)
            .join(Inventory)
            .filter(Book.book_id == book_id)
            .first()
        )

        if result is None:
            raise HTTPException(status_code=404, detail="Book not found")

        book, inventory = result

        # Create book dictionary with inventory data
        book_dict = BookInstance.model_validate(book, from_attributes=True).model_dump()
        book_dict["quantity_in_stock"] = inventory.quantity_in_stock
        book_dict["price"] = inventory.price

        # Add author information
        authors = []
        for author in book.authors:
            author_info = {
                "author_id": author.author_id,
                "name": author.name,
                "bio": author.bio,
            }
            authors.append(author_info)
        book_dict["authors"] = authors

        return BookInstance(**book_dict)


class InventoryUpdate(BaseModel):
    quantity_in_stock: Optional[int] = None
    price: Optional[float] = None


@router.post("/{book_id}")
async def add_to_inventory(
    user: get_admin_depends, book_id: int, inventory_data: InventoryUpdate
) -> BookInstance:
    """
    Add or update a book in the inventory.

    Args:
        book_id (int): The ID of the book to add/update
        inventory_data (InventoryUpdate): The inventory data to update

    Returns:
        BookInstance: A BookInstance object representing the book that was added/updated in the inventory.

    Raises:
        HTTPException: If the book with the specified ID is not found.
    """
    with Session() as session:
        # Check if book exists
        book = session.query(Book).filter(Book.book_id == book_id).first()
        if book is None:
            raise HTTPException(status_code=404, detail="Book not found")

        # Get or create inventory entry
        inventory = (
            session.query(Inventory).filter(Inventory.book_id == book_id).first()
        )
        if inventory is None:
            inventory = Inventory(
                book_id=book_id,
                quantity_in_stock=inventory_data.quantity_in_stock or 0,
                price=inventory_data.price or 0.0,
            )
            session.add(inventory)
        else:
            # Update existing inventory
            if inventory_data.quantity_in_stock is not None:
                inventory.quantity_in_stock = inventory_data.quantity_in_stock
            if inventory_data.price is not None:
                inventory.price = inventory_data.price

        session.commit()
        session.refresh(inventory)

        # Prepare response
        book_dict = BookInstance.model_validate(book, from_attributes=True).model_dump()
        book_dict["quantity_in_stock"] = inventory.quantity_in_stock
        book_dict["price"] = inventory.price

        # Add author information
        authors = []
        for author in book.authors:
            author_info = {
                "author_id": author.author_id,
                "name": author.name,
                "bio": author.bio,
            }
            authors.append(author_info)
        book_dict["authors"] = authors

        return BookInstance(**book_dict)


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
        # Query both book and inventory
        result = (
            session.query(Book, Inventory)
            .join(Inventory)
            .filter(Book.book_id == book_id)
            .first()
        )

        if result is None:
            raise HTTPException(status_code=404, detail="Book not found")

        book, inventory = result

        # Create response before deletion
        book_dict = BookInstance.model_validate(book, from_attributes=True).model_dump()
        book_dict["quantity_in_stock"] = inventory.quantity_in_stock
        book_dict["price"] = inventory.price

        # Add author information
        authors = []
        for author in book.authors:
            author_info = {
                "author_id": author.author_id,
                "name": author.name,
                "bio": author.bio,
            }
            authors.append(author_info)
        book_dict["authors"] = authors

        # Remove from inventory
        session.delete(inventory)
        session.commit()

        return BookInstance(**book_dict)


@router.put("/{book_id}")
async def update_inventory(
    book_id: int, 
    inventory_data: InventoryUpdate
) -> BookInstance:
    """
    Update the inventory details for a specific book.

    Args:
        book_id (int): The ID of the book to update.
        inventory_data (InventoryUpdate): The updated inventory data.

    Returns:
        BookInstance: A BookInstance object representing the book that was updated in the inventory.

    Raises:
        HTTPException: If the book with the specified ID is not found.
    """
    with Session() as session:
        # Query both book and inventory
        result = (
            session.query(Book, Inventory)
            .join(Inventory)
            .filter(Book.book_id == book_id)
            .first()
        )

        if result is None:
            raise HTTPException(status_code=404, detail="Book not found")

        book, inventory = result

        # Update inventory fields
        if inventory_data.quantity_in_stock is not None:
            inventory.quantity_in_stock = inventory_data.quantity_in_stock
        if inventory_data.price is not None:
            inventory.price = inventory_data.price

        session.commit()
        session.refresh(inventory)

        # Prepare response
        book_dict = BookInstance.model_validate(book, from_attributes=True).model_dump()
        book_dict["quantity_in_stock"] = inventory.quantity_in_stock
        book_dict["price"] = inventory.price

        # Add author information
        authors = []
        for author in book.authors:
            author_info = {
                "author_id": author.author_id,
                "name": author.name,
                "bio": author.bio,
            }
            authors.append(author_info)
        book_dict["authors"] = authors

        return BookInstance(**book_dict)