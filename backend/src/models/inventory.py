from pydantic import BaseModel, Field
from typing import Optional

class InventoryUpdate(BaseModel):
    title: str
    quantity_in_stock: int = Field(ge=0)
    price: float = Field(ge=0.0)
    author: str
    ISBN: str
    token: str  # Added token field requirement

    class Config:
        from_attributes = True

class InventoryResponse(BaseModel):
    book_id: int
    title: str
    quantity_in_stock: int
    price: float
    author: str
    ISBN: str
    message: Optional[str] = None

    class Config:
        from_attributes = True