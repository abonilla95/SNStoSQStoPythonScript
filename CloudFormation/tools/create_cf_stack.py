import boto3
import json


def get_parameters(file_name):
    config_dict = {}
    with open(file_name, 'r') as config:
        config_read = config.read()
        config_dict = json.loads(config_read)
    return config_dict['DeploymentParameters']

def create_cf_stack(cf_client,parameters):
    response = cf_client.create_stack(
        StackName = parameters['StackName'],
        RoleARN = parameters['CloudFormationRoleARN'],
        TemplateURL = parameters['templateUrl'],
        Parameters = [
            {
                'ParameterKey':'pLambdaFunctionName',
                'ParameterValue': parameters['LambdaFunctionName']
            },
            {
                'ParameterKey':'pLambdaCodeBucketName',
                'ParameterValue': parameters['S3BucketForLambdaFunction']
            },
            {
                'ParameterKey':'pLambdaFunctionHandler',
                'ParameterValue': parameters['LambdaFunctionHandler']
            },
            {
                'ParameterKey':'pBucketKeyForCode',
                'ParameterValue': parameters['S3KeyForLambdaFunction']
            },
            {
                'ParameterKey':'pLambdaRole',
                'ParameterValue': parameters['LambdaRole']
            },
            {
                'ParameterKey':'pSnsTopicName',
                'ParameterValue': parameters['SnsTopicName']
            },
            {
                'ParameterKey':'pSqsQueueName',
                'ParameterValue': parameters['SqsQueueName']
            }
        ]
    )

    return response

def main(config_file):
    config_params = get_parameters(config_file)
    cf_client = boto3.client('cloudformation', region_name=config_params['AwsRegion'])
    for x in config_params:
        print(x)
    cf_create_stack = create_cf_stack(cf_client,config_params)
    print(cf_create_stack)


if __name__ == "__main__":
    config_file = 'configurations.json'
    
    main(config_file)

