import boto3

def put_security_group_on_ec2_instance_and_create_ebs_snapshot(event, context):
    # Retrieve the instance ID, security group ID, and snapshot description from the event data
    instance_id = event['instance_id']
    security_group_id = event['security_group_id']
    snapshot_description = event['snapshot_description']

    # Create EC2 and EBS clients
    ec2 = boto3.client('ec2')
    ebs = boto3.client('ebs')

    # Modify the security groups for the instance
    ec2.modify_instance_attribute(
        InstanceId=instance_id,
        Groups=[security_group_id]
    )

    # Get the list of volumes attached to the instance
    volumes = ec2.describe_volumes(Filters=[{'Name': 'attachment.instance-id', 'Values': [instance_id]}])['Volumes']

    # Create a snapshot of each volume
    for volume in volumes:
        ebs.create_snapshot(VolumeId=volume['VolumeId'], Description=snapshot_description)

    # Send an SNS message
    sns = boto3.client('sns')
    sns.publish(TopicArn='your-topic-arn', Message='Snapshot created')
