import boto3

def update_item(event, context):
    # Extract the input values from the event
    id = event['id']
    attribute1 = event['attribute1']
    attribute2 = event['attribute2']

    # Connect to the DynamoDB table
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('my-table')

    # Construct the update expression and expression values
    key = {'id': id}
    update_expression = 'SET attribute1 = :val1, attribute2 = :val2'
    expression_values = {
        ':val1': attribute1,
        ':val2': attribute2
    }

    # Update the item in the table
    response = table.update_item(
        Key=key,
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_values
    )

    return response
