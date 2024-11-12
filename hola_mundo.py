# HolaMundo.py

def hola_mundo(event, context):
    
    print('Hola Mundo')

    body = {'message': 'Hola Mundo'}

    header = {}
    header['Content-Type'] = 'application/json'
    header['Access-Control-Allow-Headers'] = 'Content-Type'
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Methods'] = 'OPTIONS,POST,GET'
    #header['Access-Control-Allow-Credentials'] = 'true',
    response = {
        'isBase64Encoded': False,
        'statusCode': 202,
        'headers': header,
        'body': body 
    }

    return response