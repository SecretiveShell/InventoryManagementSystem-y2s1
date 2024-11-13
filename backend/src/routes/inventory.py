from fastapi import APIRouter, HTTPException
from models.book import Book as BookModel
from database.session import Session
from database.ORM import Book
from sqlalchemy import select

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
)

@router.get("/list")
async def view_inventory():
    """list store inventory"""
    pass