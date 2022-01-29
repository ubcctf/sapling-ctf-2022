FROM ubuntu:20.04

RUN apt-get update && apt-get -y install build-essential

WORKDIR /mnt

CMD make
