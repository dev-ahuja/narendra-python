import boto3

aws_mgm_con= boto3.session.Session(profile_name="py-bot")

ec2_con_re = aws_mgm_con.resource(service_name="ec2", region_name="us-east-1")
ec2_con_cli = aws_mgm_con.client(service_name="ec2, region_name="us-east-1")

while True:
    print("This script peforms the following actions on the ec2 instance")
    print("""
        1. Start
        2. Stop
        3. terminate
        4. exit
        """)

opt= int(input("Enter your option:))
if opt == 1:
    print("Starting ec2 instance....")
elif opt == 2:
    print("Stopping your ec2 instance....")
elif opt == 3:
    print("Terminating your EC2 Instance...")
elif opt == 4:
    print("Exiting the EC2 Instance....")
else:
    print("No Desired action")

