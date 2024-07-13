from pydantic import BaseModel  # type: ignore


class Transaction(BaseModel):
    transactionId = int
    fundId = str
    type = str
    amount = str
    date = str
