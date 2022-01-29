FROM ubuntu:20.04

RUN apt-get update && apt-get -y install socat

WORKDIR /chal

COPY whats_up_sys ./
COPY flag.txt ./

RUN useradd -M ctf
USER ctf:ctf

CMD ["socat", "TCP-LISTEN:5433,fork,reuseaddr","EXEC:'./whats_up_sys'"]