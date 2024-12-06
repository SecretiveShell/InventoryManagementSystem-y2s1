from pydantic import BaseModel, Field
from datetime import datetime

class BookBase(BaseModel):
    title: str = Field(title="title", description="the title of the book")
    genre: str = Field(title="genre", description="the genre of the book")
    ISBN: str = Field(
        title="ISBN",
        description="the internationally recognised identifier for the book",
    )
    publication_date: datetime = Field(
        title="publication date", description="the date the book was published"
    )
    publisher: str = Field(
        title="publisher",
        description="the name of the publisher who published the book",
    )

class BookInstance(BookBase):
    book_id: int = Field(title="book id", description="the globally unique book ID")
    quantity_in_stock: int = Field(default=0, description="current quantity in stock")
    price: float = Field(default=0.0, description="current price of the book")


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    book_id: int = Field(title="book id", description="the globally unique book ID")


class BookDeleteResponse(BaseModel):
    detail: str = Field("Book deleted successfully")
