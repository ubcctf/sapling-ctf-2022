#/usr/bin/bash

docker build -t pwintf .
docker run -d --rm -p 1442:1337 --name pwintf pwintf
