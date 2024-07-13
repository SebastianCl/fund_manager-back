from typing import List
from schemas.transaction import Transaction


class TransactionService:

    def get_transactions() -> List[Transaction]:
        result = [
            {
                "id": 1,
                "fundId": "1",
                "amount": "75000",
                "type": "apertura",
                "date": "01/01/2024",
            },
            {
                "id": 2,
                "fundId": "2",
                "amount": "125000",
                "type": "cancelacion",
                "date": "01/01/2024",
            },
            {
                "id": 3,
                "fundId": "3",
                "amount": "50000",
                "type": "apertura",
                "date": "01/01/2024",
            },
        ]
        return result

    def create_transaction(transaction: Transaction):
        print(transaction)
        return
