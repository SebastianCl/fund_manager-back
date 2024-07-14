from typing import List, Optional
from fastapi import HTTPException  # type: ignore
from models.fund_model import FundModel
from config.dynamoDB_manager import DynamoDBManager
import logging

logger = logging.getLogger(__name__)


class FundService:
    def __init__(self):
        self.dynamoDB_manager = DynamoDBManager()

    def get_funds(self) -> List[FundModel]:
        try:
            items = self.dynamoDB_manager.get_all("fund")
            return [FundModel(**item) for item in items]
        except RuntimeError as e:
            logger.error(f"Error fetching funds: {e}")
            raise HTTPException(status_code=500, detail="Error fetching funds")

    def create_fund(self, fund: FundModel) -> None:
        try:
            self.dynamoDB_manager.create_item("fund", fund.dict())
        except RuntimeError as e:
            logger.error(f"Error creating fund: {e}")
            raise HTTPException(status_code=500, detail="Error creating fund")

    def get_fund(self, fund_id: int) -> Optional[FundModel]:
        try:
            key = {"fund_id": fund_id}
            fund_data = self.dynamoDB_manager.read_item("fund", key)
            if not fund_data:
                raise HTTPException(status_code=404, detail="Fund not found")
            return fund_data
        except RuntimeError as e:
            logger.error(f"Error reading fund: {e}")
            raise HTTPException(status_code=500, detail="Error reading fund")
