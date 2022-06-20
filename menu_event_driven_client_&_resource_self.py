import boto3
import sys
aws_mgm_con= boto3.session.Session(profile_name="py-bot")

ec2_con_re = aws_mgm_con.resource(service_name="ec2", region_name="us-east-1")
ec2_con_cli = aws_mgm_con.client(service_name="ec2", region_name="us-east-1")

while True:
    print("This script peforms the following actions on the ec2 instance")
    print("""
        1. Start
        2. Stop
        3. terminate
        4. exit
        """)
#Bina Logic k steps likh do. Baad mein logic add karo aur fir modifications karte jao. 

    opt= int(input("Enter your option:"))
    if opt == 1:
        instance_id=input("Enter your instance id:")
        
        my_req_instance=ec2_con_re.Instance(instance_id)        
        my_req_instance.start()
        print("Starting ec2 instance....")
    elif opt == 2:
        instance_id=input("Enter your instance id:")
        my_req_instance=ec2_con_re.Instance(instance_id)        
        my_req_instance.stop()
        print("Stopping your ec2 instance....")
    elif opt == 3:
        instance_id=input("Enter your instance id:")
        my_req_instance=ec2_con_re.Instance(instance_id)        
        my_req_instance.terminate()
        print("Terminating your EC2 Instance...")
    elif opt == 4:
        print("ThankYou for using this script")
        sys.exit()
    else:
        print("Invalid option, Please check once again")

