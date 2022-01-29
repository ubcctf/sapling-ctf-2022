#!/usr/bin/env python3

# Make sure the emulator is always cleaned up when connection closes
# This file is not part of the challenge and is only needed for hosting reasons!

import os
import time
from subprocess import Popen

instance = {}
os.mkfifo("/tmp/CleanupMgr")
fifo = open("/tmp/CleanupMgr", "r")

while True:
    while True:
        for pid, pane_id in instance.copy().items():
            # check if instance still exists
            try:
                os.kill(pid, 0)
            except OSError:
                try:
                    Popen(["tmux", "kill-pane", "-t", f"ctf.{pane_id}"])
                except:
                    pass
                instance.pop(pid, None)
        try:
            line = fifo.readline()
            if not line:
                break
            send_pid, pane_id = line.split(" ")
            instance[int(send_pid)] = pane_id
        except:
            pass
    time.sleep(0.1)
