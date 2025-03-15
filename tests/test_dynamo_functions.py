"""
Tests for the DynamoDB utility functions
"""
import pytest
import boto3
from moto import mock_dynamodb

from aws_utils import get_dynamodb_table_items


@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for boto3"""
    import os
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"


@pytest.fixture
def dynamodb_client(aws_credentials):
    with mock_dynamodb():
        yield boto3.client("dynamodb", region_name="us-east-1")


@pytest.fixture
def dynamodb_resource(aws_credentials):
    with mock_dynamodb():
        yield boto3.resource("dynamodb", region_name="us-east-1")


@pytest.fixture
def dynamodb_table(dynamodb_resource, dynamodb_client):
    """Create a mock DynamoDB table with test data"""
    
    # Create the table
    table_name = "test-table"
    dynamodb_client.create_table(
        TableName=table_name,
        KeySchema=[
            {"AttributeName": "id", "KeyType": "HASH"},
        ],
        AttributeDefinitions=[
            {"AttributeName": "id", "AttributeType": "S"},
        ],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
    )
    
    # Add test data
    table = dynamodb_resource.Table(table_name)
    for i in range(10):
        table.put_item(
            Item={
                "id": f"item{i}",
                "data": f"test data {i}",
                "number": i
            }
        )
    
    return table_name


def test_get_dynamodb_table_items(dynamodb_table):
    """Test getting all items from a DynamoDB table"""
    
    # Get items using our utility function
    items = get_dynamodb_table_items(dynamodb_table)
    
    # Verify we got all 10 items
    assert len(items) == 10
    
    # Verify the content
    for i in range(10):
        item = next((item for item in items if item["id"] == f"item{i}"), None)
        assert item is not None
        assert item["data"] == f"test data {i}"
        assert item["number"] == i