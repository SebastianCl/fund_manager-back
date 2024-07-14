from pydantic import BaseModel, Field  # type: ignore


class TransactionCancelSchema(BaseModel):
    transaction_id: str

    class Config:
        schema_extra = {"example": {"transaction_id": 1}}
