from fastapi import APIRouter, HTTPException
from database.ORM import Author
from models.author import AuthorCreate, AuthorDeleteResponse, AuthorResponse
from database.session import Session


router = APIRouter(
    prefix="/authors",
    tags=["authors"],
)


@router.post("/")
def create_author(author: AuthorCreate) -> AuthorResponse:
    with Session() as session:
        db_author = Author(**author.model_dump())
        session.add(db_author)
        session.commit()
        session.refresh(db_author)
        return db_author


@router.get("/")
def get_authors() -> list[AuthorResponse]:
    with Session() as session:
        authors = session.query(Author).all()

    response = [AuthorResponse.model_validate(author, from_attributes=True) for author in authors]
    return response


@router.get("/{author_id}")
def get_author(author_id: int) -> AuthorResponse:
    with Session() as session:
        author = session.query(Author).filter(Author.author_id == author_id).first()

    if author is None:
        raise HTTPException(status_code=404, detail="Author not found")
    
    return AuthorResponse.model_validate(author, from_attributes=True)

# FIXME:
#   1) what does this even do?
#   2) can we please not use deprecated pydantic methods
#   3) I am fairly sure this will break because the return is not a pydantic model
@router.put("/{author_id}", response_model=AuthorResponse)
def update_author(author_id: int, author: AuthorCreate):
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
def delete_author(author_id: int):
    with Session() as session:
        db_author = session.query(Author).filter(Author.author_id == author_id).first()
        if db_author is None:
            raise HTTPException(status_code=404, detail="Author not found")
        session.delete(db_author)
        session.commit()
        return AuthorDeleteResponse()
