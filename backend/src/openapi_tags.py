from enum import StrEnum


class OpenAPITags(StrEnum):
    users = "users"
    auth = "auth"
    books = "books"
    authors = "authors"
    inventory = "inventory"
    orders = "orders"


tag_metadata = [
    # {
    #     "name": OpenAPITags.users.value,
    #     "description": "User management",
    # },
    {
        "name": OpenAPITags.auth.value,
        "description": "Authentication",
    },
    {
        "name": OpenAPITags.books.value,
        "description": "Book management",
    },
    {
        "name": OpenAPITags.authors.value,
        "description": "Author management",
    },
    {
        "name": OpenAPITags.inventory.value,
        "description": "Inventory management",
    },
    {
        "name": OpenAPITags.orders.value,
        "description": "Order management",
    },
]
