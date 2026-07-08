#!/usr/bin/env python3
import boto3
import botocore.exceptions

s3_client = boto3.client('s3')


BUCKET_NAME = "nick-p-validation-77129"
LOCAL_FILE = "backup_log.txt"

try:
    s3_client.upload_file(LOCAL_FILE,BUCKET_NAME,"remote_backup_log.txt")
    print(f"\nSuccess - File uploaded to the {BUCKET_NAME} bucket.")
    objects_payload = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
    print("\n=== Current Objects inside Bucket ===")
    if 'Contents' in objects_payload:
        for obj in objects_payload['Contents']:
            print(f"- {obj['Key']}")
    else:
        print("Bucket is empty.")
except botocore.exceptions.ClientError as e:
    
    print(f"\n[ERROR]: Authentication failed. Check your access keys.")
    print(f"Details: {e}")
except Exception as e:
    print(f"\n[ERROR]: An unexpected error occurred: {e}")