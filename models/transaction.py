from pydantic import BaseModel  # type: ignore


class Transaction(BaseModel):
    id = int
    fundId = str
    type = str
    amount = str
    date = str
