import boto3

"""This script sends a message to the given SNS Topic. 
Replace the following:
    {Add Topic ARN Here} - arn for SNS Topic
    {Add region where Topic Exists} - region where SNS Topic exists
"""


sns_client = boto3.client('sns', region_name='{Add region where Topic Exists}')
response = sns_client.publish(
    TopicArn= "{Add Topic ARN Here}",
    Message="HelloWorld"
)

print(response)
