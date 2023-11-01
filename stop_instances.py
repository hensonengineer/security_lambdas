### Function to stop an ec2 instance tagged as infected

import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        ec2 = boto3.client('ec2')
        
        # Stop instances with the tag "status:infected"
        response = ec2.describe_instances(Filters=[{'Name': 'tag:status', 'Values': ['infected']}])
        
        instance_ids = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
        
        if instance_ids:
            ec2.stop_instances(InstanceIds=instance_ids)
            logger.info(f"Stopped instances with 'status:infected' tag: {', '.join(instance_ids)}")
        else:
            logger.info("No instances with 'status:infected' tag found to stop.")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "Error"
