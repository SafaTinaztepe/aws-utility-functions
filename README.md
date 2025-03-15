# AWS Utility Functions

A collection of utility functions for working with AWS services.

## Features

- Create S3 buckets
- Upload files to S3
- Start EC2 instances
- List Lambda functions
- Get all items from DynamoDB tables

## Installation

```bash
# Install with pip
pip install -r requirements.txt
```

## Usage

```python
# Import the module
from aws_utils import create_s3_bucket

# Create a bucket
result = create_s3_bucket('my-new-bucket', 'us-west-2')
print(result)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
