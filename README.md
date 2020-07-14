Wordpress customized image to deploy in ECS container

what are included 
- newly added code files are automatically changed to www-root permissions
- also if we modified the existed files from wordpress, it also set with www-root permissions
- force SSL, redirect to https and set plugin files size settings in wp-config.php

How to build an image
- install docker in your local
- docker build --tag <image-name> <path> ---> use "." in path if you want to add files to the container in the current dir
