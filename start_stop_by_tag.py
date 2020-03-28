import boto3
import logging

def lambda_handler(event, context):
    region = 'ap-southeast-1'
    ec2 = boto3.resource('ec2', region_name=region)
#    client = boto3.client('ec2', region_name=region)
    
#    instance = ec2.Istance('id')
    filters=[
        {
            'Name': 'tag:Scheduled',
            'Values': ['True']
        },
        {
            'Name': 'instance-state-name',
            'Values': ['stopped']
        }
    ]
    ec2.instance.filter(Filters=filters).start()