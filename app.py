import boto3
import dev2

client = boto3.client('ec2')
response = client.run_instances(
    ImageId='ami-0453ec754f44f9a4a',
    InstanceType='t2.micro',
    KeyName = 'devops',

    MaxCount=1,
    MinCount=2,
)
