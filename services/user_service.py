from typing import List
from fastapi import HTTPException  # type: ignore
from models.user_model import UserModel
from config.dynamoDB_manager import DynamoDBManager
import logging

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self):
        self.dynamodb_client = DynamoDBManager()

    def get_users(self) -> List[UserModel]:
        try:
            items = self.dynamodb_client.get_all("user")
            return [UserModel(**item) for item in items]
        except RuntimeError as e:
            logger.error(f"Error fetching users: {e}")
            raise HTTPException(status_code=500, detail="Error fetching users")

    def create_user(self, user: UserModel) -> None:
        try:
            self.dynamodb_client.create_item("user", user.dict())
        except RuntimeError as e:
            logger.error(f"Error creating user: {e}")
            raise HTTPException(status_code=500, detail="Error creating user")
