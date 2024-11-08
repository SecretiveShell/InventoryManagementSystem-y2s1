from fastapi import FastAPI

from inventory import router as inventoryRouter

app = FastAPI(
    title="Books4Bucks API Gateway",
    description="books 4 bucks inventory management API"
)

app.include_router(inventoryRouter)