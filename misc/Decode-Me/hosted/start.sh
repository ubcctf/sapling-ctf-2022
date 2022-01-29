#/usr/bin/bash

docker build -t decode-me .
docker run -d --rm -p 1420:1420 --name decode-me decode-me
