# Inventory Management System Backend

## Backend Description

This is the Books4Bucks Inventory Management System, built using FastAPI as the web framework and SQLAlchemy for ORM. The system is designed to manage inventory, handle orders, and maintain information about books, authors, and categories. The database used is PostgreSQL, as inferred from the psycopg2 dependency in the requirements.txt file.

## Components

### main.py
- **Functionality**: Initializes the FastAPI application and includes the router to handle API requests.
- **Key Elements**:
  - `app`: FastAPI instance configured with a title and description.
  - `app.include_router(router)`: Includes the router defined in the `routes` module to handle API endpoints.

### start.py
- **Functionality**: Contains the command to run the FastAPI application using Uvicorn.
- **Key Elements**:
  - `uvicorn.run("main:app")`: Starts the FastAPI app with the specified module and app instance.

### database/ORM.py
- **Functionality**: Defines the ORM models and logic to create tables in the PostgreSQL database.
- **Key Elements**:
  - `Base`: Declarative base class for ORM models.
  - Association tables:
    - `book_category_association`: Many-to-many relationship between books and categories.
    - `order_book_association`: Many-to-many relationship between orders and books, including quantity.
    - `book_author_association`: Many-to-many relationship between books and authors.
  - Data tables:
    - `User`: Stores user information including orders.
    - `Order`: Stores order details including books and user.
    - `Book`: Stores book details including inventory, categories, and authors.
    - `Inventory`: Stores inventory details for books.
    - `Category`: Stores category information including books.
    - `Author`: Stores author information including books.
  - **Logic**:
    - Checks if the database exists and creates it if it doesn't.
    - Creates all tables defined in the ORM models.

### models/author.py
- **Functionality**: Defines Pydantic models for author data validation and serialization.
- **Key Elements**:
  - `AuthorBase`: Base model with common fields for authors.
  - `AuthorCreate`: Model for creating new authors, extending `AuthorBase`.
  - `AuthorResponse`: Model for author response data, extending `AuthorBase`.
  - `AuthorDeleteResponse`: Model for author deletion response data.

### models/book.py
- **Functionality**: Defines Pydantic models for book data validation and serialization.
- **Key Elements**:
  - `BookBase`: Base model with common fields for books.
  - `BookInstance`: Model for book instance data, extending `BookBase`.
  - `BookCreate`: Model for creating new books, extending `BookBase`.

### models/orders.py
- **Functionality**: Defines Pydantic models for order data validation and serialization.
- **Key Elements**:
  - `OrderBase`: Base model with common fields for orders.
  - `OrderCreate`: Model for creating new orders, extending `OrderBase`.
  - `OrderStatusUpdate`: Model for updating order status.
  - `Order`: Model for order data, extending `OrderBase`.
  - `OrderResponse`: Model for order response data, extending `OrderBase`.

## Running the Backend

To run the backend, execute the following command in the terminal:
```bash
python start.py
```

This command starts the FastAPI application using Uvicorn, making the API endpoints available for requests.
