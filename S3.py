#this file is about lab tests on AWS S3. 

import boto3

aws_mg_con = boto3.session.Session(profile_name = "py-bot", region_name = "us-east-1")
s3=aws_mg_con.client("s3")

print(s3.all)

testing tghe changes done in the file. 
