#!/usr/bin/env python3
import os
import boto3
import botocore.exceptions

s3_client = boto3.client('s3')
directory_path = '/home/nick/python-projects-basics/local_logs'
file = os.listdir(directory_path)
bucket = "nick-p-validation-77129"

try:
    for filename in os.listdir(directory_path):
        key = "fleet_backups/" + filename
        full_path = os.path.join(directory_path, filename)
        s3_client.upload_file(full_path, bucket, key)
        print(f"File {filename} has been uploaded to the '{bucket}' bucket.")
except botocore.exceptions.ClientError as e:
    print(f"\n[ERROR]: Authentication failed. Check your access keys.")
    print(f"Details: {e}")
except Exception as e:
    print(f"\n[ERROR]: An unexpected error occurred: {e}")
