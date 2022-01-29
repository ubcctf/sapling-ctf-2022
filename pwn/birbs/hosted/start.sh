#/usr/bin/bash

docker build -t birbs .
docker run -d --rm -p 4040:4040 --name birbs birbs