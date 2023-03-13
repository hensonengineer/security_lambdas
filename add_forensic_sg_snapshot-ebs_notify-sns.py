import boto3

def forensic_package(event, context):
    # Get the instance-id from the event
    instance_id = event['instance_id']
    
    #pre-build forensic Security Group ID
    security_group_id = ['<your forensic sg id>']

    # Create EC2 and EBS clients
    ec2 = boto3.client('ec2')
    ebs = boto3.client('ebs')

    # Modify the security groups for the instance
    ec2.modify_instance_attribute(
        InstanceId=instance_id, Groups=[security_group_id]
    )

    # Get the list of volumes attached to the instance
    volumes = ec2.describe_volumes(Filters=[{'Name': 'attachment.instance-id', 'Values': [instance_id]}])['Volumes']

    # Create a snapshot of each volume
    for volume in volumes:
        ebs.create_snapshot(VolumeId=volume['VolumeId'], Description=snapshot_description)

    # Send an SNS message
    sns = boto3.client('sns')
    sns.publish(TopicArn='your-topic-arn', Message='Snapshot created')
