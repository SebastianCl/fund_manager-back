from typing import List
from schemas.fund_schema import FundSchema


class FundService:

    def get_funds() -> List[FundSchema]:
        result = [
            {
                "id": 1,
                "name": "FPV_EL CLIENTE_RECAUDADORA",
                "minimumAmount": "75000",
                "category": "FPV",
            },
            {
                "id": 2,
                "name": "FPV_EL CLIENTE_ECOPETROL",
                "minimumAmount": "125000",
                "category": "FPV",
            },
            {
                "id": 3,
                "name": "DEUDAPRIVADA",
                "minimumAmount": "50000",
                "category": "FIC",
            },
        ]
        return result
