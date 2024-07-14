from pydantic import BaseModel  # type: ignore


class TransactionModel(BaseModel):
    transaction_id: str
    fund_id: int
    amount: int
    type: str
    date: str
