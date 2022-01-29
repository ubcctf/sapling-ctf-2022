#/usr/bin/bash

sudo docker build -t maplectf-pwn-build - < build.dockerfile
sudo docker run --rm --mount type=bind,src="$(pwd)",dst=/mnt maplectf-pwn-build
sudo docker run --rm --mount type=bind,src="$(pwd)",dst=/mnt maplectf-pwn-build "cp" "/lib/x86_64-linux-gnu/libc.so.6" "."

cp Dockerfile ../hosted/
cp Dockerfile ../players/
cp xinetd.conf ../hosted/
cp xinetd.conf ../players/
cp challenge.sh ../hosted/
cp challenge.sh ../players/
cp banner_fail ../hosted/
cp banner_fail ../players/

cp Makefile ../players/

cp wetuwn-to-wibc ../hosted/
cp wetuwn-to-wibc ../players/
cp wetuwn-to-wibc.c ../players/

cp libc.so.6 ../players/
