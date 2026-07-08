#!/usr/bin/env python3
import boto3
import botocore.exceptions

client = boto3.client('ec2')
AMI_ID = "ami-0a02a779008fa3b99"
SECURITY_GROUP_ID = "sg-0038559d09bab2619"
INSTANCE_TYPE = "t3.micro"


try:
    response = client.run_instances(
        ImageId=AMI_ID,
        InstanceType=INSTANCE_TYPE,
        MinCount=1,
        MaxCount=1,
        SecurityGroupIds=[SECURITY_GROUP_ID],
        CreditSpecification={
            'CpuCredits': 'standard'
        }
    )
    launched_instance_id = response['Instances'][0]['InstanceId']
    
    print(f"[SUCCESS]: Provisioned virtual compute node.")
    print(f"Instance ID: {launched_instance_id}")
except botocore.exceptions.ClientError as error:
    print(f"[ERROR]: AWS API Client Error occurred.")
    print(f"Details: {error}")
except Exception as error:
    print(f"[ERROR]: An unexpected error occurred: {error}")