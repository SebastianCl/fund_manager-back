from typing import List

import boto3  # type: ignore
import os


class DynamoDB:

    def connect() -> boto3.resource:
        return boto3.resource(
            "dynamodb",
            region_name=os.getenv("region_name"),
            aws_access_key_id=os.getenv("aws_access_key_id"),
            aws_secret_access_key=os.getenv("aws_secret_access_key"),
        )

    def consult(dynamodb, table_name) -> List:
        table = dynamodb.Table(table_name)
        response = table.scan()
        items = response.get("Items", [])
        return items
