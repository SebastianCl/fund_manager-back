from pydantic import BaseModel  # type: ignore


class UserModel(BaseModel):
    user_id: int
    name: str
    amount: int
