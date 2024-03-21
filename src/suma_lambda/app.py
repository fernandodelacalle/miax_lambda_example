import json


def lambda_handler(event, context):
    print(event.get("queryStringParameters"))
    params = event.get("queryStringParameters")
    try:
        a = int(params["a"])
        b = int(params["b"])
    except Exception:
        return {
            'statusCode': 400,
            'body': json.dumps("no valid")
        }
    result = a + b
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
