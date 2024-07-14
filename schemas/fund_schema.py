from pydantic import BaseModel, Field  # type: ignore


class FundSchema(BaseModel):
    fund_id: int
    name: str = Field(min_length=1, max_length=50)
    minimum_amount: int
    category: str = Field(min_length=1, max_length=3)

    class Config:
        schema_extra = {
            "example": {
                "fund_id": 1,
                "name": "FPV_EL CLIENTE_RECAUDADORA",
                "minimum_amount": 75000,
                "category": "FPV",
            }
        }
