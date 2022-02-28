import json
import boto3

#this is template for lambda function which is deployed on aws 
def lambda_handler(event, context):
    client = boto3.resource('dynamodb')
    table = client.Table('Machine')
    response = table.scan()

    if response['Items']:   
        return {
            'statusCode': 200,
            'data': json.dumps(response['Items'])
        }
    else:
        return {
            'statusCode': 400,
            'data': json.dumps("Could not retrieve machines")
        }
