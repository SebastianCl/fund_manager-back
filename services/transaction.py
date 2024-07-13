from typing import List

from schemas.transaction import Transaction
from config.dynamoDB import DynamoDB


class TransactionService:

    def get_transactions() -> List[Transaction]:
        dynamodb_client = DynamoDB()

        try:
            items = dynamodb_client.consult("transaction")
            return items
        except RuntimeError as e:
            print(f"Error: {e}")

    def create_transaction(transaction: Transaction):
        print(transaction)
        return
