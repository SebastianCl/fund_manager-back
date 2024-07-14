from pydantic import BaseModel  # type: ignore


class FundModel(BaseModel):
    fund_id: int
    name: str
    minimum_amount: int
    category: str
