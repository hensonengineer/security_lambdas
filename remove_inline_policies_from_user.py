import boto3

def remove_user_policies(event, context):
    # Get the name of the user to remove policies from the event data
    user_name = event['user_name']

    # Create an IAM client
    iam = boto3.client('iam')

    # Get a list of all policies attached to the user
    policies = iam.list_attached_user_policies(UserName=user_name)['AttachedPolicies']

    # Detach each policy from the user
    for policy in policies:
        policy_arn = policy['PolicyArn']
        iam.detach_user_policy(UserName=user_name, PolicyArn=policy_arn)
