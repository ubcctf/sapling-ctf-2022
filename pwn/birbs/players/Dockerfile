FROM ubuntu:20.04

RUN apt-get update && apt-get -y install socat

WORKDIR /chal

COPY birbs ./
COPY flag.txt ./

RUN useradd -M ctf
USER ctf:ctf

CMD ["socat", "TCP-LISTEN:4040,fork,reuseaddr", "EXEC:'./uwunderflow'"]