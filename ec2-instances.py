import boto3
from pprint import pprint
aws_mgm_con = boto3.session.Session(profile_name = "py-bot")

ec2_con_cli = aws_mgm_con.client(service_name="ec2", region_name="us-east-1")

response = ec2_con_cli.describe_instances()['Reservations']

for each_item in response:
    for each in each_item['Instances']:
        print("The image ID is: {}\n The Instance ID is: {}\n The machine launched on: {}".format(each['ImageId'],each['InstanceId'],each['LaunchTime'].strftime("%d-%m-%y")))

