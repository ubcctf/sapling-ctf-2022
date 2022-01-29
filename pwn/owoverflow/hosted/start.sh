#/usr/bin/bash

docker build -t owoverflow .
docker run -d --rm -p 1338:1337 --name owoverflow owoverflow
