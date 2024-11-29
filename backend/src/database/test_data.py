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
book7 = Book(
    title="The Lord of the Rings",
    genre="Fantasy",
    ISBN="978-0-747-54614-8",
    publication_date="1937-12-21",
    publisher="George Allen & Unwin",
)
book8 = Book(
    title="To Kill a Mockingbird",
    genre="Fiction",
    ISBN="978-0-06-112008-4",
    publication_date="1960-07-11",
    publisher="J.B. Lippincott & Co.",
)
book9 = Book(
    title="The Catcher in the Rye",
    genre="Fiction",
    ISBN="978-0-316-76948-0",
    publication_date="1951-07-16",
    publisher="Little, Brown and Company",
)
book10 = Book(
    title="The Great Gatsby",
    genre="Fiction",
    ISBN="978-0-7432-7356-5",
    publication_date="1925-04-10",
    publisher="Charles Scribner's Sons",
)
book11 = Book(
    title="The Chronicles of Narnia",
    genre="Fantasy",
    ISBN="978-0-06-447119-0",
    publication_date="1950-10-16",
    publisher="Geoffrey Bles",
)
book12 = Book(
    title="Wuthering Heights",
    genre="Gothic Fiction",
    ISBN="978-0-14-143955-6",
    publication_date="1847-12-01",
    publisher="Thomas Cautley Newby",
)
book13 = Book(
    title="Brave New World",
    genre="Science Fiction",
    ISBN="978-0-06-085052-4",
    publication_date="1932-08-31",
    publisher="Chatto & Windus",
)
book14 = Book(
    title="The Picture of Dorian Gray",
    genre="Philosophical Fiction",
    ISBN="978-0-141-18672-8",
    publication_date="1890-06-20",
    publisher="Ward, Lock & Co.",
)
book15 = Book(
    title="The Odyssey",
    genre="Epic Poetry",
    ISBN="978-0-14-026886-7",
    publication_date="1721-10-01",
    publisher="Penguin Classics",
)
book16 = Book(
    title="Frankenstein",
    genre="Gothic Fiction",
    ISBN="978-0-14-143947-1",
    publication_date="1818-01-01",
    publisher="Lackington, Hughes, Harding, Mavor & Jones",
)
book17 = Book(
    title="Dracula",
    genre="Horror",
    ISBN="978-0-14-143984-6",
    publication_date="1897-05-26",
    publisher="Archibald Constable and Co.",
)
book18 = Book(
    title="The Road",
    genre="Post-apocalyptic Fiction",
    ISBN="978-0-307-26542-4",
    publication_date="2006-09-26",
    publisher="Alfred A. Knopf",
)
book19 = Book(
    title="The Shining",
    genre="Horror",
    ISBN="978-0-385-12167-5",
    publication_date="1977-01-28",
    publisher="Doubleday",
)
book20 = Book(
    title="The Alchemist",
    genre="Adventure",
    ISBN="978-0-06-112241-5",
    publication_date="1988-11-01",
    publisher="HarperCollins",
)


# add the books to the database
session.add(book1)
session.add(book2)
session.add(book3)
session.add(book4)
session.add(book5)
session.add(book6)
session.add(book7)
session.add(book8)
session.add(book9)
session.add(book10)
session.add(book11)
session.add(book12)
session.add(book13)
session.add(book14)
session.add(book15)
session.add(book16)
session.add(book17)
session.add(book18)
session.add(book19)
session.add(book20)

# Inventory
inventory1 = Inventory(book=book1, quantity_in_stock=10, price=12.99)
inventory2 = Inventory(book=book2, quantity_in_stock=5, price=14.99)
inventory3 = Inventory(book=book3, quantity_in_stock=15, price=9.99)
inventory4 = Inventory(book=book4, quantity_in_stock=20, price=8.99)
inventory5 = Inventory(book=book5, quantity_in_stock=30, price=7.99)
inventory6 = Inventory(book=book6, quantity_in_stock=40, price=6.99)
Inventory7 = Inventory(book=book7, quantity_in_stock=50, price=5.99)
Inventory8 = Inventory(book=book8, quantity_in_stock=60, price=4.99)
Inventory9 = Inventory(book=book9, quantity_in_stock=70, price=3.99)
Inventory10 = Inventory(book=book10, quantity_in_stock=80, price=2.99)
Inventory11 = Inventory(book=book11, quantity_in_stock=90, price=1.99)
Inventory12 = Inventory(book=book12, quantity_in_stock=100, price=0.99)
Inventory13 = Inventory(book=book13, quantity_in_stock=110, price=9.99)
Inventory14 = Inventory(book=book14, quantity_in_stock=120, price=8.99)
Inventory15 = Inventory(book=book15, quantity_in_stock=130, price=7.99)
Inventory16 = Inventory(book=book16, quantity_in_stock=140, price=6.99)
Inventory17 = Inventory(book=book17, quantity_in_stock=150, price=5.99)
Inventory18 = Inventory(book=book18, quantity_in_stock=160, price=4.99)
Inventory19 = Inventory(book=book19, quantity_in_stock=170, price=3.99)
Inventory20 = Inventory(book=book20, quantity_in_stock=180, price=2.99)

# add the inventory to the database
session.add(inventory1)
session.add(inventory2)
session.add(inventory3)
session.add(inventory4)
session.add(inventory5)
session.add(inventory6)
session.add(Inventory7)
session.add(Inventory8)
session.add(Inventory9)
session.add(Inventory10)
session.add(Inventory11)
session.add(Inventory12)
session.add(Inventory13)
session.add(Inventory14)
session.add(Inventory15)
session.add(Inventory16)
session.add(Inventory17)
session.add(Inventory18)
session.add(Inventory19)
session.add(Inventory20)

session.commit()
