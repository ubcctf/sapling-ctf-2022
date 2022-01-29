#!/usr/bin/env python3

# creates the emulator, manages timeout and handles r/w
# This file is not part of the challenge and is only needed for hosting reasons!


import subprocess
from subprocess import Popen, PIPE, CalledProcessError
from threading import Thread, Timer
import os
import signal
import sys
import time
import tempfile

def timeout_cleanup():
    global pane_id
    time.sleep(120)
    print("timed out!")
    Popen(["tmux", "kill-pane", "-t", f"ctf.{pane_id}"])
    os.kill(os.getpid(),signal.SIGKILL)

def qemu_stdout():
    global tf
    global tx_empty
    while True:
        line = tf.file.readline()
        if not line:
            tx_empty = True
            time.sleep(0.1)
            continue
        tx_empty = False
        sys.stdout.buffer.write(line)

def read_input():
    global pane_idx
    global tx_empty
    while True:
        try:
            data = sys.stdin.buffer.readline()
        except EOFError:
            # connection terminated, kill vm
            Popen(["tmux", "kill-pane", "-t", f"ctf.{pane_id}"])
            sys.exit(0)
        for c in data:
            if c >= 0x20 and c < 0x7f:
                subprocess.check_call(["tmux", "send-keys", "-t", f"ctf.{pane_id}",  f"{hex(c)}"])
                tx_empty = False
                while not tx_empty:
                    time.sleep(0.02)
                # wait for the character to be displayed
        subprocess.check_call(["tmux", "send-keys", "-t", f"ctf.{pane_id}", "Enter"])


tf = tempfile.NamedTemporaryFile(prefix="qemu-")
debug = ""
if len(sys.argv) > 1 and sys.argv[1] == '1':
    debug = "-debug"
p = Popen(["tmux", "split-window", "-P", "-F", "#{pane_index} #{pane_tty} #{pane_id}", f"./start_qemu.sh {debug} 1>{tf.name}"], stdout=PIPE, universal_newlines=True)
pane_idx, pane_tty, pane_id = p.stdout.read().strip().split()
open("/tmp/CleanupMgr", "w").write(f"{os.getpid()} {pane_id}")
p = Popen(["tmux", "select-layout", "-t", "ctf", "tiled"])
t1 = Thread(target=qemu_stdout, daemon=True)
t2 = Thread(target=read_input, daemon=True)
# the server will auto-disconnect after 120 seconds
t3 = Thread(target=timeout_cleanup, daemon=True)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
