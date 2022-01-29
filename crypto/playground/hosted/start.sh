#/usr/bin/bash

docker build -t playground:latest .
docker run -d --rm -p 1337:1337 --name playground playground