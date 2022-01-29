FROM python:3

RUN apt-get update && apt-get -y install socat

WORKDIR /chal

RUN pip install --no-cache-dir pycryptodome

COPY server.py secret.py baby_aes.py ./

RUN adduser --system ctf
USER ctf:nogroup

CMD ["socat", "TCP-LISTEN:1337,fork,reuseaddr", "EXEC:'python ./server.py'"]