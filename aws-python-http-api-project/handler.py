import json


def hello(event, context):
    body = {
        "message": "Hello Dosto!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def bye(event, context):
    body = {
        "message": "Bye Dosto!",
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
