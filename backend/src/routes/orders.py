from fastapi import APIRouter, HTTPException
from models.orders import (
    Order as OrderModel,
    OrderCreate as OrderCreateModel,
    OrderStatusUpdate,
)
from models.book import BookResponse
from database.session import Session
from database.ORM import Order, Book
from sqlalchemy import select
from datetime import datetime
from openapi_tags import OpenAPITags


router = APIRouter(
    prefix="/orders",
    tags=[OpenAPITags.orders.value],
)

# FIXME: Add auth to this file


# 1. Get all orders
@router.get("/get")
async def get_orders() -> list[OrderModel]:
    """Get all orders"""
    with Session() as session:
        command = select(Order)
        orders = session.execute(command).scalars().all()

    return [OrderModel.model_validate(order, from_attributes=True) for order in orders]


# 2. Get details of a specific order
@router.get("/get/{order_id}")
async def get_order(order_id: int) -> OrderModel:
    """Get details of a specific order"""
    with Session() as session:
        command = select(Order).where(Order.order_id == order_id)
        order_instance = session.execute(command).scalar_one_or_none()

    if order_instance is None:
        raise HTTPException(404, detail="Order ID does not exist")

    return OrderModel.model_validate(order_instance, from_attributes=True)


# 3. Create a new order
@router.post("/add")
async def add_order(order: OrderCreateModel) -> OrderModel:
    """Create a new order"""
    with Session() as session:
        # Check if the books exist in the database
        books = (
            session.execute(select(Book).where(Book.book_id.in_(order.books)))
            .scalars()
            .all()
        )
        if len(books) != len(order.books):
            raise HTTPException(404, detail="One or more books not found")

        # Create the order
        new_order = Order(
            order_date=datetime.now(), order_status="Pending", user_id=order.user_id
        )

        session.add(new_order)
        session.commit()
        session.refresh(new_order)

        # Add books to the order
        for book_id in order.books:
            book_instance = session.execute(
                select(Book).where(Book.book_id == book_id)
            ).scalar_one()
            new_order.books.append(book_instance)

        session.commit()

    return OrderModel.model_validate(new_order, from_attributes=True)


# 4. Update the status of an order
@router.put("/update/{order_id}")
async def update_order_status(
    order_id: int, order_status: OrderStatusUpdate
) -> OrderModel:
    """Update the status of an order"""
    with Session() as session:
        order_instance = session.execute(
            select(Order).where(Order.order_id == order_id)
        ).scalar_one_or_none()

        if order_instance is None:
            raise HTTPException(404, detail="Order ID does not exist")

        # Fix: Use setattr to update the attribute
        setattr(order_instance, "order_status", order_status.order_status)
        # Alternative fix:
        # order_instance._order_status = order_status.order_status

        session.commit()
        session.refresh(order_instance)

    return OrderModel.model_validate(order_instance, from_attributes=True)


# 5. Delete an order (cancel order)
@router.delete("/delete/{order_id}", response_model=bool)
async def delete_order(order_id: int) -> bool:
    """Delete an order"""
    with Session() as session:
        command = select(Order).where(Order.order_id == order_id)
        order_instance = session.execute(command).scalar_one_or_none()

        if order_instance is None:
            raise HTTPException(404, detail="Order ID does not exist")

        session.delete(order_instance)
        session.commit()

    return True


# 6. Get books in a specific order
@router.get("/get/{order_id}/books")
async def get_books_in_order(order_id: int) -> list[BookResponse]:
    """Get the list of books in a specific order"""
    with Session() as session:
        command = select(Order).where(Order.order_id == order_id)
        order_instance = session.execute(command).scalar_one_or_none()

        if order_instance is None:
            raise HTTPException(404, detail="Order ID does not exist")

        # Return the books related to this order
        return [
            BookResponse.model_validate(book, from_attributes=True)
            for book in order_instance.books
        ]
