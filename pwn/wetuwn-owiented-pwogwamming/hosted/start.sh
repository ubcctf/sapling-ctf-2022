#/usr/bin/bash

docker build -t wetuwn-owiented-pwogwamming .
docker run -d --rm -p 1444:1337 --name wetuwn-owiented-pwogwamming wetuwn-owiented-pwogwamming
