#!/usr/bin/env python3

#!/usr/bin/env python3
"""
AWS API Authentication & S3 Discovery Test
"""

import boto3
import botocore.exceptions

try:
    
    s3_client = boto3.client('s3')
    
    print("[INFO]: Connecting to AWS API...")
    response = s3_client.list_buckets()
    
    print("\n=== Active S3 Storage Buckets Found ===")
    
    
    for bucket in response['Buckets']:
        print(f"- {bucket['Name']}")
        
except botocore.exceptions.ClientError as e:
    
    print(f"\n[ERROR]: Authentication failed. Check your access keys.")
    print(f"Details: {e}")
except Exception as e:
    print(f"\n[ERROR]: An unexpected error occurred: {e}")