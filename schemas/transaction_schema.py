from pydantic import BaseModel, Field  # type: ignore


class TransactionSchema(BaseModel):
    transaction_id: str
    fund_id: int
    amount: int
    type: str = Field(min_length=1, max_length=15)
    date: str = Field(min_length=1, max_length=10)

    class Config:
        schema_extra = {
            "example": {
                "transaction_id": "123",
                "fund_id": 1,
                "amount": 75000,
                "type": "apertura",
                "date": "12/07/2024",
            }
        }
