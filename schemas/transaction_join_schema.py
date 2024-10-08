from pydantic import BaseModel, Field  # type: ignore


class TransactionJoinSchema(BaseModel):
    user_id: int
    fund_id: int
    amount: int
    notification: str

    class Config:
        schema_extra = {
            "example": {"user_id": 1, "fund_id": 1, "amount": 75000},
            "notification": "sms",
        }
