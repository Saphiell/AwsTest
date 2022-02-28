import json
import boto3

#this is template for lambda function which is deployed on aws 
def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    machineLatest = client.get_item(
        TableName='MachinePosition',
        Key={
            'SerialNumber':{
                    'S':event['serialNumber']
                }
            }
        )
    if machineLatest:   
        return {
            'statusCode': 200,
            'data': json.dumps(machineLatest['Item'])
        }
    else:
        return {
            'statusCode': 400,
            'data': json.dumps("Could not retrieve latest logs")
        }
        
