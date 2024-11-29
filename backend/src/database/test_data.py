from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, drop_database
from URI import DATABASE_URI
from ORM import Base, Book, Inventory

engine = create_engine(DATABASE_URI)

try:
    drop_database(engine.url)
except:
    print("Database does not exist -- not dropping")

create_database(engine.url)

Base.metadata.create_all(engine)

print("Tables created successfully.")

# Create test data
session = Session(bind=engine)

# Books
book1 = Book(
    title="The Hobbit",
    genre="Fantasy",
    ISBN="978-0-141-18785-5",
    publication_date="1937-12-21",
    publisher="George Allen & Unwin",
)
book2 = Book(
    title="Harry Potter and the Philosopher's Stone",
    genre="Fantasy",
    ISBN="978-0-747-54614-4",
    publication_date="1997-07-16",
    publisher="Bloomsbury",
)
book3 = Book(
    title="Pride and Prejudice",
    genre="Romance",
    ISBN="978-0-008-32741-7",
    publication_date="1813-01-10",
    publisher="Chapman & Hall",
)
book4 = Book(
    title="Murder on the Orient Express",
    genre="Crime",
    ISBN="978-0-261-10320-7",
    publication_date="1974-10-10",
    publisher="Penguin",
)
book5 = Book(
    title="Great Expectations",
    genre="Romance",
    ISBN="978-0-099-54913-6",
    publication_date="2005-10-01",
    publisher="Macmillan",
)
book6 = Book(
    title="1984",
    genre="Science Fiction",
    ISBN="978-0-747-54624-4",
    publication_date="1949-07-15",
    publisher="Penguin",
)

# add the books to the database
session.add(book1)
session.add(book2)
session.add(book3)
session.add(book4)
session.add(book5)
session.add(book6)

# Inventory
inventory1 = Inventory(book=book1, quantity_in_stock=10, price=12.99)
inventory2 = Inventory(book=book2, quantity_in_stock=5, price=14.99)
inventory3 = Inventory(book=book3, quantity_in_stock=15, price=9.99)
inventory4 = Inventory(book=book4, quantity_in_stock=20, price=8.99)
inventory5 = Inventory(book=book5, quantity_in_stock=30, price=7.99)
inventory6 = Inventory(book=book6, quantity_in_stock=40, price=6.99)

# add the inventory to the database
session.add(inventory1)
session.add(inventory2)
session.add(inventory3)
session.add(inventory4)
session.add(inventory5)
session.add(inventory6)

session.commit()
