#/usr/bin/bash

docker build -t wetuwn-to-wibc .
docker run -d --rm -p 1443:1337 --name wetuwn-to-wibc wetuwn-to-wibc
