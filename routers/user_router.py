from fastapi import APIRouter, Path  # type: ignore
from fastapi.responses import JSONResponse  # type: ignore
from fastapi.encoders import jsonable_encoder  # type: ignore
from typing import List
from services.user_service import UserService
from schemas.user_schema import UserSchema

user_router = APIRouter()


@user_router.get("/users/{user_id}", tags=["users"], response_model=UserSchema)
def get_user(user_id: int = Path(ge=1, le=2000)) -> UserSchema:
    userService = UserService()
    result = userService.get_user(user_id)
    if not result:
        return JSONResponse(
            status_code=404, content={"message": "Usuario no encontrado"}
        )
    return JSONResponse(status_code=200, content=jsonable_encoder(result))
