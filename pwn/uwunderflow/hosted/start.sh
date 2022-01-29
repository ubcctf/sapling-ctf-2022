#/usr/bin/bash

docker build -t uwunderflow .
docker run -d --rm -p 1337:1337 --name uwunderflow uwunderflow
