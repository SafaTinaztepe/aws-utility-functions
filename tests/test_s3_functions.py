"""
Tests for the S3 utility functions
"""
import os
import pytest
import boto3
from moto import mock_s3

from aws_utils import create_s3_bucket, upload_file_to_s3


@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for boto3"""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "us-east-1"


@pytest.fixture
def s3_client(aws_credentials):
    with mock_s3():
        yield boto3.client("s3", region_name="us-east-1")


def test_create_s3_bucket(s3_client):
    """Test that we can create an S3 bucket"""
    bucket_name = "test-bucket"
    
    # Create the bucket using our utility
    create_s3_bucket(bucket_name)
    
    # Check that the bucket was created
    response = s3_client.list_buckets()
    buckets = [bucket["Name"] for bucket in response["Buckets"]]
    
    assert bucket_name in buckets


def test_upload_file_to_s3(s3_client, tmp_path):
    """Test uploading a file to S3"""
    bucket_name = "test-bucket"
    file_content = "Test file content"
    
    # Create a temporary file
    test_file = tmp_path / "test_file.txt"
    test_file.write_text(file_content)
    
    # Create the bucket
    create_s3_bucket(bucket_name)
    
    # Upload the file
    result = upload_file_to_s3(str(test_file), bucket_name)
    
    # Verify the upload
    assert result["status"] == "success"
    assert result["bucket"] == bucket_name
    assert result["key"] == "test_file.txt"
    
    # Verify the file content in S3
    response = s3_client.get_object(Bucket=bucket_name, Key="test_file.txt")
    retrieved_content = response["Body"].read().decode("utf-8")
    
    assert retrieved_content == file_content