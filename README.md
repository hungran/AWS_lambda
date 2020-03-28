# AWS_lambda
## IAM_POLICY for `lambda's role`
```
{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ],
        "Resource": "arn:aws:logs:*:*:*"
      },
      {
        "Effect": "Allow",
        "Action": [
          "ec2:StopInstances",
          "ec2:StartInstances",
          "ec2:De*"
        ],
        "Resource":"*"
        }
    ]
} 
```
## lambda_function.py
```
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
region = 'ap-southeast-1'

def lambda_handler(event, context):
    ec2 = boto3.resource('ec2', region_name=region)
    #Filter EC2 with tag
    instances = ec2.instances.filter(
    Filters=[
        {
            'Name': 'tag:Scheduled',
            'Values': ['True']
        }
    ]
    )
    #Get all instances
    for instance in instances.all():
        #Definde instance_state
        instance_state = instance.state['Name']
        #Start or stop instance if instance running or stopped then print
        if instance_state == 'stopped':
            instance.start()
            print('staring instance id: ' + str(instance.id))
        elif instance_state == 'running':
            instance.stop()
            print('stopping instance id: ' + str(instance.id))
#        else:
#            print ('no action need')
```