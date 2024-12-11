import hashlib
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, drop_database
from URI import DATABASE_URI
from ORM import Base, Book, Category, Inventory, Author, User

engine = create_engine(DATABASE_URI)

try:
    drop_database(engine.url)
except Exception:
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

user1 = User(
    name="John Doe",
    email="john.doe@example.com",
    password=hashlib.blake2b(b"password123", digest_size=64).hexdigest(),
    address="123 Main St, Anytown, USA",
    phone_number="555-1234",
    date_joined=date(2020, 1, 1),
    is_admin=False,
)

user2 = User(
    name="Jane Smith",
    email="jane.smith@example.com",
    password=hashlib.blake2b(b"password123", digest_size=64).hexdigest(),
    address="456 Elm St, Othertown, USA",
    phone_number="555-5678",
    date_joined=date(2021, 2, 15),
    is_admin=True,
)

user3 = User(
    name="Alice Johnson",
    email="alice.johnson@example.com",
    password=hashlib.blake2b(b"password123", digest_size=64).hexdigest(),
    address="789 Oak St, Sometown, USA",
    phone_number="555-9012",
    date_joined=date(2019, 5, 20),
    is_admin=False,
)

user4 = User(
    name="Bob Brown",
    email="bob.brown@example.com",
    password="password321",
    address="321 Pine St, Anycity, USA",
    phone_number="555-3456",
    date_joined=date(2018, 7, 10),
    is_admin=False,
)

# Add new categories to the database
category1 = Category(
    name="Kids",
    description="Books suitable for children, often with simple themes and illustrations.",
)
category2 = Category(
    name="Young Adult",
    description="Books targeted at young adult readers, typically between 12 and 18 years old.",
)
category3 = Category(
    name="Adult",
    description="Books intended for adult readers, with mature themes and complex storylines.",
)
category4 = Category(
    name="Classic",
    description="Books that are considered exemplary or noteworthy, often studied in literature classes.",
)
category5 = Category(
    name="Fantasy",
    description="Books that contain magical elements or are set in imaginary worlds.",
)
category6 = Category(
    name="Science Fiction",
    description="Books that explore futuristic or scientific concepts and technology.",
)
category7 = Category(
    name="Romance",
    description="Books that focus on romantic relationships as their central theme.",
)
category8 = Category(
    name="Horror",
    description="Books designed to create a sense of fear, suspense, and shock in the reader.",
)
category9 = Category(
    name="Historical Fiction",
    description="Books that are set in a specific historical time period and often include historical events.",
)
category10 = Category(
    name="Mystery",
    description="Books that involve a detective or investigator solving a crime or puzzle.",
)
category11 = Category(
    name="Adventure",
    description="Books with exciting and often dangerous journeys or quests.",
)

# example authors
author1 = Author(name="Charles Dickens", bio="some guy who wrote books.")
author2 = Author(
    name="Jane Austen", bio="Famous for her novels exploring the British landed gentry."
)
author3 = Author(
    name="Mark Twain",
    bio="An American author known for 'The Adventures of Tom Sawyer' and 'Adventures of Huckleberry Finn'.",
)
author4 = Author(
    name="George Orwell",
    bio="English writer known for his novels '1984' and 'Animal Farm', focusing on social justice and political themes.",
)
author5 = Author(
    name="Virginia Woolf",
    bio="English author and modernist, best known for 'Mrs. Dalloway' and 'To the Lighthouse'.",
)
author6 = Author(
    name="F. Scott Fitzgerald",
    bio="American novelist best known for 'The Great Gatsby', exploring themes of decadence and the American Dream.",
)
author7 = Author(
    name="J.K. Rowling",
    bio="British author famous for creating the Harry Potter series.",
)
author8 = Author(
    name="Hemingway",
    bio="American novelist known for his terse writing style and works like 'The Old Man and the Sea' and 'A Farewell to Arms'.",
)
author9 = Author(
    name="Leo Tolstoy",
    bio="Russian author of 'War and Peace' and 'Anna Karenina', focusing on philosophical and social issues.",
)
author10 = Author(
    name="Harper Lee",
    bio="American author of 'To Kill a Mockingbird', a novel on racial injustice in the Southern United States.",
)

# add the authors to the database
session.add(author1)
session.add(author2)
session.add(author3)
session.add(author4)
session.add(author5)
session.add(author6)
session.add(author7)
session.add(author8)
session.add(author9)
session.add(author10)

# add the users to the database
session.add(user1)
session.add(user2)
session.add(user3)
session.add(user4)

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

# Categories
session.add(category1)
session.add(category2)
session.add(category3)
session.add(category4)
session.add(category5)
session.add(category6)
session.add(category7)
session.add(category8)
session.add(category9)
session.add(category10)
session.add(category11)

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

