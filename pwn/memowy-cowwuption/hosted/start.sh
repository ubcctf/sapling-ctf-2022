#/usr/bin/bash

docker build -t memowy-cowwuption .
docker run -d --rm -p 1441:1337 --name memowy-cowwuption memowy-cowwuption
