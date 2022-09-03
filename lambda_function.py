import json
import boto3
from decimal import Decimal

# DynamoDBのテーブルにアクセス
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('http-crud-tutorial-items')

# Decimal型をJSONに変換するための関数
def json_serialize(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError
    
def lambda_handler(event, context):
    
    # TODO implement
    statusCode = 200
    headers = { 'Content-Type': 'application/json' }
    
    try:
        routeKey = event['routeKey']
        if routeKey == 'DELETE /items/{id}':
            id = event['pathParameters']['id']
            table.delete_item(Key={'id': id})
            body = f"Deleted item {id}"
        
        elif routeKey == 'GET /items/{id}':
            id = event['pathParameters']['id']
            body = table.get_item(Key={'id': id})
        
        elif routeKey == 'GET /items':
            body = table.scan()
        
        elif routeKey == 'PUT /items':
            request = json.loads(event['body'])
            table.put_item(Item=
            {
                'id': request['id'],
                'price': request['price'],
                'name': request['name']
            })
            body = f"Put item {request['id']}"
        else:
            raise ValueError(f"Unsupported route: {routeKey}")
        
    
    except Exception as err:
        statusCode = 400
        body = err
            
    finally:
        body = json.dumps(body, default=json_serialize)
    
    return {
        'statusCode': statusCode,
        'headers': headers,
        'body': body
    }

