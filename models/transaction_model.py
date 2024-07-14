from pydantic import BaseModel  # type: ignore


class TransactionModel(BaseModel):
    transaction_id: int
    fundId: int
    amount: int
    type: str
    date: str
