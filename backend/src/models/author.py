from typing import Literal
from pydantic import BaseModel, Field


class AuthorBase(BaseModel):
    name: str
    bio: str


class AuthorCreate(AuthorBase):
    pass


class AuthorResponse(AuthorBase):
    author_id: int

    class Config:
        orm_mode = True


class AuthorDeleteResponse(BaseModel):
    detail: Literal["Author deleted successfully"] = Field(
        "Author deleted successfully"
    )
