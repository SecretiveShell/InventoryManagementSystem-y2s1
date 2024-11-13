from pydantic import BaseModel
from typing import List
from datetime import datetime


# 1. Order Models

class OrderBase(BaseModel):
    order_date: datetime
    order_status: str
    shipping_address: str
    user_id: int
    books: List[int] = []  # List of book IDs in the order

class OrderCreate(OrderBase):
    """Model for creating a new order"""
    pass

class OrderStatusUpdate(BaseModel):
    order_status: str  # Status of the order (e.g., 'Pending', 'Shipped', 'Delivered')

class OrderResponse(OrderBase):
    order_id: int  # ID of the order
    
    class Config:
        orm_mode = True  # Tells Pydantic to read data even if it comes from an ORM model

class Order(OrderBase):
    order_id: int
    
    