from botocore.exceptions import BotoCoreError, NoCredentialsError, ClientError  # type: ignore
from typing import List, Optional
import boto3  # type: ignore
import os


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
            raise ConnectionError(f"Error al conectar a DynamoDB: {e}")

    def consult(self, table_name: str) -> List[dict]:
        try:
            table = self.dynamodb.Table(table_name)
            response = table.scan()
            items = response.get("Items", [])
            return items
        except ClientError as e:
            raise RuntimeError(f"Error al buscar en la tabla {table_name}: {e}")
