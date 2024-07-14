from fastapi import APIRouter, Body  # type: ignore
from fastapi.responses import JSONResponse  # type: ignore
from fastapi.encoders import jsonable_encoder  # type: ignore
from typing import List
from services.user_service import UserService
from schemas.user_schema import UserSchema

user_router = APIRouter()


@user_router.get(
    "/users",
    tags=["users"],
    response_model=List[UserSchema],
    status_code=200,
)
def get_users() -> UserSchema:
    userService = UserService()
    result = userService.get_users()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@user_router.post("/users", tags=["users"], response_model=dict, status_code=201)
def create_user(user: UserSchema = Body()) -> dict:
    userService = UserService()
    userService.create_user(user)
    return JSONResponse(
        status_code=201, content={"message": "Se ha registrado el fondo"}
    )
