#/usr/bin/bash

docker build -t rust_1:latest .
docker run -d --rm -p 1337:1337 --name rust_1 rust_1