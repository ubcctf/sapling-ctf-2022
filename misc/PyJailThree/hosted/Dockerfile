FROM python:3

RUN apt-get update && apt-get -y install socat

WORKDIR /chal

RUN pip install --no-cache-dir pycryptodome

COPY . .

RUN adduser --system ctf
USER ctf:nogroup

EXPOSE 2020

CMD ["socat", "TCP-LISTEN:2020,fork,reuseaddr", "EXEC:'python ./pyjailtwo.py'"]