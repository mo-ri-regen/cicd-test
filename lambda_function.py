import json


def lambda_handler(event, context):
    # return {"statusCode": 500, "body": json.dumps({"message": "Hello, Lambda!"})}
    return {"statusCode": 200, "body": json.dumps({"message": "Hello, Lambda!"})}
