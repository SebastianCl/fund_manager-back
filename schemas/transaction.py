from pydantic import BaseModel, Field  # type: ignore
from typing import Optional


class Transaction(BaseModel):
    transaction_id: int
    fundId: str = Field(min_length=1, max_length=15)
    amount: str = Field(min_length=1, max_length=15)
    type: str = Field(min_length=1, max_length=15)
    date: str = Field(min_length=1, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "transaction_id": 123,
                "fundId": "1",
                "amount": "75000",
                "type": "apertura",
                "date": "12/07/2024",
            }
        }
