# This lambda function is part of automated security response
# If an instance is flagged by GD as infected or malicious behavior, 
# and the Instance Id is sent to Lambda from CW Events, we can automatically
# place a forensic SG group on it to limit its access and investigate 

import boto3

def lambda_handler(event, context):
    try:
        # Retrieve the instance ID from the event data
        instance_id = event['instance_id']
        
        # Pre-built / existing forensic security group that will be added
        security_group_id = "<your forensic sg id>"
        
        # Create an EC2 client
        ec2 = boto3.client('ec2')
        
        # Attach the forensic security group to an EC2 instance
        response = ec2.modify_instance_attribute(
            InstanceId=instance_id,
            Groups=[security_group_id]
        )
        
        return f"Security group {security_group_id} attached to instance {instance_id}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

