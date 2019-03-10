import json
import random

def lambda_handler(event, context):
    a = random.randint(0,100)
    
    # TODO implement
    return {
        'statusCode': 200,
    #    'body': json.dumps('Hello from Lambda!')
        'number' : a
    }