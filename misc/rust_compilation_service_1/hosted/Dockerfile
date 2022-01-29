FROM rust:1.57-slim

RUN apt-get update && apt-get -y install socat python3-pip

WORKDIR /chal

RUN pip install --no-cache-dir Flask Flask-Limiter

COPY server.py ./
COPY flag.txt ./

RUN useradd -M ctf
RUN mkdir /chal/uploads \
    && chown ctf:ctf /chal/uploads

USER ctf:ctf

CMD ["python3", "./server.py"]