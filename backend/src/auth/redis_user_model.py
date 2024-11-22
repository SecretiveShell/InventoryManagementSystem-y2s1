from pydantic import BaseModel


class RedisUserModel(BaseModel):
    """
    basemodel that represents a cached user in redis
    This should be stored as <auth token>:<user object>
    """

    user_id: int
    name: str
    email: str
    address: str
    phone_number: str
    is_admin: bool
