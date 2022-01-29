#/usr/bin/bash

docker build -t baby-pwintf .
docker run -d --rm -p 1445:1337 --name baby-pwintf baby-pwintf
