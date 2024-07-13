from pydantic import BaseModel  # type: ignore


class Fund(BaseModel):
    id = int
    name = str
    minimumAmount = str
    category = str
