#!/usr/bin/env python3
import boto3
import botocore.exceptions

client = boto3.client('ec2')
AMI_ID = "ami-0a02a779008fa3b99"
SECURITY_GROUP_ID = "sg-0038559d09bab2619"
INSTANCE_TYPE = "t3.micro"
KEY_NAME = "automation-keypair"

try:
    print("[INFO]: Configuring firewall rules on security group...")
    client.authorize_security_group_ingress(
        GroupId=SECURITY_GROUP_ID,
        IpPermissions=[
            {
                'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{'CidrIp': '0.0.0.0/0', 'Description': 'Allow Global SSH access'}]
            }
        ]
    )
    print("[SUCCESS]: Inbound Port 22 rules established.")
except botocore.exceptions.ClientError as error:
    if error.response['Error']['Code'] == 'InvalidPermission.Duplicate':
        print("[WARN]: Inbound Port 22 rule already exists. Proceeding...")
    else:
        raise error

with open("bootstrap_server.sh", "r") as instance_variable:
    try:
        response = client.run_instances(
            ImageId=AMI_ID,
            InstanceType=INSTANCE_TYPE,
            MinCount=1,
            MaxCount=1,
            SecurityGroupIds=[SECURITY_GROUP_ID],
            KeyName=KEY_NAME,
            CreditSpecification={'CpuCredits': 'standard'},
            UserData=instance_variable.read()
        )
        
        launched_instance_id = response['Instances'][0]['InstanceId']
        waiter = client.get_waiter('instance_running')
        
        print(f"[INFO]: Deployment payload sent. Instance ID: {launched_instance_id}")
        print("Waiting for compute node to initialize...")
        
        
        waiter.wait(InstanceIds=[launched_instance_id])
        print("[SUCCESS]: Compute node is now active and running!")
        
        
        status_refresh = client.describe_instances(InstanceIds=[launched_instance_id])
        public_ip = status_refresh['Reservations'][0]['Instances'][0].get('PublicIpAddress')
        
        print("\n==================================================")
        print(f"LIVE INSTANCE PUBLIC IP: {public_ip}")
        print(f"Connect via terminal run: ssh -i {KEY_NAME}.pem ubuntu@{public_ip}")
        print("==================================================")
        
    except botocore.exceptions.ClientError as error:
        print(f"[ERROR]: AWS API Client Error occurred: {error}")
    except Exception as error:
        print(f"[ERROR]: An unexpected error occurred: {error}")