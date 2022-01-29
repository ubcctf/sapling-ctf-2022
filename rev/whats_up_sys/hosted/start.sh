#/usr/bin/bash

docker build -t whats_up_sys .
docker run -d --rm -p 5433:5433 --name whats_up_sys whats_up_sys