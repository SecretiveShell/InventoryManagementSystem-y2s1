"""
This module contains the API routes for managing authors in the inventory management system.
"""

from fastapi import APIRouter, HTTPException
from database.ORM import Author
from models.author import AuthorCreate, AuthorDeleteResponse, AuthorResponse
from database.session import Session
from auth.login import get_admin_depends
from openapi_tags import OpenAPITags


router = APIRouter(
    prefix="/authors",
    tags=[OpenAPITags.authors.value],
)


@router.post("/")
def create_author(user: get_admin_depends, author: AuthorCreate) -> AuthorResponse:
    """
    Create a new author.

    Args:
        author (AuthorCreate): The author data to create.

    Returns:
        AuthorResponse: The created author data.
    """
    with Session() as session:
        db_author = Author(**author.model_dump())
        session.add(db_author)
        session.commit()
        session.refresh(db_author)
        return db_author


@router.get("/")
def get_authors() -> list[AuthorResponse]:
    """
    Retrieve a list of all authors.

    Returns:
        list[AuthorResponse]: A list of all authors.
    """
    with Session() as session:
        authors = session.query(Author).all()

    response = [
        AuthorResponse.model_validate(author, from_attributes=True)
        for author in authors
    ]
    return response


@router.get("/{author_id}")
def get_author(author_id: int) -> AuthorResponse:
    """
    Retrieve an author by ID.

    Args:
        author_id (int): The ID of the author to retrieve.

    Returns:
        AuthorResponse: The author data.

    Raises:
        HTTPException: If the author is not found.
    """
    with Session() as session:
        author = session.query(Author).filter(Author.author_id == author_id).first()

    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")

    return AuthorResponse.model_validate(author, from_attributes=True)


@router.put("/{author_id}", response_model=AuthorResponse)
def update_author(
    user: get_admin_depends, author_id: int, author: AuthorCreate
) -> AuthorResponse:
    """
    Update an author by ID.

    Args:
        author_id (int): The ID of the author to update.
        author (AuthorCreate): The updated author data.

    Returns:
        AuthorResponse: The updated author data.

    Raises:
        HTTPException: If the author is not found.
    """
    with Session() as session:
        db_author = session.query(Author).filter(Author.author_id == author_id).first()
        if db_author is None:
            raise HTTPException(status_code=404, detail="Author not found")
        for key, value in author.dict().items():
            setattr(db_author, key, value)
        session.commit()
        session.refresh(db_author)
        return db_author


@router.delete("/{author_id}")
def delete_author(user: get_admin_depends, author_id: int) -> AuthorDeleteResponse:
    """
    Delete an author by ID.

    Args:
        author_id (int): The ID of the author to delete.

    Returns:
        AuthorDeleteResponse: A response indicating the deletion.

    Raises:
        HTTPException: If the author is not found.
    """
    with Session() as session:
        db_author = session.query(Author).filter(Author.author_id == author_id).first()
        if db_author is None:
            raise HTTPException(status_code=404, detail="Author not found")
        session.delete(db_author)
        session.commit()
        return AuthorDeleteResponse()
