#/usr/bin/bash

docker build -t encode-me .
docker run -d --rm -p 1421:1421 --name encode-me encode-me
