from pydantic import BaseModel, Field  # type: ignore


class UserSchema(BaseModel):
    user_id: int
    name: str = Field(min_length=1, max_length=50)
    amount: int
    email: str
    phone: str

    class Config:
        schema_extra = {
            "example": {
                "user_id": 1,
                "name": "Pepita",
                "amount": 75000,
                "email": "uncorreo@dominio.com",
                "phone": "+14343443",
            }
        }
