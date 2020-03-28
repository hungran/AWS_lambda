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
        "ec2:DescribeTags"
        ],
        "Resource":"arn:aws:lambda:*:*:*"
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
#    client = boto3.client('ec2', region_name=region)
#    instance = ec2.istances('id')
instances = ec2.instances.filter(
Filters=[
{
    'Name': 'tag:Scheduled',
    'Values': ['True']
}
]
)
for instance in instances.all():
instance_state = instance.state['Name']
if instance_state == 'stopped':
    instance.start()
else:
    print (instance.id , instance.state)
    print ('starting instances:' + str(instance.id))
```