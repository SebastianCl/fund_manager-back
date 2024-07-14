from pydantic import BaseModel, Field  # type: ignore


class UserUpdateSchema(BaseModel):
    amount: int

    class Config:
        schema_extra = {
            "example": {
                "amount": 75000,
            }
        }
