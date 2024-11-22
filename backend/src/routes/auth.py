import secrets
from typing import Annotated, Literal
from fastapi import APIRouter, Depends
from auth.login import create_session, delete_session
from auth.redis_user_model import RedisUserModel
from database.ORM import User
from models.auth import LoginRequest, LoginResponse
from database.session import Session

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/login")
async def login(login: LoginRequest) -> LoginResponse:
    # TODO: Implement login functionality

    with Session() as session:
        user = session.query(User).filter(User.email == login.email).first()

    if user is None:
        return LoginResponse(success=False)

    if secrets.compare_digest(str(user.password), login.password):
        model = RedisUserModel.model_validate(user, from_attributes=True)
        token = await create_session(model)
        return LoginResponse(success=True, token=token)

    return LoginResponse(success=False)


@router.post("/logout")
async def logout(success: Annotated[Literal[True], Depends(delete_session)]) -> Literal[True]:
    return success
