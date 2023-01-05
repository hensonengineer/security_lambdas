import boto3

def revoke_ip_address_from_security_group(event, context):
    # Retrieve the security group ID, IP address, and port from the event data
    security_group_id = event['security_group_id']
    ip_address = event['ip_address']
    port = event['port']

    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Revoke the IP address and port from the security group
    ec2.revoke_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {
                'IpProtocol': 'tcp',
                'FromPort': port,
                'ToPort': port,
                'IpRanges': [
                    {
                        'CidrIp': ip_address + '/32'
                    }
                ]
            }
        ]
    )
