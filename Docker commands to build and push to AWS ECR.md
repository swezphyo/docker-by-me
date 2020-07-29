# Docker commands to build and push to AWS ECR

### Pre-requisities:

- aws cli 

- docker

  

### Steps to follow:

1. Go to your code file location(**Dockerfile**) and start building your docker image by running 

```
$ sudo docker build .
```



2. Check the docker images with this:

```
$ sudo docker images 
```

- From that, you will able to see the newly build docker image.


3.Tag your image with specific name and tag.

```
$ sudo docker tag <image_id> <name>:<tag>
```



4. After that, log in to aws ecr: 

* Type `aws configure` by adding your aws credentials.

* then type this command to get access to AWS ECR (repository) to push the docker image.

```
$ aws ecr get-login --region us-east-1 --no-include-email
```

5. Copy and paste the output from terminal.

6. Follow the below steps if you succeeded the login to AWS.

   `$ sudo docker images`

7. Tag your image with ECR repo name to upload to ECR ***`(get ecr repository url from AWS-ECR console.)`***

```
$ sudo docker tag <name>:<tag>  <ecr-repo>:<tag>
```

8. Push your tagged image to ECR.

```
$ sudo docker push <ecr-repo>:<tag>
```

