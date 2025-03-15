from setuptools import setup, find_packages

setup(
    name="aws_utility_functions",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "boto3>=1.26.0",
        "typing>=3.10.0",
        "pytest>=7.0.0",
        "moto>=2.0.0",
    ],
    author="AWS Utils Developer",
    author_email="dev@example.com",
    description="A collection of utility functions for working with AWS services",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SafaTinaztepe/aws-utility-functions",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)