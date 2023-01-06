import boto3

def put_security_group_on_ec2_instance(event, context):
    # Retrieve the instance ID and security group ID from the event data
    # or hardcode the forensic subnet security group
    instance_id = event['instance_id']
    security_group_id = event['security_group_id']

    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Modify the security groups for the instance
    ec2.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=[security_group_id]
    )
