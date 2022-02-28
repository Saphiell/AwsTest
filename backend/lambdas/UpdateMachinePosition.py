import json
import boto3

#this is template for lambda function which is deployed on aws 
def lambda_handler(event, context):
    print(event)
    client = boto3.client('dynamodb')
    response = client.update_item(
        TableName = "MachinePosition",
        Key = {
            'SerialNumber':{
                'S' : event['machine']['serialNumber']
            }
        },
        UpdateExpression="set #x=:x, #y=:y, #t=:t ",
        ExpressionAttributeValues={
            ':x':{'N': event['machine']['posX'] },
            ':y':{'N': event['machine']['posY'] },
            ':t':{'N': event['machine']['theta'] },
        },
        ExpressionAttributeNames={
            "#x": "PosX",
            "#y": "PosY",
            "#t": "Theta",
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
