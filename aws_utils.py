# AWS Utility Functions Library
# --------------------------
# This module provides utility functions for interacting with various AWS services.

import boto3
import json
import logging
from typing import Dict, List, Any, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_s3_bucket(bucket_name: str, region: Optional[str] = None) -> Dict:
    """
    Creates an S3 bucket with the specified name.
    
    Args:
        bucket_name: The name of the bucket to create
        region: The AWS region to create the bucket in (default: None, uses boto3 default)
        
    Returns:
        Dict: Response from the bucket creation operation
    """
    try:
        s3_client = boto3.client('s3', region_name=region)
        
        if region is None or region == 'us-east-1':
            response = s3_client.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            response = s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration=location
            )
            
        logger.info(f"Successfully created S3 bucket: {bucket_name}")
        return response
    except Exception as e:
        logger.error(f"Error creating S3 bucket {bucket_name}: {str(e)}")
        raise


def upload_file_to_s3(file_path: str, bucket_name: str, object_key: Optional[str] = None) -> Dict:
    """
    Uploads a file to an S3 bucket.
    
    Args:
        file_path: The local path to the file to upload
        bucket_name: The name of the bucket to upload to
        object_key: The object key (path) in S3. If None, uses filename from file_path
        
    Returns:
        Dict: Response from the upload operation
    """
    try:
        s3_client = boto3.client('s3')
        
        # If no object_key provided, use filename from file_path
        if object_key is None:
            import os
            object_key = os.path.basename(file_path)
            
        response = s3_client.upload_file(file_path, bucket_name, object_key)
        logger.info(f"Successfully uploaded {file_path} to {bucket_name}/{object_key}")
        return {"status": "success", "bucket": bucket_name, "key": object_key}
    except Exception as e:
        logger.error(f"Error uploading file {file_path} to S3: {str(e)}")
        raise


def start_ec2_instance(instance_id: str, region: Optional[str] = None) -> Dict:
    """
    Starts an EC2 instance.
    
    Args:
        instance_id: The ID of the instance to start
        region: The AWS region where the instance is located (default: None, uses boto3 default)
        
    Returns:
        Dict: Response from the start operation
    """
    try:
        ec2_client = boto3.client('ec2', region_name=region)
        response = ec2_client.start_instances(InstanceIds=[instance_id])
        logger.info(f"Successfully started EC2 instance: {instance_id}")
        return response
    except Exception as e:
        logger.error(f"Error starting EC2 instance {instance_id}: {str(e)}")
        raise


def list_lambda_functions(region: Optional[str] = None) -> List[Dict]:
    """
    Lists all Lambda functions in the specified region.
    
    Args:
        region: The AWS region to list Lambda functions from (default: None, uses boto3 default)
        
    Returns:
        List[Dict]: List of Lambda function configurations
    """
    try:
        lambda_client = boto3.client('lambda', region_name=region)
        paginator = lambda_client.get_paginator('list_functions')
        
        functions = []
        for page in paginator.paginate():
            functions.extend(page['Functions'])
            
        logger.info(f"Successfully retrieved {len(functions)} Lambda functions")
        return functions
    except Exception as e:
        logger.error(f"Error listing Lambda functions: {str(e)}")
        raise


def get_dynamodb_table_items(table_name: str, region: Optional[str] = None) -> List[Dict]:
    """
    Scans and retrieves all items from a DynamoDB table.
    
    Args:
        table_name: The name of the DynamoDB table
        region: The AWS region where the table is located (default: None, uses boto3 default)
        
    Returns:
        List[Dict]: List of items from the table
    """
    try:
        dynamodb = boto3.resource('dynamodb', region_name=region)
        table = dynamodb.Table(table_name)
        
        response = table.scan()
        items = response.get('Items', [])
        
        # Handle pagination if there are more items
        while 'LastEvaluatedKey' in response:
            response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            items.extend(response.get('Items', []))
            
        logger.info(f"Successfully retrieved {len(items)} items from DynamoDB table: {table_name}")
        return items
    except Exception as e:
        logger.error(f"Error retrieving items from DynamoDB table {table_name}: {str(e)}")
        raise