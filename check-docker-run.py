""" Python 3 script to check which docker container are running or not
REF: https://pypi.org/project/docker/
"""
import docker 
client = docker.from_env()
container_list = client.containers.list()
#print(container_list)
#print(type(container_list)) - list type
if not container_list:
    print ("No docker container are running now")
else:
    print("Docker container {0} are running now".format(container_list))
