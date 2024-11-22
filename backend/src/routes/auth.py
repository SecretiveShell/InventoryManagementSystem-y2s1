from typing import Annotated, Literal
from fastapi import APIRouter, Depends
from auth.login import delete_session
from models.auth import LoginRequest, LoginResponse

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/login")
async def login(login: LoginRequest) -> LoginResponse:
    # TODO: Implement login functionality

    return LoginResponse(success=True, token="token")


@router.post("/logout")
async def logout(success: Annotated[Literal[True], Depends(delete_session)]) -> Literal[True]:
    return success
