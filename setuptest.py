import boto3

aws_mgm_con = boto3.session.Session(profile_name="py-bot")
iam_con = aws_mgm_con.resource('iam')

for each_user in iam_con.users.all():
    print(each_user.name)


#aws_mgm_con = boto3.session.Session(profile_name="py-bot")
s3_con = aws_mgm_con.resource('s3')

for each_bucket in s3_con.buckets.all():
    print(each_bucket.name)