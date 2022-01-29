FROM ubuntu:20.04

RUN apt-get update && \
    apt-get -y install socat tmux qemu-system-arm python3

# tools you'll probably need for this challenge
RUN apt-get update && \
    apt-get -y install binutils-arm-none-eabi gdb-multiarch

WORKDIR /chal

COPY image.elf image.bin start_qemu.sh send.py cleanup_mgr.py setup.sh ./

RUN useradd -M ctf
USER ctf:ctf

RUN tmux new -s ctf -d 

CMD ["./setup.sh"]
