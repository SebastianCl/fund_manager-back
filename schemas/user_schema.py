from pydantic import BaseModel, Field  # type: ignore


class UserSchema(BaseModel):
    user_id: int
    name: str = Field(min_length=1, max_length=50)
    amount: int

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "name": "Pepita",
                "minimum_amount": 75000,
            }
        }
