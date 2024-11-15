from fastapi import FastAPI

from routes import router

app = FastAPI(
    title="Books4Bucks API Gateway",
    description="books 4 bucks inventory management API",
)

app.include_router(router)
