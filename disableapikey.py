import boto3

def lambda_handler(event, context):
    # Connect to IAM client
    iam = boto3.client('iam')
    
    # Get the user name from the event
    user_name = event['user_name']
    
    # Get all access keys for the user
    access_keys = iam.list_access_keys(UserName=user_name)
    
    # Iterate through each access key and disable it
    for key in access_keys['AccessKeyMetadata']:
        iam.update_access_key(UserName=user_name, AccessKeyId=key['AccessKeyId'], Status='Inactive')
        
    return "Successfully disabled API key for user {}".format(user_name)
