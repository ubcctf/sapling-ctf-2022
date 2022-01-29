#/usr/bin/bash

sudo docker build -t maplectf-pwn-build - < build.dockerfile
sudo docker run --rm --mount type=bind,src="$(pwd)",dst=/mnt maplectf-pwn-build

cp Dockerfile ../hosted/
cp Dockerfile ../players/
cp xinetd.conf ../hosted/
cp xinetd.conf ../players/
cp challenge.sh ../hosted/
cp challenge.sh ../players/
cp banner_fail ../hosted/
cp banner_fail ../players/

cp Makefile ../players/

cp wetuwn-addwess ../hosted/
cp wetuwn-addwess ../players/
cp wetuwn-addwess.c ../players/
