FROM ubuntu:20.04

RUN apt-get update && apt-get -y install socat python3

WORKDIR /chal

COPY decode-me.py ./
COPY flag.txt ./

RUN useradd -M ctf
USER ctf:ctf

CMD ["socat", "TCP-LISTEN:1420,fork,reuseaddr", "EXEC:'./decode-me.py'"]
