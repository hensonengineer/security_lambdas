import boto3

def remove_user_from_roles(event, context):
    # Get the name of the user to remove from the event data
    user_name = event['user_name']

    # Create an IAM client
    iam = boto3.client('iam')

    # Get a list of all roles that the user is a member of
    roles = iam.list_roles()['Roles']

    # Remove the user from each role
    for role in roles:
        role_name = role['RoleName']
        iam.remove_user_from_role(RoleName=role_name, UserName=user_name)
