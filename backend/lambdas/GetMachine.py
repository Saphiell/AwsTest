import json
import boto3

#this is template for lambda function which is deployed on aws 
def lambda_handler(event, context):
    client = boto3.client('dynamodb')
    machinePosition = client.get_item(
        TableName='MachinePosition',
        Key={
            'SerialNumber':{
                    'S':event['serialNumber']
                }
            }
        )
    machine =  client.get_item(
        TableName='Machine',
        Key={
                'SerialNumber':{
                    'S':event['serialNumber']
                },
                'Name':{
                    'S':event['name']
                }    
            }
        )  
    response = {"name":machine['Item']['Name'],
                "serialNumber":event['serialNumber'],
                "state":machine['Item']['State'],
                "position": machinePosition['Item']
                }
    if response:   
        return {
            'statusCode': 200,
            'data': json.dumps(response)
        }
    else:
        return {
            'statusCode': 400,
            'data': json.dumps("Could not retrieve latest logs")
        }
        