import boto3
region = 'eu-central-1'

def lambda_handler(event, context):
    client = boto3.client('ec2', region_name=region)
    
    # Put the ID of your instance and the new type:
    instance_id = 'i-xxxxxxxxxxxxx'
    new_type = 'm5.large'
    
    # Stopping the instance
    client.stop_instances(InstanceIds=[instance_id])

    # Waiting for the instance to get stopped
    waiter=client.get_waiter('instance_stopped')
    waiter.wait(InstanceIds=[instance_id])
    
    # Modify the instance type
    client.modify_instance_attribute(InstanceId=instance_id, Attribute='instanceType', Value=new_type)
    print('Instance', instance_id, 'has been modified with the new type (',new_type,')')
    
    # Starting the instance
    client.start_instances(InstanceIds=[instance_id])
    print('Instance', instance_id, 'is starting with the new type')