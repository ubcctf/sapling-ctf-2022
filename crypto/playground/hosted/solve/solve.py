from Crypto.Util.number import long_to_bytes, bytes_to_long
import server as chal_server
import baby_aes

from pwn import *

# enc_flag = server.enc_flag
# encrypt_me = server.encrypt
# context.log_level = 'debug' # uncomment to enable debugging
# r = remote("localhost", 1337)
r = remote('challenges.ctf.maplebacon.org', 32001)

r.recvuntil("Encrypted flag: ")
enc_flag_hex = r.recvline().decode()
enc_flag = bytes.fromhex(enc_flag_hex.strip())

r.recvuntil("(hex)")
def encrypt_me(ptxt):
    r.sendline(ptxt.hex())
    res = r.recvline().decode()
    r.recvuntil("(hex)")
    return bytes.fromhex(res.strip())

def f(xs,k):
    s = baby_aes.bytes2matrix(xs)

    baby_aes.sub_bytes(s)
    baby_aes.shift_rows(s)
    baby_aes.mix_columns(s)
    baby_aes.add_round_key(s,k)

    return baby_aes.matrix2bytes(s)

def round(xs,k):
    l = chal_server.lh(xs)
    r = chal_server.rh(xs)
    return r + chal_server.xor(l, f(r, k))

# the lazy lady's slide attack
key = []
for key_idx in range(64):
    print(key)
    base = long_to_bytes(key_idx, 32)
    base_res = encrypt_me(base)
    goal = chal_server.rh(base_res)

    for key_guess in range(256):
        stepped = round(base, key_guess)
        res = encrypt_me(stepped)
        if chal_server.lh(res) == goal:
            key.append(key_guess)
            break
    else:
        print(f"Huh??? Failed to get a guess, key = {key}")

print(f"Recovered key = {key}")
# print(f"real key = {[x for x in baby_aes.KEY]} | {baby_aes.KEY == bytes(key)}")

key = bytes(key)
# key = baby_aes.KEY

def dec_round(ctxt):
    l = chal_server.lh(ctxt)
    r = chal_server.rh(ctxt)
    k = key[bytes_to_long(l) % 64]
    return chal_server.xor(r, f(l,k)) + l

def decrypt(ctxt):
    assert len(ctxt) == 32

    ptxt = ctxt
    for _ in range(16): 
        # round and round it goes
        ptxt = dec_round(ptxt)
    return ptxt

print("flag", decrypt(enc_flag))
