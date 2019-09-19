"""
Author: Christian Urcuqui

This code wants to print the buckets in our environment at AWS Cloud Service 
"""
# the next package allows us to use aws libraries
import boto3
import sys
import botocore

# argument with console, specifically the region, for example us-east-1
region = sys.argv[1]

s3 = boto3.client("s3", region_name=region)

response = s3.list_buckets()
print(response)