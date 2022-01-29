FROM ubuntu:20.04

RUN apt-get update && apt-get -y install socat python3

WORKDIR /chal

COPY encode-me.py ./
COPY flag.txt ./

RUN useradd -M ctf
USER ctf:ctf

CMD ["socat", "TCP-LISTEN:1421,fork,reuseaddr", "EXEC:'./encode-me.py'"]
