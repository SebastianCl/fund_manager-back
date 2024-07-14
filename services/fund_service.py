from typing import List
from fastapi import HTTPException  # type: ignore
from models.fund_model import FundModel
from config.dynamoDB_manager import DynamoDBManager
import logging

logger = logging.getLogger(__name__)


class FundService:
    def __init__(self):
        self.dynamodb_client = DynamoDBManager()

    def get_funds(self) -> List[FundModel]:
        try:
            items = self.dynamodb_client.get_all("fund")
            return [FundModel(**item) for item in items]
        except RuntimeError as e:
            logger.error(f"Error fetching funds: {e}")
            raise HTTPException(status_code=500, detail="Error fetching funds")

    def create_fund(self, fund: FundModel) -> None:
        try:
            self.dynamodb_client.create_item("fund", fund.dict())
        except RuntimeError as e:
            logger.error(f"Error creating fund: {e}")
            raise HTTPException(status_code=500, detail="Error creating fund")
