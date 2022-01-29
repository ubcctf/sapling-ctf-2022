#/usr/bin/bash

docker build -t cut_and_paste:latest .
docker run -d --rm -p 1337:1337 --name cut_and_paste cut_and_paste