from ubuntu:20.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get update && apt-get install -y python3 python3-pip xinetd
RUN useradd --create-home --shell /bin/bash ctf
COPY players/ /home/ctf/players
RUN pip3 install -r /home/ctf/players/requirements.txt

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY checkreplay.sh /checkreplay.sh
COPY flags/ /home/ctf/players/flags
COPY banner_fail.txt /home/ctf/banner_fail.txt
COPY main_hosted.py /home/ctf/players/Game

EXPOSE 1337

CMD ["xinetd", "-f", "/etc/xinetd.d/ctf", "-dontfork"]