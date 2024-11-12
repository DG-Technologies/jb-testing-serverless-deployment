# HelloWorld.py

def hello_world(event, context):
    print('Hello, World!')

    body = {'message': 'Hello, World!'}

    header = {}
    header['Content-Type'] = 'application/json'
    header['Access-Control-Allow-Headers'] = 'Content-Type'
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Methods'] = 'OPTIONS,POST,GET'
    #header['Access-Control-Allow-Credentials'] = 'true',
    response = {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': header,
        'body': body 
    }

    return response