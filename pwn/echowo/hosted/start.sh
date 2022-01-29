#/usr/bin/bash

docker build -t echowo .
docker run -d --rm -p 1340:1337 --name echowo echowo
