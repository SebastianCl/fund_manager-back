from typing import List, Optional, Dict, Any
import boto3  # type: ignore
import os
from botocore.exceptions import BotoCoreError, NoCredentialsError, ClientError  # type: ignore


class DynamoDB:
    def __init__(
        self,
        region_name: Optional[str] = None,
        aws_access_key_id: Optional[str] = None,
        aws_secret_access_key: Optional[str] = None,
    ):
        self.region_name = region_name or os.getenv("region_name")
        self.aws_access_key_id = aws_access_key_id or os.getenv("aws_access_key_id")
        self.aws_secret_access_key = aws_secret_access_key or os.getenv(
            "aws_secret_access_key"
        )
        self.dynamodb = self.connect()

    def connect(self) -> boto3.resource:
        try:
            return boto3.resource(
                "dynamodb",
                region_name=self.region_name,
                aws_access_key_id=self.aws_access_key_id,
                aws_secret_access_key=self.aws_secret_access_key,
            )
        except (BotoCoreError, NoCredentialsError) as e:
            raise ConnectionError(f"Failed to connect to DynamoDB: {e}")

    def create_item(self, table_name: str, item: Dict[str, Any]) -> None:

        try:
            table = self.dynamodb.Table(table_name)
            table.put_item(Item=item)
        except ClientError as e:
            raise RuntimeError(f"Failed to create item in table {table_name}: {e}")

    def read_item(
        self, table_name: str, key: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:

        try:
            table = self.dynamodb.Table(table_name)
            response = table.get_item(Key=key)
            return response.get("Item")
        except ClientError as e:
            raise RuntimeError(f"Failed to read item from table {table_name}: {e}")

    def update_item(
        self,
        table_name: str,
        key: Dict[str, Any],
        update_expression: str,
        expression_attribute_values: Dict[str, Any],
    ) -> None:

        try:
            table = self.dynamodb.Table(table_name)
            table.update_item(
                Key=key,
                UpdateExpression=update_expression,
                ExpressionAttributeValues=expression_attribute_values,
            )
        except ClientError as e:
            raise RuntimeError(f"Failed to update item in table {table_name}: {e}")

    def delete_item(self, table_name: str, key: Dict[str, Any]) -> None:

        try:
            table = self.dynamodb.Table(table_name)
            table.delete_item(Key=key)
        except ClientError as e:
            raise RuntimeError(f"Failed to delete item from table {table_name}: {e}")

    def get_all(self, table_name: str) -> List[Dict[str, Any]]:

        try:
            table = self.dynamodb.Table(table_name)
            response = table.scan()
            items = response.get("Items", [])
            return items
        except ClientError as e:
            raise RuntimeError(f"Failed to scan table {table_name}: {e}")
