from typing import List

from schemas.transaction import Transaction
from config.dynamoDB import DynamoDB


class TransactionService:

    def get_transactions() -> List[Transaction]:
        connection = DynamoDB.connect()
        response = DynamoDB.consult(connection, "transaction")
        return response

    def create_transaction(transaction: Transaction):
        print(transaction)
        return
