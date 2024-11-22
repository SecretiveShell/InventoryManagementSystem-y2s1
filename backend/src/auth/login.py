from fastapi import HTTPException
from .redis_client import get_redis_client
from secrets import token_hex
from .redis_user_model import RedisUserModel

TOKEN_EXPIRE = 60 * 30 # 30 minutes

async def create_session(User: RedisUserModel) -> str:
    """Function to create a session for a user, returns a session token"""
    token = token_hex(128)
    json = User.model_dump_json()

    async with get_redis_client() as redis:
        redis.setex(token, json, TOKEN_EXPIRE)

    return token

async def delete_session(token: str) -> None:
    """Function to delete a session for a user"""
    async with get_redis_client() as redis:
        redis.delete(token)

# this can be depended on to check if a user is logged in
async def get_user_from_session(token: str) -> RedisUserModel:
    """Function to get a user from a session"""
    async with get_redis_client() as redis:
        user_json = redis.get(token)

    # if the user_json is None, the session token is invalid
    if user_json is None:
        raise HTTPException(status_code=401, detail="Invalid session token")
        
    return RedisUserModel(**user_json)