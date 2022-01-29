FROM python:3

COPY ./requirements.txt /app/requirements.txt

WORKDIR /usr/src/app

RUN pip install -r /app/requirements.txt

COPY . .

EXPOSE 8991

ENTRYPOINT [ "python3" ]

CMD [ "server.py" ]