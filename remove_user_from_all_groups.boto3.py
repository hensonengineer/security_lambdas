import boto3

def remove_user_from_groups(event, context):
    # Get the name of the user to remove from the event data
    user_name = event['user_name']

    # Create an IAM client
    iam = boto3.client('iam')

    # Get a list of all groups that the user is a member of
    groups = iam.list_groups_for_user(UserName=user_name)['Groups']

    # Remove the user from each group
    for group in groups:
        group_name = group['GroupName']
        iam.remove_user_from_group(GroupName=group_name, UserName=user_name)
