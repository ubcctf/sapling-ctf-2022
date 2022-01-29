#/usr/bin/bash

docker build -t rust_2:latest .
docker run -d --rm -p 1337:1337 --name rust_2 rust_2