#/usr/bin/bash

docker build -t propagation:latest .
docker run -d --rm -p 1337:1337 --name propagation propagation