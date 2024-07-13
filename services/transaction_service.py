from typing import List
from fastapi import HTTPException # type: ignore
from schemas.transaction_schema import TransactionSchema
from config.dynamoDB import DynamoDB
import logging

logger = logging.getLogger(__name__)

class TransactionService:
    def __init__(self):
        self.dynamodb_client = DynamoDB()

    def get_transactions(self) -> List[TransactionSchema]:
        try:
            items = self.dynamodb_client.get_all("transaction")
            return [TransactionSchema(**item) for item in items]
        except RuntimeError as e:
            logger.error(f"Error fetching transactions: {e}")
            raise HTTPException(status_code=500, detail="Error fetching transactions")

    def create_transaction(self, transaction: TransactionSchema) -> None:
        try:
            self.dynamodb_client.create_item("transaction", transaction.dict())
        except RuntimeError as e:
            logger.error(f"Error creating transaction: {e}")
            raise HTTPException(status_code=500, detail="Error creating transaction")
