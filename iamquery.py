import boto3
import datetime
session= boto3.session.Session(profile_name = "py-bot")
iam_con = session.resource(service_name="iam")

#getting details of any iam user. 
iam_user_ob = iam_con.User("boto3-learn")
#print(iam_user_ob.user_name,iam_user_ob.user_id,iam_user_ob.arn,iam_user_ob.create_date.strftime("%Y-%m-%d"))

for each_user in iam_con.users.all():
    print(each_user)
