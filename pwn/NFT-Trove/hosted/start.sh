#!/bin/bash

docker build -t nft-trove .
docker run -d --rm -p 31337 --name nft-trove nft-trove
