from fastapi import APIRouter
from models.auth import LoginRequest, LoginResponse

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)

@router.post("/login")
async def login(login: LoginRequest) -> LoginResponse:

    # TODO: Implement login functionality

    return LoginResponse(success=True, token="token")
