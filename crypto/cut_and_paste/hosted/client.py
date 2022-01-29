# These functions will just access the server the same way you can by hand

# Normally you would need to write your own client to do this
# but for this challenge I'll provide you with a working client

# requires pwntools (https://pypi.org/project/pwntools/)
from pwn import *

# r = remote('localhost', 1337)
r = remote('challenges.ctf.maplebacon.org', 32000)

def register_user(username, password):
    print(f"[Client] Registering user: {username} | passwd: {password}")
    r.sendline("1")
    r.recvuntil("Input your username:")
    r.sendline(username)
    r.recvuntil("Input your password:")
    r.sendline(password)

    debug_stuff = r.recvuntil("Here's").decode()
    for line in debug_stuff.split("\n")[:-1]:
        print(line)

    r.recvuntil("when we add the login feature: ")
    token = r.recvline()
    r.recvuntil(">")
    return token

def admin_login(token):
    print("[Client] Attempting login")
    r.sendline("2")
    r.recvuntil("token: ")
    r.sendline(token)
    print(r.recvline())
    r.recvuntil(">")