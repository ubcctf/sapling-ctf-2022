#!/bin/bash

docker build -t nft-trove .
# port 31337 for chall, 1234 for gdb (see `start_qemu.sh`)
docker run -d --rm -p 31337:31337 -p 1234:1234 -e QEMU_DEBUG="${QEMU_DEBUG}" --name nft-trove nft-trove
