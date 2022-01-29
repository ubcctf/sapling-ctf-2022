from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Util.Padding import pad

flag = b'maple{aMAZE1ng_job!11!1}'
hasher = SHA256.new()
hasher.update(b'sqasasaaawwqqqqdqqwdedddwq')
key = hasher.digest()
iv = b'0123456789012345'
cipher = AES.new(key, AES.MODE_CBC, iv)
b = cipher.encrypt(pad(flag, AES.block_size))
f = open("flag.enc", "wb")
f.write(b)

ct = b"\xc6\x3d\x55\x7c\x57\x2e\xdd\xeb\x45\xf3\x2c\x7c\x83\xa5\x6d\x41\x3b\x5c\x31\x8e\x3d\xce\xa8\x0c\x4e\x53\x8e\xc2\x4d\x55\x90\x73"
cipher = AES.new(key, AES.MODE_CBC, iv)
print(cipher.decrypt(ct))
print(key)