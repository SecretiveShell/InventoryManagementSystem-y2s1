from fastapi import FastAPI

from routes import router
from openapi_tags import tag_metadata

app = FastAPI(
    title="Books4Bucks API Gateway",
    description="books 4 bucks inventory management API",
    openapi_tags=tag_metadata,
    root_path="/api",
)

app.include_router(router)
