"""
This module initializes the API routers for the Inventory Management System.

It includes routers for handling book, inventory, author, and orders operations.
"""
from fastapi import APIRouter
from .book import router as book_router
from .inventory import router as inventory_router
from .author import router as author_router
from .orders import router as orders_router

router = APIRouter(
    prefix="/api",
)

router.include_router(book_router)
router.include_router(inventory_router)
router.include_router(author_router)
router.include_router(orders_router)
