FROM python:3

RUN apt-get update && apt-get -y install socat

WORKDIR /chal

RUN pip install --no-cache-dir pycryptodome

COPY oracle.py ./
COPY secrets.py ./

RUN useradd -M ctf
USER ctf:ctf

CMD ["socat", "TCP-LISTEN:1337,fork,reuseaddr", "EXEC:'python ./oracle.py'"]