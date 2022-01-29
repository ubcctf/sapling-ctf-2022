#/usr/bin/bash

docker build -t wetuwn-addwess .
docker run -d --rm -p 1339:1337 --name wetuwn-addwess wetuwn-addwess
