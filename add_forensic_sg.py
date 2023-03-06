# This lambda function is part of automated security response
# If an instance is flagged by GD as infected or malicious behavior, 
# and the Instance Id is sent to Lambda from CW Events, we can automatically
# place a forensic SG group on it to limit its access and investigate 

import boto3


def lambda_handler(event, context):
    # Retrieve the instance ID from the event data
    # uncomment the below when passing in the Instance ID from a cloudwatch event
    #instance_id = event['instance_id']
    
    # hard code yourself for testing
    instance_id = "<your test instanceId>"
    
    #pre-built / existing forensic security group that will be added
    security_group_id = "<your forensic sg id>"

    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Attach the forensic security group to an EC2 instance
    response = ec2.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=[security_group_id]
    )

    #print(f"Security group {security_group_id} attached to instance {instance_id}")

