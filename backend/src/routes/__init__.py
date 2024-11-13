from fastapi import APIRouter
from .book import router as book_router
from .inventory import router as inventory_router

router = APIRouter(
    prefix="/api",
)

router.include_router(book_router)
router.include_router(inventory_router)