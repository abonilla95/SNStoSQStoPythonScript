import boto3

"""python script to gather messages from an SQS Queue
Replace the Following:
    {add region where SQS exists} - region where SQS Queue exists 
    {add url for sqs queue here} - url for sqs queue
"""

def get_message(sqs_client, queue_url):
    """gets messages contained within the given queue url
    
    Arguments:
        sqs_client {boto3.client} -- boto3 client set to the region where the sqs queue exists
        queue_url {sting} -- url for the given sqs queue
    """
    response = sqs_client.receive_message(
        QueueUrl = queue_url,
        MaxNumberOfMessages=1,
        AttributeNames=[
            "All"
        ]
    )
    return response

def get_message_body(sqs_response):
    message_bodies = [message['Body'] for message in sqs_response['Messages']]
    return message_bodies

if __name__ == "__main__":
    sqs_client = boto3.client('sqs', region_name='{add region where SQS exists}')
    sqs_url = '{add url for sqs queue here}'
    sqs_response = get_message(sqs_client, sqs_url)
    message_body = get_message_body(sqs_response)
    for message in message_body:
        print(message)