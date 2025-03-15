# AWS Utility Functions

A collection of utility functions for working with AWS services.

## Features

- Create S3 buckets
- Upload files to S3
- Start EC2 instances
- List Lambda functions
- Get all items from DynamoDB tables

## Installation

### Using pip

```bash
# Install directly with pip
pip install -r requirements.txt
```

### Using a virtual environment (recommended)

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Development Setup

```bash
# Clone the repository
git clone https://github.com/SafaTinaztepe/aws-utility-functions.git
cd aws-utility-functions

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dev dependencies
pip install -r requirements.txt
pip install pytest moto

# Run tests
pytest
```

## Usage

```python
# Import the module
from aws_utils import create_s3_bucket

# Create a bucket
result = create_s3_bucket('my-new-bucket', 'us-west-2')
print(result)
```

## AWS Credentials

The utility functions use boto3, which looks for AWS credentials in the following order:
1. Environment variables
2. Shared credential file (~/.aws/credentials)
3. AWS IAM role (if running on an EC2 instance or Lambda)

Make sure your AWS credentials are properly configured.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.