from typing import List, Optional
from fastapi import HTTPException  # type: ignore
from models.transaction_model import TransactionModel
from config.dynamoDB_manager import DynamoDBManager
import logging

logger = logging.getLogger(__name__)


class TransactionService:
    def __init__(self):
        self.dynamoDB_manager = DynamoDBManager()

    def get_transactions(self) -> List[TransactionModel]:
        try:
            items = self.dynamoDB_manager.get_all("transaction")
            return [TransactionModel(**item) for item in items]
        except RuntimeError as e:
            logger.error(f"Error fetching transactions: {e}")
            raise HTTPException(status_code=500, detail="Error fetching transactions")

    def create_transaction(self, transaction: TransactionModel) -> None:
        try:
            self.dynamoDB_manager.create_item("transaction", transaction.dict())
        except RuntimeError as e:
            logger.error(f"Error creating transaction: {e}")
            raise HTTPException(status_code=500, detail="Error creating transaction")

    def get_transaction(self, transaction_id: int) -> Optional[TransactionModel]:
        try:
            key = {"transaction_id": transaction_id}
            transaction_data = self.dynamoDB_manager.read_item("transaction", key)
            if not transaction_data:
                raise HTTPException(status_code=404, detail="Transaction not found")
            return transaction_data
        except RuntimeError as e:
            logger.error(f"Error reading transaction: {e}")
            raise HTTPException(status_code=500, detail="Error reading transaction")
