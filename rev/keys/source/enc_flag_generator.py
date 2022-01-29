key = b"\x4a\x83\x04\xd5"
flag = b'maple{th3_KEY_IS_H4RDC0D3d_1n_THE_B1n4ry}'
enc_flag = b''
for i in range(len(flag)):
    enc_flag += bytes([flag[i] ^ key[i % len(key)]])
print(len(flag)==len(enc_flag))
print(''.join(r'\x'+hex(letter)[2:] for letter in enc_flag))