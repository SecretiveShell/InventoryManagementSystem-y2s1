from fastapi import FastAPI

from inventory import router as inventoryRouter
from book import router as bookRouter

app = FastAPI(
    title="Books4Bucks API Gateway",
    description="books 4 bucks inventory management API"
)

app.include_router(inventoryRouter)
app.include_router(bookRouter)