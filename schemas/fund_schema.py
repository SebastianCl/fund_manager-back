from pydantic import BaseModel, Field # type: ignore


class FundSchema(BaseModel):
    id: int
    name: str = Field(min_length=5, max_length=15)
    minimumAmount: str = Field(min_length=5, max_length=15)
    category:str = Field(min_length=5, max_length=15)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "FPV_EL CLIENTE_RECAUDADORA",
                "minimumAmount": "75000",
                "category" : "FPV"
            }
        }

