#!/bin/bash

tmux new -s ctf -d
python3 cleanup_mgr.py &
socat TCP-LISTEN:31337,fork,nodelay,reuseaddr EXEC:"python3 -u ./send.py ${QEMU_DEBUG}"
