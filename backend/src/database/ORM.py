from sqlalchemy import Column, Integer, String, Date, Boolean, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Association tables for many-to-many relationships
book_category_association = Table(
    "book_category",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.book_id"), primary_key=True),
    Column(
        "category_id", Integer, ForeignKey("categories.category_id"), primary_key=True
    ),
)

order_book_association = Table(
    "order_book",
    Base.metadata,
    Column("order_id", Integer, ForeignKey("orders.order_id"), primary_key=True),
    Column("book_id", Integer, ForeignKey("books.book_id"), primary_key=True),
    Column("quantity", Integer, nullable=False),
)

book_author_association = Table(
    "book_author",
    Base.metadata,
    Column("book_id", Integer, ForeignKey("books.book_id"), primary_key=True),
    Column("author_id", Integer, ForeignKey("authors.author_id"), primary_key=True),
)


# data tables
class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    address = Column(String)
    phone_number = Column(String)
    date_joined = Column(Date, nullable=False)
    is_admin = Column(Boolean, default=False)

    orders = relationship("Order", back_populates="user")


class Order(Base):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True)
    order_date = Column(Date, nullable=False)
    order_status = Column(String, nullable=False)
    shipping_address = Column(String)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    user = relationship("User", back_populates="orders")
    books = relationship(
        "Book", secondary=order_book_association, back_populates="orders"
    )


class Book(Base):
    __tablename__ = "books"

    book_id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    ISBN = Column(String, unique=True)
    publication_date = Column(Date)
    publisher = Column(String)

    inventory = relationship("Inventory", back_populates="book")
    categories = relationship(
        "Category", secondary=book_category_association, back_populates="books"
    )
    authors = relationship(
        "Author", secondary=book_author_association, back_populates="books"
    )
    orders = relationship(
        "Order", secondary=order_book_association, back_populates="books"
    )


class Inventory(Base):
    __tablename__ = "inventory"

    inventory_id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.book_id"), nullable=False)
    quantity_in_stock = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)

    book = relationship("Book", back_populates="inventory")


class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    description = Column(String)

    books = relationship(
        "Book", secondary=book_category_association, back_populates="categories"
    )


class Author(Base):
    __tablename__ = "authors"

    author_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    bio = Column(String)

    books = relationship(
        "Book", secondary=book_author_association, back_populates="authors"
    )


# Logic to create tables
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy_utils import database_exists, create_database
    from URI import DATABASE_URI

    engine = create_engine(DATABASE_URI)
    if not database_exists(engine.url):
        create_database(engine.url)

    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)

    print("Tables created successfully.")
