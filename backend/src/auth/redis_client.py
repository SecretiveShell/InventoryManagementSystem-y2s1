import redis.asyncio as redis
from os import getenv
from contextlib import asynccontextmanager

# optionally read redis url from environment variable
REDIS_URL = getenv("B4B_REDIS_URL", "redis://localhost")

pool = redis.ConnectionPool.from_url(REDIS_URL)


@asynccontextmanager
async def get_redis_client():
    """Context manager to get a redis client"""
    client = redis.Redis.from_pool(pool)
    yield client
    await client.close()
