# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 21:12:08 2018
@author: G.Poudel
"""
import docker
import time
import boto3
import os
import paramiko

def lambda_handler(event, context):

    ec2 = boto3.resource('ec2', region_name='us-east-1')

    instance_id = 'i-048b7919a6526dc34'

    instance = ec2.Instance(instance_id)

    # Start the instance
    instance.start()

    # Giving some time to start the instance completely
   # time.sleep(60)

    # Print few details of the instance
    print("Instance id - ", instance.id)
    print("Instance public IP - ", instance.public_ip_address)
    print("Instance private IP - ", instance.private_ip_address)
    print("Public dns name - ", instance.public_dns_name)
    print("----------------------------------------------------")

    # Connect to S3, we will use it get the pem key file of your ec2 instance
    s3_client = boto3.client('s3')

    # Download private key file from secure S3 bucket
    # and save it inside /tmp/ folder of lambda event
    s3_client.download_file('swelambdakeyfile', 'zl-belive-test.pem',
                            '/tmp/belive-test-old.pem')

    # Allowing few seconds for the download to complete
    time.sleep(20)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    privkey = paramiko.RSAKey.from_private_key_file('/tmp/belive-test-old.pem')
    # username is most likely 'ec2-user' or 'root' or 'ubuntu'
    # depending upon yor ec2 AMI
    ssh.connect(instance.public_dns_name, username='ubuntu', pkey=privkey)
    cmd = 'sh /home/ubuntu/swe/startcontainer.sh'
    checkstatus = 'service mongod status'

    stdin, stdout, stderr = ssh.exec_command(cmd)
    stdin.flush()
    stdin, stdout, stderr = ssh.exec_command(checkstatus)
    print(stdout.read())

    ssh.close()

    # Stop the instance
    #instance.stop()