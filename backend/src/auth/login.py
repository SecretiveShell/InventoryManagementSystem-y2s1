from typing import Annotated, Literal
from fastapi import Depends, HTTPException, Header
from .redis_client import get_redis_client
from secrets import token_hex
from .redis_user_model import RedisUserModel
import json

TOKEN_EXPIRE = 60 * 30  # 30 minutes


async def create_session(User: RedisUserModel) -> str:
    """Function to create a session for a user, returns a session token"""
    token = token_hex(128)
    json = User.model_dump_json()

    async with get_redis_client() as redis:
        await redis.setex(str(token), int(TOKEN_EXPIRE), str(json))

    return token


async def delete_session(token: Annotated[str, Header()]) -> Literal[True]:
    """Function to delete a session for a user"""
    async with get_redis_client() as redis:
        await redis.delete(token)

    return True


# this can be depended on to check if a user is logged in
async def get_user_from_session(token: Annotated[str, Header()]) -> RedisUserModel:
    """Function to get a user from a session"""
    async with get_redis_client() as redis:
        user_json = await redis.get(token)

    # if the user_json is None, the session token is invalid
    if user_json is None:
        raise HTTPException(status_code=401, detail="Invalid session token")

    return RedisUserModel(**json.loads(user_json))


# this just annotates the get_user_from_session function
# improves DRY with fastapi dependency injection
get_session_depends = Annotated[RedisUserModel, Depends(get_user_from_session)]


# this is a utility function to force a logged in user to be an admin
async def get_admin(user: get_session_depends) -> RedisUserModel:
    if user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")
    return user


get_admin_depends = Annotated[RedisUserModel, Depends(get_admin)]
