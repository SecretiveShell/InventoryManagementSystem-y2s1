import redis.asyncio as redis
from os import getenv
from contextlib import asynccontextmanager

# optionally read redis url from environment variable
REDIS_URL = getenv("B4B_REDIS_URL", "redis://localhost:6379")

pool = redis.ConnectionPool.from_url(REDIS_URL)


@asynccontextmanager
async def get_redis_client():
    """Context manager to get a redis client"""
    client = redis.Redis.from_pool(pool)
    try:
        yield client
    finally:
        await client.aclose()

if __name__ == "__main__":
    import asyncio

    async def function():
        async with get_redis_client() as client:
            await client.set("hello", "world")

    asyncio.run(function())  # Call the function() correctly
