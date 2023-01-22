import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    #stop any instance in running state. DANGER! 
    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

    #stop any instance in dev
    #response = ec2.describe_instances(Filters=[{'Name': 'tag:Environment', 'Values': ['dev']}])
    instance_ids = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    ec2.stop_instances(InstanceIds=instance_ids)


