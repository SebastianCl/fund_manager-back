from typing import List
from fastapi import HTTPException # type: ignore
from models.transaction_model import TransactionModel
from config.dynamoDB_manager import DynamoDBManager
import logging

logger = logging.getLogger(__name__)

class TransactionService:
    def __init__(self):
        self.dynamodb_client = DynamoDBManager()

    def get_transactions(self) -> List[TransactionModel]:
        try:
            items = self.dynamodb_client.get_all("transaction")
            return [TransactionModel(**item) for item in items]
        except RuntimeError as e:
            logger.error(f"Error fetching transactions: {e}")
            raise HTTPException(status_code=500, detail="Error fetching transactions")

    def create_transaction(self, transaction: TransactionModel) -> None:
        try:
            self.dynamodb_client.create_item("transaction", transaction.dict())
        except RuntimeError as e:
            logger.error(f"Error creating transaction: {e}")
            raise HTTPException(status_code=500, detail="Error creating transaction")
