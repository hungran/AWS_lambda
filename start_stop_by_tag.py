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