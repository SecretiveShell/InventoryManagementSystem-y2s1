from pydantic import BaseModel, Field
from datetime import datetime

class BookBase(BaseModel):
    title: str = Field(title="title", description="the title of the book")
    genre: str = Field(title="genre", description="the genre of the book")
    ISBN: str = Field(title="ISBN", description="the internationally recognised identifier for the book")
    publication_date: datetime = Field(title="publication date", description="the date the book was published")
    publisher: str = Field(title="publisher", description="the name of the publisher who published the book")

class Book(BookBase):
    book_id: int = Field(title="book id", description="the globally unique book ID")

class BookCreate(BookBase):
    pass