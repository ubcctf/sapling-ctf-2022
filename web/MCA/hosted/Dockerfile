FROM python:3

COPY ./requirements.txt /app/requirements.txt

WORKDIR /usr/src/app

RUN pip install -r /app/requirements.txt

COPY . .

# User
#RUN addgroup -S ctf && adduser -S ctf -G ctf
#USER ctf:ctf

EXPOSE 5000

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]