# Associate authors with books
book1.authors.append(
    author1
)  # The Hobbit by J.R.R. Tolkien, associating it with Author1
book2.authors.append(
    author7
)  # Harry Potter and the Philosopher's Stone by J.K. Rowling
book3.authors.append(author2)  # Pride and Prejudice by Jane Austen
book4.authors.append(author10)  # Murder on the Orient Express by Agatha Christie
book5.authors.append(author1)  # Great Expectations by Charles Dickens
book6.authors.append(author4)  # 1984 by George Orwell
book7.authors.append(author1)  # The Lord of the Rings by J.R.R. Tolkien
book8.authors.append(author10)  # To Kill a Mockingbird by Harper Lee
book9.authors.append(author8)  # The Catcher in the Rye by J.D. Salinger
book10.authors.append(author6)  # The Great Gatsby by F. Scott Fitzgerald
book11.authors.append(author1)  # The Chronicles of Narnia by C.S. Lewis
book12.authors.append(author2)  # Wuthering Heights by Emily Brontë
book13.authors.append(author4)  # Brave New World by Aldous Huxley
book14.authors.append(author3)  # The Picture of Dorian Gray by Oscar Wilde
book15.authors.append(author2)  # The Odyssey by Homer
book16.authors.append(author2)  # Frankenstein by Mary Shelley
book17.authors.append(author3)  # Dracula by Bram Stoker
book18.authors.append(author4)  # The Road by Cormac McCarthy
book19.authors.append(author3)  # The Shining by Stephen King
book20.authors.append(author5)  # The Alchemist by Paulo Coelho

# Assign categories to books
book1.categories.append(category5)  # The Hobbit - Fantasy
book1.categories.append(category9)  # The Hobbit - Adventure
book1.categories.append(category1)  # The Hobbit - Kids

book2.categories.append(category5)  # Harry Potter - Fantasy
book2.categories.append(category2)  # Harry Potter - Young Adult
book2.categories.append(category7)  # Harry Potter - Romance

book3.categories.append(category7)  # Pride and Prejudice - Romance
book3.categories.append(category4)  # Pride and Prejudice - Classic

book4.categories.append(category10)  # Murder on the Orient Express - Mystery
book4.categories.append(category3)  # Murder on the Orient Express - Adult

book5.categories.append(category7)  # Great Expectations - Romance
book5.categories.append(category4)  # Great Expectations - Classic

book6.categories.append(category6)  # 1984 - Science Fiction
book6.categories.append(category3)  # 1984 - Adult
book6.categories.append(category4)  # 1984 - Classic

book7.categories.append(category5)  # The Lord of the Rings - Fantasy
book7.categories.append(category9)  # The Lord of the Rings - Adventure
book7.categories.append(category1)  # The Lord of the Rings - Kids

book8.categories.append(category7)  # To Kill a Mockingbird - Romance
book8.categories.append(category3)  # To Kill a Mockingbird - Adult
book8.categories.append(category4)  # To Kill a Mockingbird - Classic

book9.categories.append(category3)  # The Catcher in the Rye - Adult
book9.categories.append(category4)  # The Catcher in the Rye - Classic

book10.categories.append(category3)  # The Great Gatsby - Adult
book10.categories.append(category4)  # The Great Gatsby - Classic

book11.categories.append(category5)  # The Chronicles of Narnia - Fantasy
book11.categories.append(category9)  # The Chronicles of Narnia - Adventure
book11.categories.append(category1)  # The Chronicles of Narnia - Kids

book12.categories.append(category4)  # Wuthering Heights - Classic
book12.categories.append(category3)  # Wuthering Heights - Adult
book12.categories.append(category7)  # Wuthering Heights - Romance

book13.categories.append(category6)  # Brave New World - Science Fiction
book13.categories.append(category3)  # Brave New World - Adult

book14.categories.append(category7)  # The Picture of Dorian Gray - Romance
book14.categories.append(category3)  # The Picture of Dorian Gray - Adult
book14.categories.append(category4)  # The Picture of Dorian Gray - Classic

book15.categories.append(category4)  # The Odyssey - Classic
book15.categories.append(category9)  # The Odyssey - Adventure

book16.categories.append(category4)  # Frankenstein - Classic
book16.categories.append(category6)  # Frankenstein - Science Fiction
book16.categories.append(category3)  # Frankenstein - Adult

book17.categories.append(category8)  # Dracula - Horror
book17.categories.append(category3)  # Dracula - Adult

book18.categories.append(category8)  # The Road - Horror
book18.categories.append(category3)  # The Road - Adult
book18.categories.append(category6)  # The Road - Science Fiction

book19.categories.append(category8)  # The Shining - Horror
book19.categories.append(category3)  # The Shining - Adult

book20.categories.append(category9)  # The Alchemist - Adventure
book20.categories.append(category1)  # The Alchemist - Kids
book20.categories.append(category7)  # The Alchemist - Romance

session.commit()
