import json
import boto3

#this is template for lambda function which is deployed on aws 
def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    response = client.update_item(
        TableName = "Machine",
        Key = {
            'SerialNumber':{
                'S' : event['serialNumber']
            },
            'Name':{'S':event['name']}
        },
        UpdateExpression="set #s=:s",
        ExpressionAttributeValues={
            ':s':{'S': event['state'] }
        },
        ExpressionAttributeNames={
            "#s": "State"
        },
        ReturnValues="UPDATED_NEW"
        )
    print(response)
    if response:   
        return {
            'statusCode': 200,
            'data': json.dumps(response)
        }
    else:
        return {
            'statusCode': 400,
            'data': json.dumps("Could not retrieve machines")
        }
