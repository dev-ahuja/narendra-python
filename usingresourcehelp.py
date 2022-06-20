#Implement Python Boto3 using CLIENT object and using boto3 help on client.

import boto3
from pprint import pprint
aws_mgm_con = boto3.session.Session(profile_name="py-bot")

#now working with s3, iam & ec2
iam_con_re = aws_mgm_con.resource(service_name="iam", region_name="us-east-1")
s3_con_re = aws_mgm_con.resource(service_name="s3", region_name="us-east-1")
ec2_con_re = aws_mgm_con.resource(service_name="ec2", region_name="us-east-1")

'''
response = iam_con_cli.list_users()

for each_item in response['Users']:
    print(each_item['UserName'])
'''
print(dir(ec2_con_re))