from typing import Optional
from pydantic import BaseModel, Field


class LoginRequest(BaseModel):
    email: str = Field(..., description="the users email address")
    password: str = Field(..., description="the users password")


class LoginResponse(BaseModel):
    success: bool = Field(..., description = "did the login succeed")
    token: Optional[str] = Field(default=None, description="the user session token")
