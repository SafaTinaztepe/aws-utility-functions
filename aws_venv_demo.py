#!/usr/bin/env python3
"""
AWS Utilities Virtual Environment Demo
---------------------------------
This script demonstrates how to use AWS utility functions 
with a proper Python virtual environment.
"""

import os
import sys
import subprocess
import platform

def setup_venv():
    """Set up a virtual environment for AWS utilities"""
    print("Setting up a virtual environment...")
    
    # Determine the correct activation command based on OS
    if platform.system() == "Windows":
        activate_cmd = "venv\\Scripts\\activate"
        python_cmd = "python"
    else:
        activate_cmd = "source venv/bin/activate"
        python_cmd = "python3"
    
    # Create the virtual environment
    try:
        subprocess.run([python_cmd, "-m", "venv", "venv"], check=True)
        print("Virtual environment created successfully.")
    except subprocess.CalledProcessError:
        print("Failed to create virtual environment.")
        sys.exit(1)
    
    # Print activation instructions
    print("\nTo activate the virtual environment:")
    print(f"  {activate_cmd}")
    
    activation_note = """
After activation, install required packages:
  pip install -r requirements.txt
  pip install boto3
    
Example code to run after setup:"""
    print(activation_note)

def create_aws_example():
    """Create a simple AWS example script"""
    example_code = """#!/usr/bin/env python3
# aws_example.py - Example using AWS utility functions

import time
from aws_utils import create_s3_bucket, list_lambda_functions

def demo_aws_utilities():
    # Create a unique bucket name using timestamp
    bucket_name = f"demo-bucket-{int(time.time())}"
    
    print(f"Creating S3 bucket: {bucket_name}")
    try:
        result = create_s3_bucket(bucket_name, "us-west-2")
        print(f"Bucket created successfully: {bucket_name}")
        print(result)
    except Exception as e:
        print(f"Error creating bucket: {str(e)}")
    
    print("\\nListing Lambda functions:")
    try:
        functions = list_lambda_functions()
        if functions:
            for i, func in enumerate(functions, 1):
                print(f"{i}. {func.get('FunctionName')} - Runtime: {func.get('Runtime')}")
        else:
            print("No Lambda functions found in this region")
    except Exception as e:
        print(f"Error listing Lambda functions: {str(e)}")

if __name__ == "__main__":
    demo_aws_utilities()
"""
    
    with open("aws_example.py", "w") as f:
        f.write(example_code)
    
    # Make the script executable on Unix-like systems
    if platform.system() != "Windows":
        os.chmod("aws_example.py", 0o755)
    
    print("Created aws_example.py script for demonstrating AWS utilities")

if __name__ == "__main__":
    setup_venv()
    create_aws_example()
    
    print("\nSetup complete! Follow the instructions above to activate your virtual environment.")