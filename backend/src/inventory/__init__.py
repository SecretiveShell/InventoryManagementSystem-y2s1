from fastapi import APIRouter

router = APIRouter(
    prefix="/inventory",
    tags=["inventory"],
)

from . import list