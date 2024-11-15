from pydantic import BaseModel
from typing import List, Annotated
from datetime import datetime

# 1. Order Models

class OrderBase(BaseModel):
    order_date: datetime
    order_status: Annotated[str, "Order status (e.g., 'Pending', 'Shipped', 'Delivered')"]
    user_id: int
    books: List[int] = []  # List of book IDs in the order

class OrderCreate(OrderBase):
    """Model for creating a new order"""
    pass

class OrderStatusUpdate(BaseModel):
    order_status: Annotated[str, "Order status (e.g., 'Pending', 'Shipped', 'Delivered')"]

class Order(OrderBase):
    order_id: int
    
    class Config:
        from_attributes = True

class OrderResponse(OrderBase):
    order_id: int  # ID of the order
    
    class Config:
        orm_mode = True  # Tells Pydantic to read data even if it comes from an ORM model


    
    