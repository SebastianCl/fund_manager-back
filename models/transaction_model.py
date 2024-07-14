from pydantic import BaseModel  # type: ignore


class TransactionModel(BaseModel):
    transaction_id: str
    user_id: int
    fund_id: int
    amount: int
    type: str
    date: str
