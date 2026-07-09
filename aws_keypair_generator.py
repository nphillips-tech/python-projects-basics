#!/usr/bin/env python3
import boto3
import botocore.exceptions
import os

client = boto3.client('ec2')
KEY_NAME = "automation-keypair"
FILE_NAME = f"{KEY_NAME}.pem"

try:
    print(f"[INFO]: Requesting cryptographic key pair '{KEY_NAME}' from AWS...")
    response = client.create_key_pair(KeyName=KEY_NAME)
    private_key_material = response['KeyMaterial']
    with open(FILE_NAME, "w") as key_file:
        key_file.write(private_key_material)
    print(f"[SUCCESS]: Key pair created on AWS and saved locally as: {FILE_NAME}")
    
    os.chmod(FILE_NAME, 0o400)
    print(f"[INFO]: Restricted local file permissions to read-only (chmod 400).")

except client.exceptions.ClientError as error:
    if error.response['Error']['Code'] == 'InvalidKeyPair.Duplicate':
        print(f"[WARN]: A key pair named '{KEY_NAME}' already exists on AWS.")
    else:
        print(f"[ERROR]: AWS API Client Error: {error}")
except Exception as error:
    print(f"[ERROR]: An unexpected error occurred: {error}")