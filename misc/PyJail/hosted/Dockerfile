FROM python:3

RUN apt-get update && apt-get -y install socat

WORKDIR /chal

RUN pip install --no-cache-dir pycryptodome

COPY pyjail.py ./
COPY secrets/flag/topsecret.txt ./secrets/flag/

RUN adduser --system ctf
USER ctf:ctf

EXPOSE 2021

CMD ["socat", "TCP-LISTEN:2021,fork,reuseaddr", "EXEC:'python ./pyjail.py'"]