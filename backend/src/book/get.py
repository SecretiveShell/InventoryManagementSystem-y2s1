from .router import router
from models import Book

@router.get("/get")
async def get_book(id: int) -> Book:
    pass
