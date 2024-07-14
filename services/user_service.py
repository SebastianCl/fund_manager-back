from typing import List, Optional
from fastapi import HTTPException  # type: ignore
from models.user_model import UserModel
from schemas.user_update_schema import UserUpdateSchema
from config.dynamoDB_manager import DynamoDBManager
import logging

logger = logging.getLogger(__name__)


class UserService:
    def __init__(self):
        self.DynamoDBManager = DynamoDBManager()

    def get_users(self) -> List[UserModel]:
        try:
            items = self.DynamoDBManager.get_all("user")
            return [UserModel(**item) for item in items]
        except RuntimeError as e:
            logger.error(f"Error fetching users: {e}")
            raise HTTPException(status_code=500, detail="Error fetching users")

    def create_user(self, user: UserModel) -> None:
        try:
            self.DynamoDBManager.create_item("user", user.dict())
        except RuntimeError as e:
            logger.error(f"Error creating user: {e}")
            raise HTTPException(status_code=500, detail="Error creating user")

    def get_user(self, user_id: int) -> Optional[UserModel]:
        try:
            key = {"user_id": user_id}
            user_data = self.DynamoDBManager.read_item("user", key)
            if not user_data:
                raise HTTPException(status_code=404, detail="User not found")
            return user_data
        except RuntimeError as e:
            logger.error(f"Error reading user: {e}")
            raise HTTPException(status_code=500, detail="Error reading user")

    def update_user_amount(self, user_id: int, update_data: UserUpdateSchema):
        try:
            key = {"user_id": user_id}
            update_expression = "SET amount = :amount"
            expression_attribute_values = {
                ":amount": update_data.amount,
            }

            self.DynamoDBManager.update_item(
                "user", key, update_expression, expression_attribute_values
            )
            return {"message": "User updated successfully"}

        except RuntimeError as e:
            raise HTTPException(status_code=500, detail=f"Failed to update user: {e}")
