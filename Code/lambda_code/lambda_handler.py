import boto3
import json
"""This script will run on the lambda function and all it does is print out the 
message passed to the lambda_handler function
"""

def lambda_handler(event,context):
    for message in event['Records']:
        print(message['Sns']['Message'])

if __name__ == "__main__":
    lambda_handler(None, None)